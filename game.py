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
    self.width = DIFFICULTIES[difficulty]['width']
    self.height = DIFFICULTIES[difficulty]['height']
    self.bombs = DIFFICULTIES[difficulty]['bombs']
    self.solved_board = board.Random_Board(self.width, self.height, self.bombs)
    self.board = board.create_unknown_board(self.solved_board)

  def print_board(self):
    """"Prints the current state of the board. This is a pass through to board.Print_Board()"""
    board.Print_Board(self.board)

  def select(self, x, y):
    """Selects the cord (x,y) of the board and executes a 'click' action"""
    # select the tile passed in
    self.board[y][x] = self.solved_board[y][x]

    # Open neighbor tiles if it is 0
    if (self.board[y][x] == 0):
      neighbors = list(board.get_neighbors((x,y), self.board))

      while len(neighbors):
        # print neighbors
        current_x, current_y = neighbors.pop(0)
        if (current_x == None and current_y == None):
          continue
        self.board[current_y][current_x] = self.solved_board[current_y][current_x]

        if (self.board[current_y][current_x] == 0):
          current_neighbors = list(board.get_neighbors((current_x, current_y), self.board))
          near_untounched_tiles = sum([ 1 if self.board[ny][nx] == '*' else 0 for nx,ny in current_neighbors])
          if (near_untounched_tiles > 0):
            for nx,ny in current_neighbors:
              if self.board[ny][nx] == '*':
                neighbors.append((nx, ny))

  def get(self, x, y):
    """Gets the value of the cord (x,y) of the board"""
    return self.board[y][x] # x and y coords need to be switched to be correct

  def get_status(self):
    """
      Returns whether the game was won, lost, or in_progress
    """
    unsolved_squares = 0
    shown_bombs = 0
    for y in range(self.height):
      for x in range(self.width):
        symbol = self.get(x,y)
        # if a bomb is shown then they lose
        if (symbol == -1):
          return 'lose'
        if (symbol == '*'):
          unsolved_squares += 1

    # if amount of unsolved squares is the number of bombs they win
    if (unsolved_squares == self.bombs):
      return 'win'

    # else the game is in_progress
    return 'in_progress'
