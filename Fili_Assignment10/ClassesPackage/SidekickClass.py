#Sidekick Class
class SideKick():
    def setSideKickName(self, name):
        self.validateSideKickName
    def validateVillianName(self, name):
        if name == '':
            print("Enter sidekick name")
        else:
            self.name = name
    def setGender(self, gender):
        self.validateGender(gender)
    def validateGender(self, gender):
        if gender =='':
            print("Enter sidekick's suspected gender")
        else:
            self.gender = gender
    def setSideKickStatus(self, status):
        self.validateVillainStatus(status)
    def validateSideKickStatus(self, status):
        if status == '':
            print("Enter Sidekick status")
        else:
            self.status = status
    def setSideKickHero(self, hero):
        self.validateSideKickHero(hero)
    def validateSideKickHero(self, hero):
        if hero == '':
            print("Enter sidekick's hero")
        else:
            self.hero = hero
    def setUniverse(self, universe):
        self.validateUniverse(universe)
    def validateUniverse(self, universe):
        if universe == '':
            print("Sidekick must be a member of a universe")
        else: 
            self.universe = universe
            
    def __init__(self, name, gender, status, hero, universe):
        self.name = name
        self.validateSideKickName(name)
        self.gender = gender
        self.validateGender(gender)
        self.setSideKickStatus = hero
        self.validateSideKickHero(hero)
        self.setUniverse = universe
        self.validateUniverse(universe)
    def __repr__(self):
        '''
        Return a string representation of the object
        '''
        return "name = " + self.name
    def __str__(self):
        '''
        return a 'pretty string representation of the object
        '''
        return "name: " + self.name + ", gender: " + self.gender + ", status: " + self.status + ", hero: " + self.hero + ", universe: " + self.universe 
        