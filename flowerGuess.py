import random

def hydrangea():
    hydrangea_list = "Hydrangea"
    print("Guess the 9 characters: _ _ _ _ _ _ _ _ _")
    attempt = len(hydrangea_list)
    print(f"You have {attempt} more attempt(s).")
    guessed = ""

    fail = 0
    while fail < attempt:
        user_input = input("\nEnter a character: ")

        if user_input in hydrangea_list:
            print(f"Great guess! {user_input} is in the word.\n")
            guessed += user_input
        else:
            fail += 1
            print(f"There is no such character in the word. "
                  f"You have {attempt-fail} attempt(s) left.\n")
        completed = len(hydrangea_list)
        
        #print the current letter
        for letter in hydrangea_list:
            if letter in guessed:
                print(f"{letter} ", end="")
                completed -= 1
            else:
                print(f"_ ", end="")

        if completed == 0:
            print(f"Congrats, you won! The secret word is {hydrangea_list}.")
            break
    else:
        print("\nYou have run out of the attempts. Better luck next time!")


def orchid():
    orchid_list = "Orchid"
    print("Guess the 6 characters: _ _ _ _ _ _")
    attempt = len(orchid_list)
    print(f"You have {attempt} attempt(s).")
    guessed = ""

    fail = 0
    while fail < attempt:
        user_input = input("\nEnter a character: ")

        if user_input in orchid_list:
            print(f"Great guess! {user_input} is in the word.\n")
            guessed += user_input
        else:
            fail += 1
            print(f"There is no such character in the word. "
                  f"You have {attempt-fail} attempt(s) left.\n")
        completed = len(orchid_list)
        
        #print the current letter
        for letter in orchid_list:
            if letter in guessed:
                print(f"{letter} ", end="")
                completed -= 1
            else:
                print(f"_ ", end="")
        print()
        if completed == 0:
            print(f"Congrats, you won! The secret word is {orchid_list}.")
            break
    else:
        print("You have run out of the attempts. Better luck next time!")


def marigold():
    marigold_list = "Marigold"
    print("Guess the 8 characters: _ _ _ _ _ _ _ _")
    attempt = len(marigold_list)
    print(f"You have {attempt} more attempt(s).")
    guessed = ""

    fail = 0
    while fail < attempt:
        user_input = input("\nEnter a character: ")

        if user_input in marigold_list:
            print(f"Great guess! {user_input} is in the word.\n")
            guessed += user_input
        else:
            fail += 1
            print(f"There is no such character in the word. "
                  f"You have {attempt-fail} attempt(s) left.\n")
        completed = len(marigold_list)
        
        #print the current letter
        for letter in marigold_list:
            if letter in guessed:
                print(f"{letter} ", end="")
                completed -= 1
            else:
                print(f"_ ", end="")

        if completed == 0:
            print(f"\nCongrats, you won! The secret word is {marigold_list}.")
            break
    else:
        print("\nYou have run out of the attempts. Better luck next time!")

def calendula():
    calendula_list = "Calendula"
    print("Guess the 9 characters: _ _ _ _ _ _ _ _ _")
    attempt = len(calendula_list)
    print(f"You have {attempt} more attempt(s).")
    guessed = ""

    fail = 0
    while fail < attempt:
        user_input = input("\nEnter a character: ")

        if user_input in calendula_list:
            print(f"Great guess! {user_input} is in the word.\n")
            guessed += user_input
        else:
            fail += 1
            print(f"There is no such character in the word. "
                  f"You have {attempt-fail} attempt(s) left.\n")
        completed = len(calendula_list)
        
        #print the current letter
        for letter in calendula_list:
            if letter in guessed:
                print(f"{letter} ", end="")
                completed -= 1
            else:
                print(f"_ ", end="")

        if completed == 0:
            print(f"Congrats, you won! The secret word is {calendula_list}.")
            break
    else:
        print("\nYou have run out of the attempts. Better luck next time!")


def jasmine():
    jasmine_list = "Jasmine"
    print("Guess the 7 characters: _ _ _ _ _ _ _")
    attempt = len(jasmine_list)
    print(f"You have {attempt} more attempt(s).")
    guessed = ""

    fail = 0
    while fail < attempt:
        user_input = input("\nEnter a character: ")

        if user_input in jasmine_list:
            print(f"Great guess! {user_input} is in the word.\n")
            guessed += user_input
        else:
            fail += 1
            print(f"There is no such character in the word. "
                  f"You have {attempt-fail} attempt(s) left.\n")
        completed = len(jasmine_list)
        
        #print the current letter
        for letter in jasmine_list:
            if letter in guessed:
                print(f"{letter} ", end="")
                completed -= 1
            else:
                print(f"_ ", end="")

        if completed == 0:
            print(f"Congrats, you won! The secret word is {jasmine_list}.")
            break
    else:
        print("\nYou have run out of the attempts. Better luck next time!")


def dandelion():
    dandelion_list = "Dandelion"
    print("Guess the 9 characters: _ _ _ _ _ _ _ _ _")
    attempt = len(dandelion_list)
    print(f"You have {attempt} more attempt(s).")
    guessed = ""

    fail = 0
    while fail < attempt:
        user_input = input("\nEnter a character: ")

        if user_input in dandelion_list:
            print(f"Great guess! {user_input} is in the word.\n")
            guessed += user_input
        else:
            fail += 1
            print(f"There is no such character in the word. "
                  f"You have {attempt-fail} attempt(s) left.\n")
        completed = len(dandelion_list)
        
        #print the current letter
        for letter in dandelion_list:
            if letter in guessed:
                print(f"{letter} ", end="")
                completed -= 1
            else:
                print(f"_ ", end="")

        if completed == 0:
            print(f"Congrats, you won! The secret word is {dandelion_list}.")
            break;
    else:
        print("\nYou have run out of the attempts. Better luck next time!")


# Main program
play_again = True
while play_again:
    print("Theme: Flower.")
    rand_num = random.randint(1,6)
    if rand_num == 1:
        hydrangea()
    elif rand_num == 2:
        orchid()
    elif rand_num == 3:
        marigold()
    elif rand_num == 4:
        calendula()
    elif rand_num == 5:
        jasmine()
    else:
        dandelion()

    user_input = input("Do you want to play again? (y/n): ").lower()
    if user_input == "n":
        print("Goodbye!")
        play_again = False
