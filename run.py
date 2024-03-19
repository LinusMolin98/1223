import random
from colorama import init, Fore

init(autoreset=True)  # Initialize Colorama for colored output

def print_board(board, hide_ships=True):
    """
    Prints the game board to the console with ASCII art and color enhancements.
    """
    for row in board:
        row_str = " ".join([
            f"{Fore.BLUE}≈" if cell == 'O' else
            f"{Fore.RED}╳" if cell == 'X' else
            f"{Fore.GREEN}□" if not hide_ships and cell == 'S' else
            f"{Fore.BLUE}≈" for cell in row
        ])
        print(row_str)

def generate_board(size):
    """
    Generates a square game board of the given size initialized with 'O'.
    """
    return [['O' for _ in range(size)] for _ in range(size)]

def place_ship(board, ship_size, ships):
    """
    Places a ship of the specified size on the board at a random location.
    """
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - ship_size)
        else:  # vertical
            row = random.randint(0, len(board) - ship_size)
            col = random.randint(0, len(board[0]) - 1)
        ship_coordinates = {(row, col + i) if orientation == 'horizontal' else (row + i, col) for i in range(ship_size)}
        
        if all(board[r][c] == 'O' for r, c in ship_coordinates):
            for r, c in ship_coordinates:
                board[r][c] = 'S'
            ships.append({'coordinates': ship_coordinates, 'hits': set()})
            break

def check_for_sunken_ships(player_guess, ships):
    """
    Checks if a hit results in a sunken ship and updates the ships list.
    """
    for ship in ships:
        if player_guess in ship['coordinates']:
            ship['hits'].add(player_guess)
            if ship['hits'] == ship['coordinates']:
                return True
    return False

def player_turn(board, previous_guesses, size):
    """
    Manages the player's turn, including input validation and tracking guesses.
    """
    while True:
        try:
            user_input = input("Enter row and column numbers, or type 'help' or 'quit': ").lower()
            if user_input == 'quit':
                return None
            if user_input == 'help':
                print_instructions(size)
                continue

            guess_row, guess_col = map(int, user_input.split())
            if (guess_row, guess_col) in previous_guesses or not (0 <= guess_row < size and 0 <= guess_col < size):
                print(f"{Fore.YELLOW}Invalid guess or already guessed. Try again.")
                continue

            previous_guesses.add((guess_row, guess_col))
            return guess_row, guess_col
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter row and column numbers separated by a space.")

def print_instructions(size):
    """
    Prints the game instructions to the console.
    """
    print("\nWelcome to Battleship!")
    print(f"The game board is a {size}x{size} grid.")
    print("Enter row and column numbers to guess where the enemy ships are hidden.")
    print("If you hit all parts of a ship, it's considered sunk.")
    print("Repeat until you have sunk all the enemy's ships to win.")
    print("\nCommands:")
    print("- Enter 'quit' during your turn to exit the game.")
    print("- Enter 'help' during your turn to see these instructions again.\n")

def print_victory():
    """
    Prints a victory message with ASCII art.
    """
    victory_art = f"{Fore.GREEN}Congratulations! You've sunk all the ships and won the game!"
    print(victory_art)

def play_battleship(size, num_ships):
    """
    Main function to setup and play the Battleship game.
    """
    print_instructions(size)
    player_board = generate_board(size)
    previous_guesses = set()
    ships = []

    for _ in range(num_ships):
        place_ship(player_board, 3, ships)

    ships_remaining = num_ships

    while ships_remaining > 0:
        print("Player Board:")
        print_board(player_board, hide_ships=True)
        
        player_guess = player_turn(player_board, previous_guesses, size


   