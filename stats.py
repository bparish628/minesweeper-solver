class Stats:

  def __init__(self):
    self.stats = {}

  def _set_stats(self, f):
    content = f.readlines()
    for line in content:
      stat = line.strip().split(',')
      self.stats[stat[0]] = { 'wins': stat[1], 'games_played': stat[2] }

  def get(self):
    try:
      with open('stats.sav', 'r+') as f:
        self._set_stats(f)
    except IOError:
      # If file doesn't exist create it and start data over
      with open('stats.sav', 'w+') as f:
        f.write('BEGINNER,0,0\n')
        f.write('INTERMEDIATE,0,0')
      with open('stats.sav', 'r+') as f:
        self._set_stats(f)

  def update(self, game):
    with open('stats.sav', 'w+') as f:
      f.writelines(['{},{},{}'.format(difficulty,\
          int(stat['wins']) + (1 if (game.difficulty == difficulty and game.get_status() == 'win') else 0), \
          int(stat['games_played']) + (1 if game.difficulty == difficulty else 0)) + '\n' \
          for (difficulty, stat) in self.stats.items()])
