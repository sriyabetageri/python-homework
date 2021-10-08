import random

number = random.randint(1,9)

chances = 0
print("Guess a number between 1 and 9")

while chances<5:
    guess = int(input("enter your guess: "))

    if guess== number: 
        print("You did it!")
        break
    elif guess<number:
        print("try a higher number")
    else:
        print("guess a lower number")

    chances += 1
if not chances<5:
    print("your all out of chances, you lose!")

