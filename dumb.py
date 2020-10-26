import random
import time
import os
from game import Game

class Dumb(Game):
    
    def play(self):
        list_choices = [i for i in range(1, 10)]

        while True:
            os.system("clear")
            self.board.draw()

            winner = self.board.hasWinner()
            if winner != None:
                self.board.printWinner(winner)
                self.resetBoard()
                time.sleep(1.4)
                self.play()
                
            if self.playerTurn == 'X':
                choice = 0
                choice = int(input('Escolha um campo: '))
                try:
                    self.board.insertMove(choice, self.playerTurn)
                except:
                    print('Campo não existente. Tente novamente')
                    self.play()

            else:
                choice = random.choice(list_choices)
                self.board.insertMove(choice, self.playerTurn)
            list_choices.pop(list_choices.index(choice))
            self.switchPlayer()
