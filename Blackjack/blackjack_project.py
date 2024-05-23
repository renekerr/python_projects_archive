import random
import os
from art import logo

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_cards():
    """
    Generates and returns a random card from a list of cards.
    
    Returns:
        int: A randomly selected card from the list.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Calculates the sum of all cards in the provided list.
    
    Parameters:
        cards (list): A list containing integer values representing cards.
        
    Returns:
        int: The total sum of all cards.
    """
    score = sum(cards)

    if score == 21 and len(cards) == 2:    # Check for blackjack
        return 0 
    
    if 11 in cards and score > 21: # Check if score exceeds 21 and an 11 is present    
        cards.remove(11)    # Replace 11 with 1
        cards.append(1)

    return score

def compare(player_score, computer_score):
    """
    Compares the scores of the player and the computer and determines the outcome of the game.
    
    Parameters:
        player_score (int): The score of the player.
        computer_score (int): The score of the computer.
        
    Returns:
        str: A string indicating the result of the game.
    """

    if player_score == computer_score:
        return "Result:\n\t No winner. It's a draw.\n"
    elif computer_score == 0:
        return "Result:\n\t Computer's blackjack!. Computer wins.\n"
    elif player_score == 0:
        return "Result:\n\t Blackjack! You win.\n"
    elif player_score > 21:
        return "Result:\n\t You went over, computer wins.\n"
    elif computer_score > 21:
        return "Result:\n\t Computer went over, you win.\n"
    elif computer_score > player_score:
        return "Result:\n\t Computer wins.\n"
    else:
        return "Result:\n\t You win!\n"

def play_game():
    """
    Simulates a card game between the player and the computer.
    """
    
    print(logo)

    player_cards, computer_cards = [], []
    for _ in range(2):  # Dealing first two cards
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    game_over = False
    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print('\n      \tcards\t\tscoring')
        print(f"player\t{player_cards}\t\t{player_score}")
        print(f"pc\t{computer_cards[0]}\n")


        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                player_cards.append(deal_cards())
            else: 
                game_over = True
                
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand is {player_cards}, your final score is {player_score}")
    print(f"Computer's final hand is {computer_cards}, its final score is {computer_score}\n")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear_screen()
    play_game()






