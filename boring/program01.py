import datetime
import os
os.system('cls' if os.name == 'nt' else 'clear')  
yourName = input(" please enter your name ");
os.system('cls' if os.name == 'nt' else 'clear')  
yourBirthYear = input(" please enter your birth year ")
currentTime = datetime.datetime.now()
currentYear =  currentTime.year
yearDifference = currentYear - int(yourBirthYear)
os.system('cls' if os.name == 'nt' else 'clear')    
print("your name is {0} , you are {1} year old".format(yourName,yearDifference))

