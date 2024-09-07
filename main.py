from art import logo
import random as rd

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack_game():


    your_cards = []
    current_score = 0
    computers_cards = [rd.choice(cards)]
    computer_score = 0

    while len(your_cards) < 2:
        card = rd.choice(cards)
        if card != 11:
            your_cards.append(card)
        elif card == 11 and (your_cards.count(11) == 0):
            your_cards.append(card)

    rd.shuffle(your_cards)
    current_score = sum(your_cards)

    while sum(computers_cards) < 16:
        card = rd.choice(cards)
        computers_cards.append(card)

    rd.shuffle(computers_cards)
    computer_score = sum(computers_cards)


    option = input("Hey There! Do you want to play some Blackjack game's? Type 'yes' or 'no':  ")
    if option.lower() == "no":
        print("Goodbye, see you soon.")
        exit()

    elif option.lower() == "yes":

        print("\n"*20)
        print(logo)

        print(f"""
            Your cards are: {your_cards}        ---------       Computer's first card: {computers_cards[0]}      
            Current score:  {current_score}
        """)

        if current_score == 21:
            print("BlackJazz 🤩🤩🤩. You Win!")


        match_over = True
        while match_over:
            choice = input("Type 'y' to ge another card, type 'n' to pass:  ")
            if choice.lower() == 'n':
                match_over = False
                print(f"""
                    Your final hand is: {your_cards}        ---------       Computer's final hand: {computers_cards}      
                    Your final score is:  {current_score}        ---------       Computer's final score: {computer_score}
                    """)
                if current_score > computer_score:
                    print("You Win 🥳🥳🥳")
                elif current_score < computer_score:
                    if computer_score <= 21:
                        print("You Lose 😵‍💫😵‍💫😵‍💫")
                    else:
                        print("You Win 🥳🥳🥳")
                else:
                    print("Draw Game 😐😐😐")

            elif choice.lower() == 'y':
                new_card = rd.choice(cards)
                your_cards.append(new_card)

                current_score = sum(your_cards)

                if current_score == 21:
                    print(f"""
                        Your final hand is: {your_cards}        ---------       Computer's final hand: {[computers_cards[0]]}      
                        Your final score is:  {current_score}        ---------       Computer's final score: {computers_cards[0]}
                        """)
                    print()
                    print("You Win 🥳🥳🥳")
                    match_over = False

                elif current_score > 21:
                    print(f"""
                        Your final hand is: {your_cards}        ---------       Computer's final hand: {[computers_cards[0]]}      
                        Your final score is:  {current_score}        ---------       Computer's final score: {computers_cards[0]}
                        """)
                    print()
                    print("You went over. You lose 😭😭😭")
                    match_over = False
                else:
                    print(f"""
                        Your cards are: {your_cards}        ---------       Computer's first card: {computers_cards[0]}      
                        Current score:  {current_score}
                    """)
    blackjack_game()

blackjack_game()