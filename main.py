# Text-based game

import random

valid_inputs = ["1", "2", "3"]

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input, please try again.")

def create_board():
    row_count = 3
    column_count = 3
    board = []

    for _ in range(row_count):
        board.append([0] * column_count)

    return board
    
# Adapting print_board function for a 3x3 board
def print_board(board):
    print("\n========== Tic Tac Toe =========")
    print("Player 1: X       Player 2: O\n")
    print('    1   2   3')
    print('  -------------')
    for i, row in enumerate(board):
        row_str = str(i+1) + ' | '
        for cell in row:
            if cell == 0:
                row_str += '  | '
            elif cell == 1:
                row_str += 'X | '
            else:
                row_str += 'O | '
        print(row_str + '\n  -------------')
    print()

def local_2_player_game():
    board = create_board()
    current_player = 1

    while True:
        clear_screen()
        print_board(board)
        execute_player_turn(current_player, board)
        
        result = end_of_game(board)
        if result != 0:
            print_board(board)
            if result == 1:
                print('Player 1 wins!')
            elif result == 2:
                print('Player 2 wins!')
            else:
                print("It's a draw!")
            return

        current_player = 3 - current_player  # Switch current player between 1 and 2

def end_of_game(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:  # Horizontal
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:  # Vertical
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:  # Diagonal top-left to bottom-right
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:  # Diagonal bottom-left to top-right
        return board[0][2]

    # If the board is full, it's a draw.
    for row in board:
        if 0 in row:
            return 0  # Game not over.
    return 3  # Draw.

def game_against_cpu():
    board = create_board()
    current_player = 1

    print("Select CPU difficulty level")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty = validate_input("Please choose an option (1-3): ", ["1", "2", "3"])
    
    while True:
        clear_screen()
        print_board(board)
        if current_player == 1:  # Human player
            execute_player_turn(current_player, board)
        else:  # AI player
            execute_player_turn(current_player, board, difficulty)
        
        result = end_of_game(board)
        if result != 0:
            print_board(board)
            if result == 1:
                print('Player 1 wins!')
            elif result == 2:
                print('The computer wins!')
            else:
                print("It's a draw!")
            return

        current_player = 3 - current_player  # Switch current player between 1 and 2

def execute_player_turn(player, board, difficulty=None):
    if difficulty != None:  # AI player
        game_against_cpu(board, player, difficulty)
    else:  # Human player
        while True:
            row_input = validate_input(
                f"Player {player}, please enter the row you would like to place your piece into: ", valid_inputs)
            column_input = validate_input(
                f"Player {player}, please enter the column you would like to place your piece into: ", valid_inputs)
            row = int(row_input) - 1
            column = int(column_input) - 1
            if board[row][column] == 0:
                board[row][column] = player
                return
            else:
                print("That cell is occupied, please try again.")

def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    return None


def main():
    # This is the main loop that runs until the user chooses to exit the game.
    while True:
        clear_screen()  # Clear the console screen for a fresh menu display.

        # Print the main menu with options for the user.
        print("=============== Main Menu ===============")
        print("Welcome to Tic-Tac-Toe!")
        print("1. View rules")
        print("2. Play a local 2 player game")
        print("3. Play a game against the computer")
        print("4. Exit")
        print("=========================================")

        # Prompt the user to choose an option and validate their input.
        game_choice = validate_input("Please choose an option (1-4): ", ["1", "2", "3", "4"])

        # If the user chooses option 1 (View rules):
        if game_choice == "1":
            clear_screen()  # Clear the console screen.
            print_rules()  # Display the rules of the game.
            # Wait for the user to press Enter before returning to the main menu.
            input("Press Enter to return to the main menu.")
            clear_screen()

        # If the user chooses option 2 (Play a local 2 player game):
        elif game_choice == "2":
            clear_screen()  # Clear the console screen.
            local_2_player_game()  # Start the local 2 player game.
            # Wait for the user to press Enter before returning to the main menu.
            input("Press Enter to return to the main menu.")

        # If the user chooses option 3 (Play a game against the computer):
        elif game_choice == "3":
            clear_screen()  # Clear the console screen.
            game_against_cpu()  # Start the game against CPU.
            # Wait for the user to press Enter before returning to the main menu.
            input("Press Enter to return to the main menu.")

        # If the user chooses option 4 (Exit):
        elif game_choice == "4":
            print("Thanks for playing! Goodbye!")  # Print a farewell message.
            break  # Break out of the while loop to exit the game.

    return None



def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Players take turns putting their marks in")
    print("empty squares. The first player to get 3")
    print("of her marks in a row (up, down, across,")
    print("or diagonally) is the winner. When all 9 ")
    print("squares are full, the game is over.\n")
    print("If no player has 3 marks in a row, the")
    print("the game ends in a tie.")
    print("=========================================")

if __name__ == "__main__":
    main()
