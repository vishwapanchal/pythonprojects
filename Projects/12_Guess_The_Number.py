import random
import os 

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def play_game():
    level = input("Select level: 'e' for Easy and 'h' for 'hard': ").lower()
    lives = 0
    if level == "e":
        lives += 10
    elif level == 'h':
        lives += 5
    else:
        print("Invalid Choice, try again!")
        return

    random_number = random.randint(0,101)

    while lives>0:
        guess = int(input("\nGuess the number: "))
        if guess == random_number:
            print("You guessed the right number!")
            return
        elif guess > random_number:
            print("\nGuess is high")
            lives -= 1
            print(f"lives remaining: {lives}")
        elif guess < random_number:
            print("\nGuess is low")
            lives -= 1
            print(f"lives remaining: {lives}")
        else:
            print("Invalid guess, try again!")

    if lives == 0:
        print("\nYou run out of lives, Game Over!")

while input("Do you want to play the Number Guessing Game? (y/n): ").lower()=='y':
    clear()
    play_game()
print("\nGood Bye!")