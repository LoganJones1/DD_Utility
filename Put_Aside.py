# Data setup

pcFileLoc = os.path.join('data', 'pcList.txt')
pcList = []

# grab the data of the pcs
with open(pcFileLoc, "r") as file:
    for line in file:
        line = line.strip()
        line = line.replace(" ", "_")
        line = line.replace("~", " ")
        words = line.split()
        for i in range(len(words)):
            words[i] = words[i].replace("_", " ")
        pcList.append(Entity(int(words[0]), words[1], int(words[2]), int(words[3]), int(words[4]), int(words[5]),
                             0, words[6], False))



# Create Tracker Item
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
    hpLbl = tk.Label(master=infoFrame,
                     text="HP: " + str(pcList[i].hp_Current + pcList[i].hp_Temp) + "/" + str(pcList[i].hp_Max),
                     width=len("HP: " + str(int(pcList[i].hp_Current) + int(pcList[i].hp_Temp)) + "/" + str(pcList[i].hp_Max)),
                     height=1)
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