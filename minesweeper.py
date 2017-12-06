from game import Game
from stats import Stats
from solver import Minesweeper_Solver
import sys

def show_instructions():
  print('\n\t * untouched tile')
  print('\t ! bomb')
  print('\t 0-5 Number of bombs nearby')

def get_difficulty():
  """Prompts the user for the difficulty"""
  print('\nDifficulties:')
  print('1: Beginner')
  print('2: Intermediate')
  print('X: Exit\n')

  # Keep prompting the user until they select a correct option
  while True:
    user_diff = raw_input('Please select a difficulty: ')
    if (user_diff == '1'):
      return 'BEGINNER'
    elif (user_diff == '2'):
      return 'INTERMEDIATE'
    elif (user_diff == 'X'):
      exit(1)

def get_selection(game):
  while True:
    user_selection = raw_input('\nTile selection (ex: 1 3): ')
    if user_selection == '@hint' :
      for y,row in enumerate(game.solved_board):
        for x,col in enumerate(game.solved_board[y]):
          if game.solved_board[y][x] != -1 and (x,y) in game.available_moves():
            return (x, y)
    if (' ' in user_selection):
      x,y = user_selection.split(' ')
      # Only allow if it's an available move
      if (x and y and (int(x),int(y)) in game.available_moves()):
        return (int(x), int(y))
    print('Invalid Coordinates')


if __name__=='__main__':
  # Create a new stats object
  stats = Stats()
  stats.get()

  if ('--solver' in sys.argv):
    games_played = 0
    games_won = 0
    for i in range(5000):
      games_played += 1
      game = Game('BEGINNER')
      solver = Minesweeper_Solver(game)
      is_a_win = solver.solve()
      games_won += 1 if is_a_win else 0
    stats.update('BEGINNER', games_won, games_played)
  else:
    show_instructions()

    # Create the game with difficulty
    game = Game(get_difficulty())

    # Show initial board
    game.print_board()

    while (game.get_status() == 'in_progress'):
      # Just an example of getting a selection and showing the new board
      game.select(*get_selection(game))
      game.print_board()

    stats.update(game.difficulty, 1 if game.get_status() == 'win' else 0, 1)
    # show the result of the game
    print('\nYou {}!'.format(game.get_status()))