class Hospital:
    def __init__(self, preferences, ID):
        self.preferences = preferences
        self.ID = ID
    
class Student:
    def __init__(self, preferences):
        self.preferences = preferences
        self.matched = False
    
    def matchTo(self, hospital):
        self.currentMatch = hospital
        self.matched = True