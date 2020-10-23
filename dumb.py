import random
import time
import os
from game import Game

class Dumb(Game):
    
    def play(self):
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
            print(choice)
            try:
                self.board.insertMove(choice, self.playerTurn)
            except:
                print('Campo não existente. Tente novamente')
                self.play()

        else:
            self.board.insertMove(random.choice(range(1, 9)), self.playerTurn)
        
        self.switchPlayer()
