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

  def update(self, current_difficulty, games_won, games_played):
    with open('stats.sav', 'w+') as f:
      f.writelines(['{},{},{}'.format(difficulty,\
          int(stat['wins']) + (games_won if (current_difficulty == difficulty) else 0), \
          int(stat['games_played']) + (games_played if current_difficulty == difficulty else 0)) + '\n' \
          for (difficulty, stat) in self.stats.items()])
      print self.stats[current_difficulty]['wins'] + ' wins out of ' + self.stats[current_difficulty]['games_played'] + ' games.'
