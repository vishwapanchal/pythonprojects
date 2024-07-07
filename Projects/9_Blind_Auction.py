import os

# Function to clear the console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Logo ASCII art
logo = '''
                           ___________
                           \         /
                            )_______(
                            |"""""""|_.-._,.---------.,_.-._
                            |       | | |               | | ''-.
                            |       |_| |_             _| |_..-'
                            |_______| '-' `'---------'` '-'
                            )"""""""(
                           /_________\\
                         .-------------.
                        /_______________\\
'''
print(logo)

# List to store bidders and their bids
bidders_list = []

auction_status = True

while auction_status:
    bidder_name = input("Enter your name: ")
    bid_value = int(input("Enter your bid value: ₹"))

    # Append bidder and bid to bidders_list
    bidders_list.append({
        'name': bidder_name,
        'bid': bid_value
    })

    next_person = input("Are there any other bidders? (y/n): ").lower()
    if next_person == "n":
        # Find the winner
        winner = max(bidders_list, key=lambda x: x['bid'])
        print(f"The winner is {winner['name']} with a bid of ₹{winner['bid']}.")

        auction_status = False
    elif next_person == 'y':
        clear()
