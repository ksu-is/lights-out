'''
Constants, common functions, and other shared material
'''

class EntityTypes:
    def __init__(self):

        self.Player = 0
        self.Wall = 1
        self.Enemy = 2
        self.Example = 3

EntityTypeList = EntityTypes()

class StateList:
    BEGIN = -1
    NORMAL = 0
    PAUSED = 1
    MENU = 2

states = StateList()