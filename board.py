from color import color

class Board:
  def __init__(self):
    self.state = self.configBoard()
    self.references = self.configReferences()

  # Configura tabuleiro inicial
  def configBoard(self):
    return  [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]

  # Configura referencias por numero no tabuleiro
  def configReferences(self):
    refs = {}
    cont = 1
    for i in range(3):
      for j in range(3):
        refs[cont] = (i , j)
        cont += 1
    return refs

  # Checagem de fim de tabuleiro
  def hasWinner(self):
    # Vitória Vertical
    for i in range(3):
      if (self.state[0][i] != '.' and
        self.state[0][i] == self.state[1][i] and
        self.state[1][i] == self.state[2][i]):
          return self.state[0][i]

    # Vitória Horizontal
    for i in range(0, 3):
      if self.state[i] == ['X', 'X', 'X']:
        return 'X'
      elif self.state[i] == ['O', 'O', 'O']:
        return 'O'

    # Vitória Diagonal Principal
    if (self.state[0][0] != '.' and
      self.state[0][0] == self.state[1][1] and
      self.state[0][0] == self.state[2][2]):
      return self.state[0][0]

    # Vitória Diagonal Secundária
    if (self.state[0][2] != '.' and
      self.state[0][2] == self.state[1][1] and
      self.state[0][2] == self.state[2][0]):
      return self.state[0][2]

    # Checa se tabuleiro está totalmente preenchido, se não, continua o jogo
    for i in range(3):
      for j in range(3):
        if (self.state[i][j] == '.'):
          return None

    # Em caso de empate
    return '.'      

  def insertMove(self, ref, simbol):
      i, j = self.references[ref]
      if self.state[i][j] == '.':
        self.state[i][j] = simbol
      else:
       print('Campo já preenchido')

  def getField(self, ref):
    i, j = self.references[ref]
    if self.state[i][j] == '.':  
      return ref
    elif self.state[i][j] == 'X':
      return color.RED + color.BOLD + self.state[i][j] + color.END
    elif self.state[i][j] == 'O':
      return color.BLUE + color.BOLD + self.state[i][j] + color.END

  def findRefByValue(self, i, j):
    for key, value in self.references.items():
      if value[0] is i and value[1] is j:
        return key

  def printWinner(self, winner):
      if winner != '.':
        print(f"'<>'<>'<>' Vitória [{winner}] '<>'<>'<>'")
      else:
        print('# Empate #')

  def draw(self):
    print('+-----------+')
    print('|',self.getField(1), "|", self.getField(2), "|", self.getField(3),'|')
    print('|','-'* 9,'|')
    print('|',self.getField(4), "|", self.getField(5), "|", self.getField(6),'|')
    print('|','-'* 9,'|')
    print('|',self.getField(7), "|", self.getField(8), "|", self.getField(9),'|')
    print('+-----------+')