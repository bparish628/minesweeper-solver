from game import Game

def get_difficulty():
  """Prompts the user for the difficulty"""
  print('\nDifficulties:')
  print('1: Beginner')
  print('2: Intermediate')
  print('X: Exit\n')

  # Keep prompting the user until they select a correct option
  while True:
    user_diff = raw_input('Please select a difficulty:')
    if (user_diff == '1'):
      return 'BEGINNER'
    elif (user_diff == '2'):
      return 'INTERMEDIATE'
    elif (user_diff == 'X'):
      exit(1)

def get_selection():
  while True:
    user_selection = raw_input('Tile selection (ex: 1,3):')
    if (',' in user_selection):
      x,y = user_selection.split(',')
      if (x and y):
        return (int(x), int(y))
    print('Invalid Coordinates')


if __name__=='__main__':
  # Create the game with difficulty
  game = Game(get_difficulty())

  # Show initial board
  game.print_board()

  # Just an example of getting a selection and showing the new board
  game.select(*get_selection())
  game.print_board()