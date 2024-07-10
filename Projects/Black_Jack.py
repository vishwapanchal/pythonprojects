import random
import os

# Clear the console screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Print the Blackjack logo
def print_logo():
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(logo)

# Deal a card from the deck
def card_deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Calculate the score of a given hand of cards
def calculate_score(cards):
    # Check for a blackjack (two cards summing to 21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Adjust for Ace if the total is greater than 21
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Compare user and computer scores and determine the result
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer wins with Blackjack! 😓"
    elif user_score == 0:
        return "User wins with Blackjack! 🤩"
    elif user_score > 21:
        return "You went over, you lost 😟"
    elif computer_score > 21:
        return "Opponent went over, you win 😃"
    elif user_score > computer_score:
        return "User wins 😁"
    else:
        return "You lose"

# Main game function
def play_game():
    print_logo()

    computer_cards = []
    user_cards = []
    is_game_over = False

    # Initial dealing of two cards to both user and computer
    for _ in range(2):
        computer_cards.append(card_deal())
        user_cards.append(card_deal())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(card_deal())
            else:
                is_game_over = True
                
    # Computer's turn to draw cards until the score reaches at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(card_deal())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main loop to keep playing the game
while input("\nDo you want to play the Blackjack game: type 'y' or 'n' : ") == "y":
    clear()
    play_game()
