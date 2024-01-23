import random

def print_board(board):
    for row in board:
        print(" ".join(row))

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

def player_turn(board):
    while True:
        try:
            user_input = input("Enter 'quit' to end the game.\nGuess Row (0 to {}): ".format(len(board) - 1))
            if user_input.lower() == 'quit':
                return None  
            guess_row = int(user_input)
            
            user_input = input("Enter 'quit' to end the game.\nGuess Col (0 to {}): ".format(len(board) - 1))
            if user_input.lower() == 'quit':
                return None  
            guess_col = int(user_input)
            
            if 0 <= guess_row < len(board) and 0 <= guess_col < len(board):
                return guess_row, guess_col
            else:
                print("Invalid input. Please enter valid row and column numbers.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")


def play_battleship(size, num_ships):
    player_board = generate_board(size)

    for _ in range(num_ships):
        place_ship(player_board, 3)  

    while True:
        print("Player Board:")
        print_board(player_board)

        player_guess = player_turn(player_board)
        result = player_board[player_guess[0]][player_guess[1]]

        if result == 'S':
            print("Congratulations! You hit a ship!")
            player_board[player_guess[0]][player_guess[1]] = 'X'
        elif result == 'X':
            print("You've already guessed that one. Try again.")
        else:
            print("Sorry, you missed.")

      
        if all('S' not in row for row in player_board):
            print("Congratulations! You sank all the ships. You win!")
            break

if __name__ == "__main__":
    board_size = 8  
    num_ships = 3  
    play_battleship(board_size, num_ships)            