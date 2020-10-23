import time
import os
from board import Board
from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self):
        self.board = Board()
        self.scoreboard = {'X': 0, 'O': 0}
        self.playerTurn = 'O'

    # Troca o jogador
    def switchPlayer(self):
        if self.playerTurn == 'X':
            self.playerTurn = 'O'
        else:
            self.playerTurn = 'X'

    def resetBoard(self):
        self.board = Board()

    def drawScoreboard(self):
        print(f"<>[X] {scoreboard['X']} ][ {scoreboard['O']} [O]<>")

    def playerMove(self):
        choice = 0
        choice = int(input('Escolha um campo: '))
        print(choice)
        try:
          self.board.insertMove(choice, self.playerTurn)
          started = True
        except:
          print('Campo não existente. Tente novamente')
          self.start()

    @abstractmethod
    def play(self):
        pass