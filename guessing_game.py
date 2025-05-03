import random

while True: 
number = random.randint(1,75) #Bigger range(75)

print("Guess a number between 1 and 75")

guess = int(input())

if guess < number: 
    print("Too low!") 
elif guess > number: 
    print("Too high!") 

if guess == number:
    print ("Victory ")  #changed You Win! to Victory

else:
    print("Wrong!The number was{number}")
    
    print("Play again? (y/n)") 
    if input().lower() != 'y': 
        break 