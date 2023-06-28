from random import randint
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
