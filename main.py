# DD_Utility.py
# 1 Nov 2023
# Rendition: 0.3
# By Logan Jones, loganpjjones@gmail.com

# Importing
import sys
import os
import tkinter as tk
from tkinter import font
import pygame
import threading
import time
from Entity import Entity

# Create Window
window = tk.Tk()
window.title("DD Utility")

# initializing tools
pygame.init()
pygame.mixer.init()

'''
# Create Label
greeting = tk.Label(
    text="Hello, World!",
    foreground="#5E1D92",
    background="black",
    width=10,
    height=5)
greeting.pack()

# Entry
entry = tk.Entry(
    width=50)
entry.pack()

# text box
text = tk.Text(
    width=60,
    height=5)
text.pack()

scale = tk.Scale(window, from_=0, to=100, orient=tk.VERTICAL)
scale.pack()
'''

'''
=====================================================================================================================
defining sound board functions
'''
def playStop(id):
    channel = pygame.mixer.Channel(id)
    if isPlaying[id]:
        sounds[id].stop()
        isPlaying[id] = False
        playStopButtonList[id].config(bg="#269CCB")
    else:
        if doesLoop[id]:
            channel.play(sounds[id], loops=-1)
            isPlaying[id] = True
            playStopButtonList[id].config(bg="#5E1D92")
        else:
            channel.play(sounds[id])
            isPlaying[id] = True
            playStopButtonList[id].config(bg="#5E1D92")
            t = threading.Thread(target=reset_button_color, args=(id,))
            t.start()
def volumeChange(id, value):
    sounds[id].set_volume(float(value)/100.0)
def toggleLoop(id):
    if doesLoop[id]:
        doesLoop[id] = False
        loopButtonList[id].config(bg="#269CCB")
        sounds[id].stop()
        isPlaying[id] = False
        playStopButtonList[id].config(bg="#269CCB")
    elif not isPlaying[id]:
        doesLoop[id] = True
        loopButtonList[id].config(bg="#5E1D92")
def reset_button_color(id):
    pygame.time.wait(int(sounds[id].get_length() * 1000))
    if not pygame.mixer.Channel(id).get_busy():
        isPlaying[id] = False
        playStopButtonList[id].config(bg="#269CCB")
'''
=====================================================================================================================
defining tracker functions
'''
def partyLU():
    # Create new window
    window2 = tk.Toplevel(window)
    window2.title("Select Party")

    # Create frame
    window2Frame = tk.Frame(master=window2)
    window2Frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=8, pady=8)

    # Create label
    label = tk.Label(master=window2Frame, text="Select a Party", width=len("Select a Party"), height=1, font=nameFont)
    label.grid(row=0, column=0, padx=2, pady=2)

    # Create Drop-Down
    options = []
    fileLoc = os.path.join('data', 'partyList.txt')
    with open(fileLoc, "r") as partyFile:
        for line in partyFile:
            words = processLine(line)
            options.append(words[0])
    selectedVar = tk.StringVar(window2Frame)
    selectedVar.set("Click Here")
    partyMenu = tk.OptionMenu(window2Frame, selectedVar, *options)
    partyMenu.grid(row=1, column=0, padx=2, pady=2)

    # Create Buttons
    btnFrame = tk.Frame(master=window2Frame)
    btnFrame.grid(row=2, column=0)
    lButton = tk.Button(master=btnFrame, text="Load", width=10, height=2, command=lambda: get_selected_value(selectedVar, window2))
    lButton.grid(row=0, column=0)
    cButton = tk.Button(master=btnFrame, text="Cancel", width=10, height=2, command=window2.destroy)
    cButton.grid(row=0, column=1)

