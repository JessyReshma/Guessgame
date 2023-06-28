"""print("Guess the number between 1 & 100")
answer = 50
chances = 0
while chances < 5:
    chances +=1
    guess = int(input("Guess the number here: "))
    if answer == guess:
        print("you have guessed the correct number")
        break
    elif answer != guess:
        print("you have guessed it wrong!")
        print(f"you have {5-chances} left")
    else: 
        print("you lost")"""
from random import randint
"""answer = randint(0,100)
print(answer)
chances = 0
import math as maths
highestrange = randint(50,100)
print(highestrange)
lowestrange = randint(0,50 )
print(lowestrange)
desiredrange= highestrange - lowestrange
desiredrange
noofchances = round(maths.log(desiredrange))
noofchances"""

import math
startingpoint, endingpoint= map(int,input("Choose a starting point and ending point: ").split(" "))
answer = randint(startingpoint,endingpoint)
tries = 0
chances = round(math.log(endingpoint - startingpoint+1,2))
print(f" You  have {chances} chances")
while tries < chances: 
    tries += 1
    guess = int(input(f"Guess a number between {startingpoint} & {endingpoint}: "))
    
    if guess == answer:
        print("You are correct!")
        break
    elif guess > answer: 
        print("your guess is wrong. Pick a smaller number")
    elif guess < answer:
        print("your guess is wrong. Pick a bigger number")
    print(f"You have {chances - tries} tries left")
if tries >= chances: 
    print("The correct answer is {ans}".format(ans=answer))