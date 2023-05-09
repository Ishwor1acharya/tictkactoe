import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    pass

def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    pass

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    return row, col

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    return True
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    return 0
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    return leaders
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    pass

'''

def menu():
    while True:
        print("Main Menu:")
        print("1. Play game")
        print("2. Save score")
        print("3. Load scores")
        print("q. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            # Call the function to play the game
            play_game()
        elif choice == '2':
            # Call the function to save the score
            save_score()
        elif choice == '3':
            # Call the function to load and display scores
            load_scores()
        elif choice == 'q':
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")


def load_scores():
    """
    This is load_scores function where score is store.
    Open leaderboard.txt file.
    Use loads function to load dictionary.
    """
    leaderboard = {}
    if not exists('leaderboard.txt'):  # if leaderboard does not exist
        print("\nLeaderboard does not exists.\n")
        with open('leaderboard.txt', 'w') as new_file: # w is write mode
            print('Creating new leaderboard.') # it create new leaderboard
            json.dump({}, new_file)
    with open('leaderboard.txt', 'r') as read_file: # r is read mode
        line = read_file.read() # read the file only
    try:
        leaderboard = json.loads(line)  # loads all names and score in leaderboard
    except json.JSONDecodeError:  # if leaderboard does not have object
        with open('leaderboard.txt', 'w') as write_file: #create a new, empty leaderboard file
            json.dump({}, write_file) # it write an empty python dictionary to a file in json format
    return leaderboard # return the leaderboard dictionary


def save_score(score):
    """
    This is save_score function where all the player name as well as all score of
    player is stored in dictionary . player name is input to save the name.
    
    Updates dictionary.
    Opens leaderboard.txt on write mode
    Saves using dump function.
    """
    user_name = input('Enter your name: ').strip().lower()  # prompt user to enter name
    leaderboard = load_scores()  # call load_scores function to get dictionary with names and scores
    all_players = leaderboard.keys()  # only get usernames
    if user_name in all_players:  # if user in leaderboard
        old_score = leaderboard[user_name]
        new_score = old_score + score  # update the old score
        leaderboard[user_name] = new_score
    else:  # if user not in leaderboard
        leaderboard[user_name] = score
    with open('leaderboard.txt', 'w') as write_file:
        json.dump(leaderboard, write_file)  # stores all names and scores
        print('\nSaved Successfully.')


def display_leaderboard(leaders):
    """
    This is display_leaderboard function.
    Displays all players and their scores in console.
    """
    print('''
======LEADERBOARD======
''') # print the head of the board name.
    if leaders == {}:  # empty leaderboard
        print('No leaders yet') # it print no leder yet if there is empty leaderboard.
    else:
        for names, scores in leaders.items():  # loops run for all names and scores 
        
            print(names, 'scored', scores) # print player name and score in leaderboard.
'''