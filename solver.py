import random
import board

class Minesweeper_Solver:
  def __init__(self, game):
    self.game = game
    self.found_mines = [] # holds an array of states

  def solve(self):
    actions = self.game.available_moves()

    x, y = random.choice(actions)
    # We don't want to start off with an automatic loss, because that is no fun
    while self.game.solved_board[y][x] == -1:
      x, y = random.choice(actions)

    # select the first move of the game
    self.game.select(x, y)

    # Now we run it through the algorithm
    while (self.game.get_status() == 'in_progress'):
      self.best_action()

    return self.game.get_status() == 'win'

  def best_action(self):
    actions = list(set(self.game.available_moves()) - set(self.found_mines))
    if (not self.check_patterns() and actions):
      x, y = random.choice(actions)
      self.game.select(x,y)

  def check_patterns(self):
    changes = False
    for (y, row) in enumerate(self.game.board):
      for (x, col) in enumerate(row):
        self.number_equals_unmarked((x, y))
        did_change = self.number_equals_mines((x, y))
        if (did_change):
          changes = True
    self.found_mines = list(set(self.found_mines)) # removes duplicates
    # print self.found_mines
    return changes

  def count_free_squares(self, coord):
    x,y = coord
    neighbors = list(board.get_neighbors((x, y), self.game.board))
    return sum([1 if self.game.get(nx,ny) == '*' else 0 for (nx, ny) in neighbors])

  def count_mine_squares(self, coord):
    x,y = coord
    neighbors = list(board.get_neighbors((x, y), self.game.board))
    return sum([1 if self.game.get(nx,ny) == '*' and (nx, ny) in self.found_mines else 0 for (nx, ny) in neighbors])

  def number_equals_unmarked(self, coord):
    x,y = coord
    unmarked_tiles = self.count_free_squares(coord)
    if (unmarked_tiles == self.game.get(x,y)):
      for n in list(board.get_neighbors((x, y), self.game.board)):
        if (self.game.get(*n) == '*'):
          self.found_mines.append(n)

  def number_equals_mines(self, coord):
    x,y = coord
    mine_tiles = self.count_mine_squares(coord)
    new_opened_tiles = False
    if (mine_tiles == self.game.get(x,y)):
      for n in list(board.get_neighbors((x, y), self.game.board)):
        if (self.game.get(*n) == '*' and n not in self.found_mines):
          self.game.select(*n)
          new_opened_tiles = True
    return new_opened_tiles