def get_selected_value(var1, win):
    # check for invalid val
    check = var1.get()
    if check != "Click Here":
        # get val and close window2
        partyName = var1.get()
        win.destroy()
        # get the pc ids of the party
        memsToFind = []
        partyFileLoc = os.path.join('data', 'partyList.txt')
        with open(partyFileLoc, "r") as partyFile:
            for line in partyFile:
                words = processLine(line)
                if words[0] == partyName:
                    memsToFind = words[1:]
                    break
        pcListFileLoc = os.path.join('data', 'pcList.txt')
        # append the pc list of respective pcs
        with open(pcListFileLoc, "r") as pcListFile:
            for line in pcListFile:
                words = processLine(line)
                for id in memsToFind:
                    if id == words[0]:
                        pcList.append(Entity(words[0], words[1], words[2], words[3], words[4], words[5],
                                             0, words[6], False))
        # load in pc to gui
        for i in range(len(pcList)):
            # Create frame
            pcFrame = tk.Frame(master=trackerFrame, relief=tk.RAISED, borderwidth=2)
            pcFrame.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

            # Create sub-frames
            nameInfoFrame = tk.Frame(master=pcFrame)
            nameInfoFrame.pack(side=tk.LEFT)
            infoFrame = tk.Frame(master=nameInfoFrame)
            infoFrame.grid(row=1, column=0, sticky="nw")
            initFrame = tk.Frame(master=pcFrame)
            initFrame.pack(side=tk.RIGHT)
            condFrame = tk.Frame(master=pcFrame)
            condFrame.pack(side=tk.RIGHT)
            hpFrame = tk.Frame(master=pcFrame)
            hpFrame.pack(side=tk.RIGHT, padx=5)

            # Create Widgets for frames
            ## name label
            nameLbl = tk.Label(master=nameInfoFrame, text=pcList[i].name, width=len(pcList[i].name), height=1, font=nameFont)
            nameLbl.grid(row=0, column=0, padx=0, pady=0, sticky="nw")
            ## hp label
            hpLbl = tk.Label(master=infoFrame, text="", height=1)
            if int(pcList[i].hp_Temp) > 0:
                hpLbl.config(text="     HP: " + str(pcList[i].hp_Current) + "(" + str(pcList[i].hp_Temp) + ")/" + str(pcList[i].hp_Max))
            else:
                hpLbl.config(text="     HP: " + str(pcList[i].hp_Current) + "/" + str(pcList[i].hp_Max))
            hpLbl.pack(side=tk.LEFT, padx=1, pady=1)
            ## ac label
            acLbl = tk.Label(master=infoFrame, text="AC: " + str(pcList[i].ac), width=len("AC: " + str(pcList[i].ac)), height=1)
            acLbl.pack(side=tk.LEFT, padx=1, pady=1)
            ## condition label
            condLbl = tk.Label(master=condFrame, text="Condition(s):", width=len("Condition(s):"), height=1)
            condLbl.pack(side=tk.TOP, anchor="nw", padx=0, pady=0)
            ## condition text
            condText = tk.Text(master=condFrame, wrap="word", width=20, height=2)
            condText.pack(side=tk.TOP, padx=3, pady=3)
            condText.insert(tk.END, pcList[i].conditions)
            ## initiative label
            initLbl = tk.Label(master=initFrame, text="Initiative", width=len("Initiative"), height=1)
            initLbl.pack(side=tk.TOP)
            ## initiative entry
            initEntry = tk.Entry(master=initFrame, width=3)
            initEntry.pack(side=tk.TOP)
            ## temp hp button
            tempBtn = tk.Button(master=hpFrame, text="Tp", width=2, height=1, command=lambda v=i: playStop(v))
            tempBtn.grid(row=0, column=0, padx=1, pady=1)
            ## heal hp button
            healBtn = tk.Button(master=hpFrame, text="+", width=2, height=1, command=lambda v=i: playStop(v))
            healBtn.grid(row=0, column=1, padx=1, pady=1)
            ## max hp button
            maxBtn = tk.Button(master=hpFrame, text="Mx", width=2, height=1, command=lambda v=i: playStop(v))
            maxBtn.grid(row=0, column=2, padx=1, pady=1)
            ## hp entry
            hpEntry = tk.Entry(master=hpFrame, width=4)
            hpEntry.grid(row=1, column=1, padx=1, pady=1)
            ## damage hp button
            dmgBtn = tk.Button(master=hpFrame, text="-", width=2, height=1, command=lambda v=i: playStop(v))
            dmgBtn.grid(row=2, column=1, padx=1, pady=1)
            ## max hp down button
            maxDBtn = tk.Button(master=hpFrame, text="Mx", width=2, height=1, command=lambda v=i: playStop(v))
            maxDBtn.grid(row=2, column=2, padx=1, pady=1)




