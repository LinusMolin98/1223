import random


def print_board(board, hide_ships=True):
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


def player_turn(board, previous_guesses):
    while True:
        try:
            row_input = input("Enter 'quit' to end the game, or guess Row (0 to {}): ".format(len(board) - 1))
            if row_input.lower() == 'quit':
                return None
            guess_row = int(row_input)

            col_input = input("Guess Col (0 to {}): ".format(len(board) - 1))
            guess_col = int(col_input)

            if (guess_row, guess_col) in previous_guesses:
                print("You've already guessed that! Try a different spot.")
                continue

            if 0 <= guess_row < len(board) and 0 <= guess_col < len(board):
                previous_guesses.add((guess_row, guess_col))  # Add guess to set of previous guesses
                return guess_row, guess_col
            else:
                print("Out of bounds! Please guess within the board.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def play_battleship(size, num_ships):
    player_board = generate_board(size)

    for _ in range(num_ships):
        place_ship(player_board, 3)  

    ships_remaining = num_ships

    while ships_remaining > 0:
        print("Player Board:")
        print_board(player_board)

        player_guess = player_turn(player_board)
        if player_guess is None:
            break  # User decided to quit the game

        result = player_board[player_guess[0]][player_guess[1]]

        if result == 'S':
            print("Congratulations! You hit a ship!")

            # Check if the ship is completely sunk
            if all(cell == 'X' for row in player_board for cell in row if cell == 'S'):
                print("You sank a ship!")
                ships_remaining -= 1
            player_board[player_guess[0]][player_guess[1]] = 'X'
        elif result == 'X':
            print("You've already guessed that one. Try again.")
        else:
            print("Sorry, you missed.")
      
    if ships_remaining == 0:
        print("Congratulations! You sank all the ships. You win!")


if __name__ == "__main__":
    board_size = 5  
    num_ships = 3  
    play_battleship(board_size, num_ships)         