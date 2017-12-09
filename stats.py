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
    self.stats[current_difficulty]['wins'] = str(int(self.stats[current_difficulty]['wins']) + games_won)
    self.stats[current_difficulty]['games_played'] = str(int(self.stats[current_difficulty]['games_played']) + games_played)
    with open('stats.sav', 'w+') as f:
      f.writelines(['{},{},{}'.format(difficulty,\
          stat['wins'], \
          stat['games_played']) + '\n' \
          for (difficulty, stat) in self.stats.items()])
      win_percentage = float(self.stats[current_difficulty]['wins']) / float(self.stats[current_difficulty]['games_played']) * 100
      print '{}: {} wins out of {} games. Winrate: {}%'.format(current_difficulty, self.stats[current_difficulty]['wins'], self.stats[current_difficulty]['games_played'], win_percentage)