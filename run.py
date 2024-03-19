import random
from colorama import init, Fore

init(autoreset = True)


def print_board(board, hide_ships = True):
    """Print the game board with ASCII art and color enhancements."""
    for row in board:
        print(" ".join(
[f"{Fore.BLUE}≈" if cell == 'O' else
f"{Fore.RED}╳" if cell == 'X' else
f"{Fore.GREEN}□" if not hide_ships and cell == 'S' else
f"{Fore.BLUE}≈" for cell in row]
        ))


def generate_board(size):
    """Generate a square game board initialized with 'O' for open water."""
    return [['O' for _ in range(size)] for _ in range(size)]


def place_ship(board, ship_size, ships):
    """
    Place a ship on the board at a random location without overlap.
    """
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        row, col = (random.randint(0, len(board) - ship_size),
                    random.randint(0, len(board) - 1))
        if orientation == 'vertical':
            row, col = col, row

        ship_coordinates = {
(row + i if orientation == 'vertical' else row,
col + i if orientation == 'horizontal' else col)
            for i in range(ship_size)}

        if all(board[r][c] == 'O' for r, c in ship_coordinates):
            for r, c in ship_coordinates:
                board[r][c] = 'S'
            ships.append({'coordinates': ship_coordinates, 'hits': set()})
            break


def check_for_sunken_ships(player_guess, ships):
    """Check if a hit results in a sunken ship."""
    for ship in ships:
        if player_guess in ship['coordinates']:
            ship['hits'].add(player_guess)
            if ship['hits'] == ship['coordinates']:
                return True
    return False


def player_turn(board, previous_guesses, size):
    """Manage the player's turn, including input validation."""
    while True:
        user_input = input(
            "Enter row and column numbers, or type 'help' or 'quit': "
        ).lower()
        if user_input in ['quit', 'help']:
            if user_input == 'quit':
                return None
            print_instructions(size)
            continue

        try:
            guess_row, guess_col = map(int, user_input.split())
            if not (0 <= guess_row < size) or not (0 <= guess_col < size):
                print(f"{Fore.YELLOW}Out of bounds. Try again.")
                continue
        except ValueError:
            print(f"{Fore.RED}Invalid input. Use row and column numbers.")
            continue

        if (guess_row, guess_col) in previous_guesses:
            print(f"{Fore.YELLOW}Already guessed. Try a new spot.")
            continue

        previous_guesses.add((guess_row, guess_col))
        return guess_row, guess_col


def print_instructions(size):
    """Print enhanced game instructions."""
    print(f"\n{Fore.CYAN}Welcome to Battleship!")
    print("Objective: Sink all hidden ships on the board.")
    print("Game Board: A grid of size {}x{}. Symbols mean:".format(size, size))
    print(f"{Fore.BLUE}≈ : Water")
    print(f"{Fore.RED}╳ : Hit")
    print(f"{Fore.CYAN}~ : Miss")
    print("\nCommands:\n - 'quit': Exit game\n - 'help': Show instructions")
    print("\nTips:\n - Ships are placed horizontally or vertically.")


def print_victory():
    """Print a victory message."""
    print(f"{Fore.GREEN}Congratulations! All ships sunk! You win!")


def play_battleship(size, num_ships):
    """Setup and start the Battleship game."""
    print_instructions(size)
    player_board = generate_board(size)
    previous_guesses = set()
    ships = []

    for _ in range(num_ships):
        place_ship(player_board, 3, ships)

    ships_remaining = num_ships

    while ships_remaining > 0:
        print("Player Board:")
        print_board(player_board, hide_ships = True)
        player_guess = player_turn(player_board, previous_guesses, size)
        if player_guess is None:
            print(f"{Fore.LIGHTRED_EX}Game ended by player.")
            return

        guess_row, guess_col = player_guess
        result = player_board[guess_row][guess_col]

        if result == 'S':
            print(f"{Fore.GREEN}Hit! A ship



   