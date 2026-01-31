class Hospital:
    def __init__(self, preferences, ID):
        self.preferences = preferences
        self.ID = ID
        self.matched = False
        self.nextProposalIndex = 0

    def matchTo(self, student):
        self.currentMatch = student
        self.matched = True

    def unmatch(self):
        self.currentMatch = None
        self.matched = False

    def get_match(self):
        return self.currentMatch
    
class Student:
    def __init__(self, preferences, ID):
        self.preferences = preferences
        self.ID = ID
        self.matched = False
    
    def matchTo(self, hospital):
        self.currentMatch = hospital
        self.matched = True

    def unmatch(self):
        self.currentMatch = None
        self.matched = False

    def get_match(self):
        return self.currentMatch