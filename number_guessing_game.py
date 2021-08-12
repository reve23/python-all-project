import random

print("This is a number guessing game. Here you would be given a range of number and you have to guess the correct number")
ask_range = random.randint(0,1000)
starts_with = random.randint(0,100)
number = random.randint(starts_with,ask_range)
print("")
print(f"The number is between {starts_with} to {ask_range}")
answer = int(input("Enter number: "))

guess = 0
while guess < 3:
    
    if answer == number:
        print(f"You guessed it! The number was {number}")
        break
    else:
        if answer < number:
            print("Too high")
            guess += 1
        elif answer > number:
            print("Too low")
            guess += 1
       
