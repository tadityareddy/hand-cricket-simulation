from cv_input import user_input
import random
import numpy as np
from sklearn.linear_model import LinearRegression
import csv
def toss_input():
    """Asks the user to choose odd or even and returns the choice."""
    choice = input("Odd or Even? ").lower()
    while choice not in ['odd', 'even']:
        choice = input("Please enter 'Odd' or 'Even': ").lower()
    return choice
def play_toss():
    """Simulates the toss and returns which player will bat first."""
    print("Welcome to Hand Cricket!")
    # Simulate the toss
    toss_choice = toss_input()
    toss_number = random.randint(1, 6)
    total = toss_number + user_input()
    print("Machine chose:", toss_number)
    # Determine which player will bat first
    if total % 2 == 0:
        print("Total is even.")
        if toss_choice == 'even':
            print("You won the toss!")
            choice = input("Bat or bowl? ").lower()
            while choice not in ['bat', 'bowl']:
                choice = input("Please enter 'Bat' or 'Bowl': ").lower()
            if choice == 'bat':
                return "player"
            else:
                return "machine"
        else:
            print("Machine won the toss.")
            choice = random.choice(['bat', 'bowl'])
            print("Machine chose to", choice)
            if choice == 'bat':
                return "machine"
            else:
                return "player"
    else:
        print("Total is odd.")
        if toss_choice == 'odd':
            print("You won the toss!")
            choice = input("Bat or bowl? ").lower()
            while choice not in ['bat', 'bowl']:
                choice = input("Please enter 'Bat' or 'Bowl': ").lower()
            if choice == 'bat':
                return "player"
            else:
                return "machine"
        else:
            print("Machine won the toss.")
            choice = random.choice(['bat', 'bowl'])
            print("Machine chose to", choice)
            if choice == 'bat':
                return "machine"
            else:
                return "player"
def get_machine_input(time_series):
    """Uses linear regression to predict the next run based on the previous runs."""
    # Create input and output arrays for the linear regression model
    n_steps = 5
    X = np.array([time_series[i:i+n_steps] for i in range(len(time_series)-n_steps)])
    y = np.array(time_series[n_steps:])
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    # Use the model to predict the next run and return the predicted value
    next_run = model.predict(np.array([time_series[-n_steps:]]))[0]
    return round(next_run)
def get_player_input():
    """Asks the player to input a number between 1 and 6 and returns the input."""
    while True:
        try:
            player_input = int(input("Enter a number between (1-6):"))
            if player_input < 1 or player_input > 6:
                print("Invalid input. Please enter a number between 1 and 6.")
            else:
                return player_input
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
def batting():
    # Initialize the time series list to keep track of runs
    runs_history = []
    for i in range(6):
        # Generate random runs for the first 6 balls
        runs_history.append(random.randint(1, 6))
    # Initialize the score to zero
    total_score = 0
    # Loop until the player is out
    while True:
        # Get input from the player and the machine
        player_runs = user_input()
        print("you bat "+str(player_runs))
        machine_runs = get_machine_input(runs_history)
        # Add the player's runs to the time series
        runs_history.append(player_runs)
        runs_history = runs_history[1:]
        # Print the machine's runs
        print("Machine bowls " + str(machine_runs))
        # If the player is out, end the inning
        if machine_runs == player_runs:
            print("OUT")
            break
        else:
            # Add the player's runs to the score
            total_score += player_runs
    return total_score
def bowling():
    # Initialize the time series list
    runs_series = []
    for i in range(6):
        runs_series.append(random.randint(1, 6))
    # Initialize the score to zero
    score = 0
    # Loop until the player gets all the batsmen out
    while True:
        # Get input from the player and the machine
        player_runs = user_input()
        print("you bowl "+str(player_runs))
        machine_runs = random.randint(1,6)
        machine_runs_excluding_player = get_machine_input(runs_series)
        while machine_runs_excluding_player == machine_runs:
            machine_runs = random.randint(1,6)
        # Add the player's runs to the time series
        runs_series.append(player_runs)
        runs_series = runs_series[1:]
        # Print the machine's runs
        print("Machine bats " + str(machine_runs))
        # If the machine is out, end the inning
        if machine_runs == player_runs:
            print("OUT")
            break
        else:
            # Add the machine's runs to the score
            score += machine_runs
    return score
