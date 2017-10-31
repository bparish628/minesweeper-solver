import board

DIFFICULTIES = {
  'BEGINNER': {
    'width': 8,
    'height': 8,
    'bombs': 10
  },

  'INTERMEDIATE': {
    'width': 16,
    'height': 16,
    'bombs': 40
  }
}

class Game:
  def __init__(self, difficulty):
    width = DIFFICULTIES[difficulty]['width']
    height = DIFFICULTIES[difficulty]['height']
    bombs = DIFFICULTIES[difficulty]['bombs']
    self.solved_board = board.Random_Board(width, height, bombs)
    self.board = board.create_unknown_board(self.solved_board)

  def print_board(self):
    """"Prints the current state of the board. This is a pass through to board.Print_Board()"""
    board.Print_Board(self.board)

