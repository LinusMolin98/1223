import random
from colorama import init, Fore

init(autoreset=True)  # Initialize Colorama for colored output

def print_board(board, hide_ships=True):
    """
    Prints the game board to the console with ASCII art and color enhancements.
    
    Parameters:
    - board: The game board, a 2D list representing the grid.
    - hide_ships: Boolean indicating whether to hide ships on the board.
    """
    for row in board:
        print(" ".join([
            f"{Fore.BLUE}≈" if cell == 'O' else
            f"{Fore.RED}╳" if cell == 'X' else
            f"{Fore.GREEN}□" if not hide_ships and cell == 'S' else
            f"{Fore.BLUE}≈" for cell in row
        ]))

def generate_board(size):
    """
    Generates a square game board of the given size initialized with 'O' for open water.
    
    Parameters:
    - size: Integer, the size of the board (size x size).
    
    Returns:
    - A 2D list representing the game board.
    """
    return [['O' for _ in range(size)] for _ in range(size)]

def place_ship(board, ship_size, ships):
    """
    Places a ship of the specified size on the board at a random location without overlap.
    
    Parameters:
    - board: The game board, a 2D list.
    - ship_size: Integer, the size of the ship to place.
    - ships: A list of dictionaries, each representing a ship with its coordinates and hits.
    """
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - ship_size)
        else:
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
    Prints the enhanced game instructions to the console.
    """
    print(f"\n{Fore.CYAN}Welcome to Battleship!")
    print("Objective:")
    print("  Your goal is to sink all hidden ships on the board by guessing their locations.\n")
    print("Game Board:")
    print(f"  The board is a grid of size {size}x{size}. Here's what the symbols mean:")
    print(f"    {Fore.BLUE}≈ : Water (unexplored territory)")
    print(f"    {Fore.RED}╳ : Hit (part of a ship you've successfully targeted)")
    print(f"    {Fore.CYAN}~ : Miss (an unsuccessful guess)\n")
    print("Commands:")
    print("  - 'quit' to exit the game.")
    print("  - 'help' to display these instructions again.\n")
    print("Tips:")
    print("  - Ships can be oriented horizontally or vertically.")
    print("  - Try spreading out your guesses to discover the general location of a ship.\n")
    print(f"{Fore.YELLOW}Ready to play? Make your first guess by entering row and column numbers (e.g., '0 3').")
    print(f"{Fore.YELLOW}Good luck, captain!\n")

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
        
        player_guess = player_turn(player_board, previous_guesses, size)
        if player_guess is None:
            print(f"{Fore.LIGHTRED_EX}Game ended by player.")
            return  # Exit the function if the player quits

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
            return  # Exit the function after displaying the win message

if __name__ == "__main__":
    board_size = 5  # Define the size of the game board
    num_ships = 3   # Define the number of ships
    play_battleship(board_size, num_ships)



   