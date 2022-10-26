'''
Name: Dana Garadah
email: garadada@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Group Assignment
Citations:
Anything else that's relevant:
'''
class Hero():
    def setHeroName(self, name):
        self.validateHeroName(name)
    def validateHeroName(self, name):
        if name == '':
            print ("Enter hero name")
        else:
            self.name = name
    def getHeroName(self):
        return self.name
    def setGender(self, gender):
        self.validateGender(gender)
    def validateGender(self, gender):
        if gender == '':
            print ("Enter hero's suspected gender")
        else:
            self.gender = gender
    def HeroStatus(self, status):
        self.validateHeroStatus(status)
    def validateHeroStatus(self, status):
        if status == '':
            print ("Enter hero status")
        else:
            self.status = status
    def setUniverse(self, universe):
        self.validateUniverse(universe)
    def validateUniverse(self, universe):
        if universe == '':
            print("Hero must be a member of a universe")
        else:
            self.universe = universe
    def __init__(self, name, gender, status, universe):
        self.name = name
        self.validateHeroName(name)
        self.gender = gender
        self.validateGender(gender)
        self.setHeroStatus = status
        self.validateHeroStatus(status)
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
        return "name = " + self.name + ", " + self.gender + ", " + self.status + ", " + self.universe 
    
    