import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def generate_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]

