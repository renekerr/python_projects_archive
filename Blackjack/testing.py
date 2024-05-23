import random
from mod_clear_screen import clear_screen
from art import logo

def deal_cards():
    """
    Return a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Return the sum of all cards in a list of cards passed as a parameter
    Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    Check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(player_score, computer_score):
    """
    Compares user and computer scores and decide who wins.
    This function accepts two parameters (player_score and computer_score)
    """
    """
    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    """
    if player_score == computer_score:
        return "Result:\n\t No winner. It's a draw.\n"
    elif computer_score == 0:
        return "Result:\n\t Computer's blackjack!. Computer wins!\n"
    elif player_score == 0:
        return "Result:\n\t Blackjack! You win!\n"
    elif player_score > 21:
        return "Result:\n\t You went over, computer wins!\n"
    elif computer_score > 21:
        return "Result:\n\t Computer went over, you win\n"
    elif computer_score > player_score:
        return "Result:\n\t Computer wins!\n"
    else:
        return "Result:\n\t You win!\n"

def play_game():
    player_cards, computer_cards = [],[]
    game_over = False

    print(logo)

    # First two cards
    for _ in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print('\n      \tcards\t\tscoring')
        print(f"player\t{player_cards}\t\t{player_score}")
        print(f"pc\t{computer_cards[0]}\n")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            getcard_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if getcard_or_pass == 'y':
                player_cards.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    
    print(f"\nYour final hand is {player_cards}, your final score is {player_score}")
    print(f"Computer's final hand is {computer_cards}, its final score is {computer_score}\n")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear_screen()
    play_game()





        









    





