import random


def print_board(board, hide_ships=True):
    """
    Prints the game board to the console.

    Args:
    board: The game board, a list of lists containing 'O' for open water,
           'S' for ships, and 'X' for hits.
    hide_ships: Whether ships ('S') should be hidden and displayed as 'O'.
    """
    for row in board:
        print(" ".join(['X' if cell == 'S' and hide_ships else cell for cell in row]))


def generate_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]


def place_ship(board, ship_size):
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board) - ship_size)
        else:
            row = random.randint(0, len(board) - ship_size)
            col = random.randint(0, len(board) - 1)

        ship_coordinates = []

        for i in range(ship_size):
            if orientation == 'horizontal':
                ship_coordinates.append((row, col + i))
            else:
                ship_coordinates.append((row + i, col))

        valid = all(board[row][col] == 'O' for row, col in ship_coordinates)
        if valid:
            for row, col in ship_coordinates:
                board[row][col] = 'S'
            break


def player_turn(board, previous_guesses, size):
    while True:
        try:
            user_input = input("Enter row and column numbers, or type 'help' or 'quit': ")
            if user_input.lower() == 'quit':
                return None
            elif user_input.lower() == 'help':
                print_instructions(size)
                continue  # Show instructions and prompt for input again

            # Split the input by any space to separate row and col inputs
            inputs = user_input.split()
            if len(inputs) != 2:
                raise ValueError("Please enter both a row and a column number.")

            guess_row, guess_col = int(inputs[0]), int(inputs[1])

            if (guess_row, guess_col) in previous_guesses:
                print("You've already guessed that! Try a different spot.")
                continue

            if 0 <= guess_row < len(board) and 0 <= guess_col < len(board):
                previous_guesses.add((guess_row, guess_col))
                return guess_row, guess_col
            else:
                print("Out of bounds! Please guess within the board.")
        except ValueError:
            print("Invalid input! Please enter two numbers (row col), 'help', or 'quit'.")


def play_battleship(size, num_ships):
    player_board = generate_board(size)
    previous_guesses = set()

    for _ in range(num_ships):
        place_ship(player_board, 3)

    ships_remaining = num_ships

    while ships_remaining > 0:
        print("Player Board:")
        print_board(player_board)
        
        player_guess = player_turn(player_board, previous_guesses)
        if player_guess is None:
            print("Game ended by player.")
            break

        result = player_board[player_guess[0]][player_guess[1]]

        if result == 'S':
            print("Hit!")
            player_board[player_guess[0]][player_guess[1]] = 'X'
            # Additional logic needed here to check if a ship is completely sunk
        elif result == 'X':
            print("You've already hit this spot.")
        else:
            print("Miss.")
      
    if ships_remaining == 0:
        print("All ships sunk! You win!")        