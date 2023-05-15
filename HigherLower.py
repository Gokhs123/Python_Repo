from HigherLower_data import data
import random
from HigherLower_art import logo, vs
import os
clear = lambda : os.system('cls')

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers :
        return guess == "a"
    else :
        return guess == "b"
    
def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue :
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_account = account_a["follower_count"]
        b_follower_account = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_account, b_follower_account)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You are right ! Current score is {score}")
        else:
            game_should_continue = False
            print("Sorry, thats wrong, Final score: {score}")

game()