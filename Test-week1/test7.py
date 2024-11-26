import random

print("***Welcome to the Number Gussing Game!***")
print("I'm thinking of a number between 1 and 100. Can you guss it?")

target_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulation! Yo guessed the number in {attempts} attempts.")  
        break