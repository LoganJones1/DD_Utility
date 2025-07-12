# class Entity

class Entity:
    key: int
    hp_Max: int
    hp_Current: int
    hp_Temp: int
    ac: int
    initiative: int
    isMonster: bool

    def __init__(self, key, name, hp_Current, hp_Max, hp_Temp, ac,
                 initiative, conditions, isMonster):
        self.key = key
        self.name = name
        self.hp_Current = hp_Current
        self.hp_Max = hp_Max
        self.hp_Temp = hp_Temp
        self.ac = ac
        self.initiative = initiative
        self.conditions = conditions
        self.isMonster = isMonster

    def heal(self, amount):
        self.hp_Current += amount
        if self.hp_Current > self.hp_Max:
            self.hp_Current = self.hp_Max

    def damage(self, amount):
        self.hp_Temp -= amount
        if self.hp_Temp < 0:
            self.hp_Current += self.hp_Temp
            self.hp_Temp = 0
            if self.hp_Current < 0:
                self.hp_Current = 0

    def addTemp(self, amount):
        self.hp_Temp = amount
