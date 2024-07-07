print("Welcome to the Forest Adventure!")
print("Your goal is to find the hidden treasure.")

# Step 1
print("\nYou are at the entrance of the mysterious forest.")
choice1 = input("Do you want to go left or right? (left/right): ").strip().lower()

if choice1 == "left":
    # Step 2
    print("\nYou followed the left path and reached a wide river.")
    choice2 = input("Do you want to build a raft to cross or walk along the riverbank to find a bridge? (raft/walk): ").strip().lower()

    if choice2 == "raft":
        # Step 3
        print("\nYou built a raft and crossed the river safely. You meet a stranger on the other side.")
        choice3 = input("Do you trust the stranger and follow them or ignore them and continue on your own? (trust/ignore): ").strip().lower()

        if choice3 == "trust":
            # Step 4
            print("\nThe stranger leads you to a cave. They claim the treasure is inside.")
            choice4 = input("Do you enter the cave immediately or circle around to look for traps? (enter/circle): ").strip().lower()

            if choice4 == "enter":
                print("\nCongratulations! You found the hidden treasure and won the game!")
            else:
                print("\nYou circled around the cave and fell into a hidden trap. Game over!")
        else:
            print("\nYou ignored the stranger and got lost in the forest. Game over!")
    else:
        print("\nYou walked along the riverbank but couldn't find a bridge. You got tired and had to return home. Game over!")
else:
    # Step 2
    print("\nYou followed the right path and reached a wide river.")
    choice2 = input("Do you want to build a raft to cross or walk along the riverbank to find a bridge? (raft/walk): ").strip().lower()

    if choice2 == "walk":
        # Step 3
        print("\nYou found a bridge and crossed the river safely. You meet a stranger on the other side.")
        choice3 = input("Do you trust the stranger and follow them or ignore them and continue on your own? (trust/ignore): ").strip().lower()

        if choice3 == "ignore":
            # Step 4
            print("\nYou continued on your own and found a cave. The treasure might be inside.")
            choice4 = input("Do you enter the cave immediately or circle around to look for traps? (enter/circle): ").strip().lower()

            if choice4 == "circle":
                print("\nCongratulations! You found the hidden treasure and won the game!")
            else:
                print("\nYou entered the cave immediately and fell into a hidden trap. Game over!")
        else:
            print("\nYou trusted the stranger, but they led you astray. Game over!")
    else:
        print("\nYou built a raft, but it broke halfway across the river. Game over!")
