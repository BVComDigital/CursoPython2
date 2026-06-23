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
       print(f'NOme do Jogo: {self.name}')
       print(f'Ano de Lançamento: {self.yearLaunch}')
       print(f'Multiplayer: {self.multiplayer}')
       print(f'Avlaiação do Jogo: {self.note}\n')
   
   def evaluate(self, note):
       self.totalEvaluation += note
       self.evaluators += 1

   def average(self):
       print(f'Média do Jogo {self.name}: {self.totalEvaluation / self.evaluators}')

game1 = Game("The legend os Zelda", 2017, False, 9.5)
game2 = Game("Fortinet", 2017, True, 8.0)
game3 = Game("Red Dead Redemption", 2018, False, 10.00)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)
game2.evaluate(8.5)
game1.average()
game2.average()

# Exibindo o número total de jogos criados
print(f'Total de jogos criados: {Game.total_games}')