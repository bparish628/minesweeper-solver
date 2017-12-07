import random
import board

class Minesweeper_Solver:
  def __init__(self, game):
    self.game = game
    self.found_mines = [] # holds an array of states for the known mines

  def solve(self):
    self.found_mines = [] # set all found_mines to blank since this is a new solve
    self.actions = actions = self.game.available_moves()
    self.board_changed = False

    # initially select a random action
    x, y = random.choice(actions)
    # We don't want to start off with an automatic loss, because that is no fun
    while self.game.solved_board[y][x] == -1:
      x, y = random.choice(actions)

    # select the first move of the game
    self.game.select(x, y)

    # Now we run it through the algorithm
    while (self.game.get_status() == 'in_progress'):
      self.run_best_action()

    return self.game.get_status() == 'win'

  def run_best_action(self):
    self.actions = list(set(self.game.available_moves()) - set(self.found_mines))

    # run the pattern
    self.run_pattern_algorithms()
    # If there were no changes and there are actions left, then select a random choice
    if (not self.board_changed and self.actions):
      x, y = random.choice(self.actions)
      self.game.select(x,y)

  def run_pattern_algorithms(self):
    self.board_changed = False
    for state in self.get_states_near_unmarked():
      self.number_equals_unmarked(state)
      self.number_equals_mines(state)
    self.found_mines = list(set(self.found_mines)) # removes duplicates

  def get_states_near_unmarked(self):
    states_nearby = [] # holds an array of states next to unmarked tiles
    actions = self.actions
    for action in actions:
      for (nx, ny) in list(board.get_neighbors(action, self.game.board)):
        if (self.game.get(nx, ny) != '*'):
          states_nearby.append((nx, ny))
    return list(set(states_nearby)) # remove dups

  def count_free_squares(self, coord):
    neighbors = list(board.get_neighbors(coord, self.game.board))
    return sum([1 if self.game.get(nx,ny) == '*' else 0 for (nx, ny) in neighbors])

  def count_mine_squares(self, coord):
    neighbors = list(board.get_neighbors(coord, self.game.board))
    return sum([1 if self.game.get(nx,ny) == '*' and (nx, ny) in self.found_mines else 0 for (nx, ny) in neighbors])

  def number_equals_unmarked(self, coord):
    """Checks if the coords number is equal to the unmarked tiles, then adds values to found_mines"""
    x,y = coord
    unmarked_tiles = self.count_free_squares(coord)
    if (unmarked_tiles == self.game.get(x,y)):
      for n in list(board.get_neighbors((x, y), self.game.board)):
        if (self.game.get(*n) == '*'):
          self.found_mines.append(n)

  def number_equals_mines(self, coord):
    """Checks if the coords number is equal to the mines tiles around it, then selects the non mine tiles"""
    x,y = coord
    mine_tiles = self.count_mine_squares(coord)
    if (mine_tiles == self.game.get(x,y)):
      for n in list(board.get_neighbors((x, y), self.game.board)):
        if (self.game.get(*n) == '*' and n not in self.found_mines):
          self.game.select(*n)
          self.board_changed = True