def second_batting(opponent_score):
    """
    Plays the second inning of the match, where the player is chasing a target score set by the opponent.
    """
    # Initialize the time series list to keep track of the player's batting history
    player_runs_history = []
    for i in range(6):
        # Initialize the series with random values
        player_runs_history.append(random.randint(1, 6))
    # Initialize the score to zero
    player_score = 0
    # Loop until the player is out or beats the opponent's score
    while True:
        # Get input from the player and the machine
        player_runs = user_input()
        print("you bat "+str(player_runs))
        machine_runs = get_machine_input(player_runs_history)
        # Add the player's runs to the time series
        player_runs_history.append(player_runs)
        player_runs_history = player_runs_history[1:]
        # Print the machine's runs
        print("Machine bowls " + str(machine_runs))
        # If the player is out, end the inning
        if machine_runs == player_runs:
            print("OUT")
            break
        else:
            # Add the player's runs to the score
            player_score += player_runs
            # If the player's score beats the opponent's score, end the inning
            if player_score > opponent_score:
                break
    # Return the score achieved by the player in the inning
    return player_score
def second_bowling(opponent_score):
    # Initialize the time series list
    runs_history = []
    for i in range(6):
        runs_history.append(random.randint(1, 6))
    # Initialize the score to zero
    total_score = 0
    # Loop until the machine gets all the batsmen out or the player beats the opponent's score
    while True:
        # Get input from the player and the machine
        player_runs = user_input()
        print("you bowl "+str(player_runs))
        machine_runs_on_bat = random.randint(1,6)
        machine_runs_excluding_player = get_machine_input(runs_history)
        while machine_runs_excluding_player == machine_runs_on_bat:
            machine_runs_on_bat = random.randint(1,6)
        # Add the player's runs to the time series
        runs_history.append(player_runs)
        runs_history = runs_history[1:]
        # Print the machine's runs
        print("Machine bats " + str(machine_runs_on_bat))
        # If the machine is out, end the inning
        if machine_runs_on_bat == player_runs:
            print("OUT")
            break
        else:
            # Add the machine's runs to the total score
            total_score += machine_runs_on_bat
            # Check if the player has beaten the opponent's score and end the inning if true
            if total_score > opponent_score:
                print("You won!")
                break
    return total_score

def super_over_bowling():
    time_series = []
    for i in range(6):
        time_series.append(random.randint(1, 6))
    score = 0
    for _ in range(6):
        bowl = get_player_input()
        machine_bowl = random.randint(1, 6)
        machine_bowl_choice = get_machine_input(time_series)
        while machine_bowl_choice == machine_bowl:
            machine_bowl = random.randint(1, 6)
        time_series.append(bowl)
        time_series = time_series[1:]
        print("Machine bat " + str(machine_bowl))
        if machine_bowl == bowl:
            print("OUT")
            break
        else:
            score += machine_bowl
    return score

def super_over_batting():
    time_series = []
    for i in range(6):
        time_series.append(random.randint(1, 6))
    score = 0
    for _ in range(6):
        bat = get_player_input()
        machine_bowl_choice = get_machine_input(time_series)
        time_series.append(bat)
        time_series = time_series[1:]
        print("Machine bowl " + str(machine_bowl_choice))
        if machine_bowl_choice == bat:
            print("OUT")
            break
        else:
            score += bat
    return score

def super_over(play_toss):
    if play_toss == 1:
        user_score = super_over_batting()
        print("Your score in superover is " + str(user_score))
        machine_score = super_over_bowling()
        print("Machine score in superover is " + str(machine_score))
        if user_score == machine_score:
            print("It's a tie!")
        elif user_score < machine_score:
            print("You lost in superover.")
        else:
            print("You won in superover!")
    else:
        machine_score = super_over_bowling()
        print("Machine score in superover is " + str(machine_score))
        user_score = super_over_batting()
        print("Your score in superover is " + str(user_score))
        if user_score == machine_score:
            print("It's a tie!")
        elif user_score < machine_score:
            print("You lost in superover.")
        else:
            print("You won in superover!")

if __name__=="__main__":
    toss_result = play_toss()
    if toss_result == "player":
        your_score = batting()
        print("Your score is " + str(your_score))

        machine_score = second_bowling(your_score)
        print("Machine's score is " + str(machine_score))
    else:
        machine_score = bowling()
        print("Machine's score is " + str(machine_score))

        your_score = second_batting(machine_score)
        print("Your score is " + str(your_score))

    with open('C:/Users/ACER/PycharmProjects/handcricket/batsmans_career.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        # write a row of data to the CSV file
        writer.writerow([your_score])
    with open('C:/Users/ACER/PycharmProjects/handcricket/machines_career.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        # write a row of data to the CSV file
        writer.writerow([machine_score])


    if your_score > machine_score:
        print("You won by " + str(your_score - machine_score) + " runs!")
    elif your_score == machine_score:
        print("It's a tie! Let's play a super over.")
        super_over(toss_result)
    else:
        print("You lost by " + str(machine_score - your_score) + " runs.")

