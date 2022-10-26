#Villain Class
class Villain():
    def setVillainName(self, name):
        self.validateVillainName
    def validateVillainName(self, name):
        if name == '':
            print("Enter villain name")
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
        else:
            self.universe = universe
    def setVillainPower(self, power):
        self.validateVillainPower(power)
    def validateVillainPower(self, power):
        if power == '':
            print("Villain must have a power")
        else:
            self.power = power
            
    def __init__(self, name, gender, status, universe, power):
        self.validateVillainName(name)
        self.validateGender(gender)
        self.validateVillainStatus(status)
        self.validateUniverse(universe)
        self.validateVillainPower(power)
    def __repr__(self):
        '''
        Return a string representation of the object
        '''
        return "name = " + self.name
    def __str__(self):
        '''
        return a 'pretty string representation of the object
        '''
        return "name = " + self.name + ", " + "gender = " + self.gender + ", " + "status = " + self.status + ", " + "universe = " + self.universe + ", " + "power = " + self.power
        