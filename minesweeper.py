from game import Game

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
    user_selection = raw_input('\nTile selection (ex: 1,3): ')
    if (',' in user_selection):
      x,y = user_selection.split(',')
      # Only allow if in the bounds of the board
      if ((x and y) and (-1 < int(x) < game.width) and (-1 < int(y) < game.height)):
        return (int(x), int(y))
    print('Invalid Coordinates')


if __name__=='__main__':
  show_instructions()
  # Create the game with difficulty
  game = Game(get_difficulty())

  # Show initial board
  game.print_board()

  while (game.get_status() == 'in_progress'):
    # Just an example of getting a selection and showing the new board
    game.select(*get_selection(game))
    game.print_board()

  # show the result of the game
  print('\nYou {}!'.format(game.get_status()))