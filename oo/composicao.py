class Game:
   total_games = 0
   def __init__(self, name='', yearLaunch=0, multiplayer=0, note=0.0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0

   def __str__(self):
      return f'Game: {self.name}'
   
   def technical_sheet(self):
       print(f'###Dados do Jogo###')
       print(f'Nome do Jogo: {self.name}')
       print(f'Ano de Lançamento: {self.yearLaunch}')
       print(f'Multiplayer: {self.multiplayer}')
       print(f'Avlaiação do Jogo: {self.note}\n')

class GameStudio:
   def __init__(self, name=''):
        self.name = name
        self.games = []

   def add_game(self, game):
      self.games.append(game)

   def evaluate_studio_quality(self):
       total_notes = sum(game.note for game in self.games)
       num_games = len(self.games)
       if num_games == 0:
           print(f'O estúdio {self.name} ainda não lançou jogos')
       else:
           average_note = total_notes / num_games
           print(f'Avaliação média do jogos do estúdio {self.name}: {average_note:.2f}\n')

game1 = Game("The legend os Zelda", 2017, False, 9.5)
game2 = Game("Fortinet", 2017, True, 8.0)
game3 = Game("Red Dead Redemption", 2018, False, 10.00) 

studio = GameStudio('Awesome Games')
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()
   

      
        