def processLine(line):
    line = line.strip()
    line = line.replace(" ", "_")
    line = line.replace("~", " ")
    words = line.split()
    words = [s.replace("_", " ") for s in words]
    return words
'''
=====================================================================================================================
Sound Board Portion
'''

# Data setup
dataFileLoc = os.path.join('data', 'sounds.txt')
soundNameList = []
soundLocList = []
playStopButtonList = []
loopButtonList = []

# grab the names of the different sound files in sounds.txt and their locations
with open(dataFileLoc, "r") as file:
    for soundFileName in file:
        soundFileName = soundFileName.strip()
        soundNameList.append(soundFileName)
        soundLocList.append(os.path.join('sounds', soundFileName))

# populates sounds array and isPlaying array
sounds = [pygame.mixer.Sound(file_path) for file_path in soundLocList]
pygame.mixer.set_num_channels(len(sounds))
isPlaying = [False] * len(sounds)
doesLoop = [False] * len(sounds)

# Create Sound Board Frame
soundBoardFrame = tk.Frame(relief=tk.SUNKEN, borderwidth=2, bg="#303030")
soundBoardFrame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=3, pady=3)

# Crate Sound Board Item
for i in range(len(sounds)):
    # Create frame
    frame = tk.Frame(master=soundBoardFrame, relief=tk.RAISED, borderwidth=2, bg="#202020")
    frame.grid(row=i-int(i/6)*6, column=int(i/6), padx=3, pady=3)

    # Create PlayPause Button
    playStopButtonList.append(tk.Button(master=frame, text=soundNameList[i], width=20, height=3,
                                        bg="#269CCB", fg="white", command=lambda v=i: playStop(v)))
    playStopButtonList[i].pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=3, pady=3)

    # Create Volume Scale
    scale = tk.Scale(master=frame, from_=100, to=0, orient=tk.HORIZONTAL, command=lambda v, id=i: volumeChange(id, v))
    scale.set(100)
    scale.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=3, pady=3)

    # Create Loop Button
    loopButtonList.append(tk.Button(master=frame, text="Loop", width=5, height=3,
                                    bg="#269CCB", fg="white", command=lambda v=i: toggleLoop(v)))
    loopButtonList[i].pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=3, pady=3)
'''
======================================================================================================================
Tracker Portion
'''
# Important variables
pcList = []

# fonts
nameFont = font.Font(size=14, underline=True)

# Create Tracker Frame
trackerFrame = tk.Frame(relief=tk.SUNKEN, borderwidth=2, bg="#909090")
trackerFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=2, pady=2)

# Create button frame
trackerButtonFrame = tk.Frame(master=trackerFrame, relief=tk.RAISED, borderwidth=2, bg="#959595")
trackerButtonFrame.pack(side=tk.TOP, padx=2, pady=2)

# Load/Unload Party Button
partyLoaded = False
partyName = ""
partyLU_Button = tk.Button(master=trackerButtonFrame, text="Load Party", width=15, height=2,
                           bg="#269CCB", fg="white", command=partyLU)
partyLU_Button.pack(side=tk.LEFT, padx=2, pady=2)

# Button Loop
window.mainloop()
pygame.quit()
