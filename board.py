import random
from itertools import product

def Random_Board(width, height, bombs):
    """This function creates a random Minesweeper
board of dimensions width x height with bombs
amount of bombs (all integers). The board is
returned as a 2D list where every element
is an integer. -1 if there is a bomb in
that space, 0-8 for the amount of bombs
the space touches if there is no bomb in it."""

    # Define directions [row_increment, column_increment]
    directions = [[-1, 0], # North
                  [-1, 1], # North East
                  [ 0, 1], # East
                  [ 1, 1], # South East
                  [ 1, 0], # South
                  [ 1,-1], # South West
                  [ 0,-1], # West
                  [-1,-1]] # North West

    # Initialise board
    board = [['']*width]*height
    for i in range(height):
        board[i]=[0]*width

    # Choosing bomb placements
    bomb_indexes = [random.randint(0, width*height-1) for i in range(bombs)]

    # Make sure to change duplicate bomb placements
    for i in range(bombs):
        while bomb_indexes[i] in bomb_indexes[:i]:
            bomb_indexes[i] = random.randint(0, width*height-1)

    # Putting bombs on field
    x = 1
    for index in bomb_indexes:
        row, column = Get_Row_Column(index, width)
        board[row][column] = -1

    # Calculating number of bombs each square touches
    for index in bomb_indexes:
        row, column = Get_Row_Column(index, width)
        for direction in directions:
            if (0 <= row + direction[0] < height and    # Row increment still in-bounds
                0 <= column + direction[1] < width):    # Column increment still in-bounds

                # Only increment space in direction if there is not a bomb there
                if (board[row + direction[0]][column + direction[1]] != -1):
                    board[row + direction[0]][column + direction[1]] += 1

    return board

def Get_Row_Column(index, width):
    """Returns row, column for the index-th
element of an array/list with row length
width if read from top left to right."""
    return index//width, index%width

def Print_Board(board):
    """This function prints the board nicely aligned with the x,y axis titles"""
    length = len(board)
    pad = 3
    print  # print an empty line
    print (''.join([''.rjust(pad), ''.rjust(pad)] + [str(x).ljust(pad) for x in range(length)])) # Print each index number for the row
    print (''.join([''.rjust(pad), ''.rjust(pad)] + ['-'.ljust(pad) for x in range(length)])) # Print a - for each number

    for (y, row) in enumerate(board):
        print(''.join([str(y).rjust(pad), '|'] + ['!'.rjust(pad) if x==-1 else str(x).rjust(pad) for x in row]))

def create_unknown_board(board):
    """This function returns the board as an unknown board"""
    return [['*' for i in board] for i in board]

def get_neighbors(cell, board):
    size = len(board)
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c

class Tile:
    def __init__(self, game, coord):
        self.game = game
        self.revealed = False
        self.coord = coord
        x,y = coord
        self.value = game.solved_board[y][x]
        self.neighbors = get_neighbors(coord, game.board)