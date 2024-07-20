import random
from random_word import RandomWords
from art import text2art

# Generate ASCII art for the word "hangman"
ascii_art = text2art("hangman")

# Print the ASCII art
print(ascii_art)

stages = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

end_of_game = False
word_list = [RandomWords().get_random_word() for _ in range(10)]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = ["_" for _ in range(word_length)]

while not end_of_game:
    guess = input("Guess a char: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
        continue

    for position in range(word_length):
        char = chosen_word[position]
        if char == guess:
            display[position] = char

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lost.")
            print(f"The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won.")

    print(stages[lives])
