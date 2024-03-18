import random
from colorama import init, Fore, Back, Style

init(autoreset=True)  # Initialize Colorama to automatically reset styles

def print_board(board, hide_ships=True):
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
        row, col = random.randint(0, len(board) - ship_size), random.randint(0, len(board) - 1) if orientation == 'horizontal' else (random.randint(0, len(board) - 1), random.randint(0, len(board) - ship_size))
        ship_coordinates = {(row + i if orientation == 'vertical' else row, col + i if orientation == 'horizontal' else col) for i in range(ship_size)}
        if all(board[r][c] == 'O' for r, c in ship_coordinates):
            for r, c in ship_coordinates:
                board[r][c] = 'S'
            ships.append({'coordinates': ship_coordinates, 'hits': set()})
            break

def check_for_sunken_ships(player_guess, ships):
    for ship in ships:
        if player_guess in ship['coordinates']:
            ship['hits'].add(player_guess)
            if ship['hits'] == ship['coordinates']:
                return True
    return False

def player_turn(board, previous_guesses, size):
    while True:
        try:
            user_input = input("Enter row and column numbers, or type 'help' or 'quit': ")
            if user_input.lower() == 'quit':
                return None
            elif user_input.lower() == 'help':
                print_instructions(size)
                continue
            guess_row, guess_col = map(int, user_input.split())
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
            if check_for_sunken_ships(player_guess, ships):
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
    board_size = 5
    num_ships = 3
    play_battleship(board_size, num_ships)

   