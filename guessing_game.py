import random

number = random.randint(1,100) #Bigger range

print("Guess a number between 1 and 100")

guess = int(input())


if guess == number:
    print ("You win!")

else:
    print("Wrong!The number was{number}")