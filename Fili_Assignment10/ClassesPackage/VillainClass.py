#Villain Class
class Villian():
    def setVillianName(self, name):
        self.validateVillianName
    def validateVillianName(self, name):
        if name == '':
            print("Enter villian name")
        else:
            self.name = name
    def setGender(self, gender):
        self.validateGender(gender)
    def validateGender(self, gender):
        if gender =='':
            print("Enter hero's suspected gender")
        else:
            self.gender = gender
    def setVillainStatus(self, status):
        self.validateVillainStatus(status)
    def validateVillainStatus(self, status):
        if status == '':
            print("Enter villain status")
        else:
            self.status = status
    def setUniverse(self, universe):
        self.validateUniverse(universe)
    def validateUniverse(self, universe):
        if universe == '':
            print("Villain must be a member of a universe")
            
    def __init__(self, name, gender, status, universe):
        self.name = name
        self.validateVillianName(name)
        self.gender = gender
        self.validateGender(gender)
        self.setVillainStatus = status
        self.validateVillainStatus(status)
        self.setUniverse = universe
        self.validateUniverse(universe)
    def __repr__(self):
        '''
        Return a string representation of the object
        '''
        return "name = " + self.name
    def __str__(self):
        '''
        return a 'pretty string representaion of the object
        '''
        return "name = " + self.name + ", " + self.gender + ", " + self.status + ", " + self.universe 
        