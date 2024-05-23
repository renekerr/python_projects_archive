# Import the random library.

# Create a variable to accumulate the score, which should be set to 0 initially.

# Create empty lists for A and B

# Get items (for A and B) from the data (list) using the choice() function from the random library. A and B have to
# be different.

# Once both are chosen, print them using this pattern: name, description, and country.

# Ask user to guess who's got more followers

# Once compared, if comparison is correct, A should be removed from list.

# If the comparison is correct, increase the score by 1 and set B as A. Then, generate a new B randomly.

# If the comparison is not correct, the program should finish, and the final score should be printed.

# Use a while loop to continually compare A against B until the user gets it wrong.

from random import choice
from game_data import data
from art import logo
import os


def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def select_random_items():
    """
    Selects two random items from the data.
    
    Returns:
    tuple: Two randomly selected items.
    """
    item_a, item_b = {}, {}
    while item_a == item_b:
        item_a = choice(data)
        item_b = choice(data)
    return item_a, item_b


def compare_followers(followers_a, followers_b):
    """
    Compares the number of followers for two entities and returns who has more followers.
    
    Parameters:
    followers_a (int): The number of followers for entity A.
    followers_b (int): The number of followers for entity B.
    
    Returns:
    str: 'a' if entity A has more followers, 'b' if entity B has more followers,
         or 'equal' if both entities have the same number of followers.
    """
    if followers_a > followers_b:
        return 'a'
    elif followers_b > followers_a:
        return 'b'
    else:
        return 'equal'


def display_data(item_a, item_b, score):
    """
    Display information about the items and the score.

    Parameters:
    item_a (dict): The first item to compare.
    item_b (dict): The second item to compare.
    score (int): The current score of the player.
    """
    print(f'Correct answers: {score}')
    print(f'Current score: {score}\n')

    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}.")
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}.")


def play_game():
    """
    Main function to play the game.
    """
    score = 0
    item_a, item_b = select_random_items()
    game_over = False

    while not game_over:
        print(logo)

        display_data(item_a, item_b, score)

        higher_follower = compare_followers(item_a['follower_count'], item_b['follower_count'])
    
        user_guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        
        if user_guess == higher_follower:
            score += 1
            item_a = item_b
            item_b = choice(data)
            while item_a == item_b:
                item_b = choice(data)
            clear_screen()
            game_over = False
        else:
            clear_screen()
            print(f'Incorrect answer\nCorrect answers: {score}\nFinal score: {score}')
            game_over = True


play_game()
