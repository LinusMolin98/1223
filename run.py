import random
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Initialize Colorama to automatically reset styles

def print_board(board, hide_ships=True):
    """
    Prints the game board to the console with color enhancements.

    Args:
    board: The game board, a list of lists containing 'O' for open water,
           'S' for ships, and 'X' for hits.
    hide_ships: Whether ships ('S') should be hidden and displayed as 'O'.
    """
    for row in board:
        row_str = " ".join([
            f"{Fore.BLUE}O" if cell == 'O' else
            f"{Fore.RED}X" if cell == 'X' else
            f"{Fore.GREEN}S" if not hide_ships and cell == 'S' else
            f"{Fore.BLUE}O" for cell in row
        ])
        print(row_str)

def generate_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]

def place_ship(board, ship_size, ships):
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board) - ship_size)
        else:
            row = random.randint(0, len(board) - ship_size)
            col = random.randint(0, len(board) - 1)

        ship_coordinates = set()

        for i in range(ship_size):
            if orientation == 'horizontal':
                ship_coordinates.add((row, col + i))
            else:
                ship_coordinates.add((row + i, col))

        if all(board[r][c] == 'O' for r, c in ship_coordinates):
            for r, c in ship_coordinates:
                board[r][c] = 'S'
            ships.append({'coordinates': ship_coordinates, 'hits': set()})
            break
def player_turn(board, previous_guesses, size):
    while True:
        try:
            user_input = input("Enter row and column numbers, or type 'help' or 'quit': ")
            if user_input.lower() == 'quit':
                return None
            elif user_input.lower() == 'help':
                print_instructions(size)
                continue

            inputs = user_input.split()
            if len(inputs) != 2:
                raise ValueError("Please enter both a row and a column number.")

            guess_row, guess_col = int(inputs[0]), int(inputs[1])

            if (guess_row, guess_col) in previous_guesses:
                print(f"{Fore.YELLOW}You've already guessed that! Try a different spot.")
                continue

            if 0 <= guess_row < len(board) and 0 <= guess_col < len(board):
                previous_guesses.add((guess_row, guess_col))
                return guess_row, guess_col
            else:
                print(f"{Fore.MAGENTA}Out of bounds! Please guess within the board.")
        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter two numbers (row col), 'help', or 'quit'.")

def print_instructions(size):
    print("\nWelcome to Battleship!")
    print("The goal is to sink all the enemy's ships.")
    print("\nInstructions:")
    print("- The game board is a {}x{} grid.".format(size, size))
    print("- Enter row and column numbers to guess where the enemy ships are hidden.")
    print("- If you hit all parts of a ship, it's considered sunk.")
    print("- Repeat until you have sunk all the enemy's ships to win.")
    print("\nCommands:")
    print("- Enter 'quit' during your turn to exit the game.")
    print("- Enter 'help' during your turn to see these instructions again.\n")            

def play_battleship(size, num_ships):
    print_instructions(size)
    player_board = generate_board(size)
    previous_guesses = set()
    ships = []  # List to track ships

    for _ in range(num_ships):
        place_ship(player_board, 3, ships)

    ships_remaining = num_ships

    while ships_remaining > 0:
        print("Player Board:")
        print_board(player_board)
        
        player_guess = player_turn(player_board, previous_guesses, size)
        if player_guess is None:
            print(f"{Fore.LIGHTRED_EX}Game ended by player.")
            break

        result = player_board[player_guess[0]][player_guess[1]]

        if result == 'S':
            print(f"{Fore.GREEN}Hit! You've hit a ship!")
            player_board[player_guess[0]][player_guess[1]] = 'X'
            # Additional logic needed here to check if a ship is completely sunk

   