#main.py
from ClassesPackage.VillainClass import *
from ClassesPackage.heroclass import *
from ClassesPackage.SidekickClass import *
#Villain testing
Villain1 = Villain('Lex Luthor','Male','Active','DC','Rich')
print(Villain1)
Villain1.setVillainPower('Super Strength')
print(Villain1.__str__())
print(Villain1.getVillainPower())

#Hero testing
Hero1 = Hero('Superman','Male','Active','DC')
print(Hero1.getHeroName())
Hero1.HeroStatus('Deceased')
print(Hero1.__str__())


#SideKick testing
SideKick1 = SideKick('Superboy','Male','Active','Superman','DC')
print(SideKick1)
SideKick1.setSideKickHero('None')
print(SideKick1.__repr__())
print(SideKick1.getSideKickHero())