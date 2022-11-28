from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

rand_number = random.randint(1, 100)
print(f"Pssst, the correct answer is {rand_number}")

def game(count):
    is_any_attemp_left = True
    print(f"You have {count} attempts remaining to guess the number.")
    while is_any_attemp_left:
        guess_number = int(input("Make a guess: "))
        if guess_number == rand_number:
            print(f"You got it! The answer was {rand_number}.")
            is_any_attemp_left = False
        elif guess_number > rand_number:
            print("Too high.")
        elif guess_number < rand_number:
            print("Too low.")            
        
        if count == 1:
            print("You've run out of guesses, you lose.")
            is_any_attemp_left = False
            break
        
        count -= 1
        print("Guess again.")
        print(f"You have {count} attempts remaining to guess the number.")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    count = 10
    game(10)
elif difficulty == "hard":
    count = 5
    game(5)