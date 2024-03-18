import random
from colorama import init, Fore

init(autoreset=True)  # Initialize Colorama for colored output

def print_board(board, hide_ships=True):
    """
    Prints the game board to the console with optional hiding of ships.
    """
    for row in board:
        print(" ".join([f"{Fore.BLUE}O" if cell == 'O' else
                        f"{Fore.RED}X" if cell == 'X' else
                        f"{Fore.GREEN}S" if not hide_ships and cell == 'S' else
                        f"{Fore.BLUE}O" for cell in row]))

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
            ship_coordinates = {(row, col + i) for i in range(ship_size)}
        else:  # vertical
            row = random.randint(0, len(board) - ship_size)
            col = random.randint(0, len(board[0]) - 1)
            ship_coordinates = {(row + i, col) for i in range(ship_size)}

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

        player_guess = player_turn(player_board, previous_guesses, size)
        if player_guess is None:
            print(f"{Fore.LIGHTRED_EX}Game ended by player.")
            break

        guess_row, guess_col = player_guess
        result = player_board[guess_row][guess_col]

        if result == 'S':
            print(f"{Fore.GREEN}Hit! You've hit a ship!")
            player_board[guess_row][guess_col] = 'X'
            if check_for_sunken_ships((guess_row, guess_col), ships):
                print(f"{Fore.YELLOW}You've sunk a ship!")
                ships_remaining -= 1
        elif result == 'X':
            print(f"{Fore.YELLOW}You've already hit this spot.")
        else:
            print(f"{Fore.CYAN}Miss.")
            player_board[guess_row][guess_col] = 'X'

        if ships_remaining == 0:
            print(f"{Fore.GREEN}All ships sunk! You win!")

if __name__ == "__main__":
    board_size = 5  # Board size can be adjusted
    num_ships = 3   # Number of ships can be adjusted
    play_battleship(board_size, num_ships)


   