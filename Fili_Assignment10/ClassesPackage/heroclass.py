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
    def setGender(self, gender):
        self.validateGender(gender)
    def validateGender(self, gender):
        if gender == '':
            print ("Enter hero gender")
        else:
            self.gender = gender
    def setStatus(self, status):
        self.validateStatus(status)
    def validateStatus(self, status):
        if status == '':
            print ("Enter if deceased or alive")
        else:
            self.status = status
    def __init__(self, name, gender, status):
        self.name = name  
        self.validateName
    def __repr__(self):
        '''
        return a string representation of the object.
        '''
        return "brand = " + self.brand
    def __str__(self):
        '''
        return a 'pretty' string representation of the object
        '''
        return "brand = " + self.brand + ", " + str(self.size)