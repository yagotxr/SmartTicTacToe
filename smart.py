import random
import time
import os
from board import Board
from game import Game


class Smart(Game):

    # Player 'O' is max, in this case AI
    def max(self, alpha, beta):

        # Valores possiveis para max:
        # -1 - derrota
        # 0  - empate
        # 1  - vitória

        maxv = -2
        px = None
        py = None

        result = self.board.hasWinner()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board.state[i][j] == '.':
                    self.board.state[i][j] = 'O'
                    (m, min_i, in_j) = self.min(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.board.state[i][j] = '.'

                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv

        return (maxv, px, py)

    # Jogador
    def min(self, alpha, beta):

        # Valores possiveis para min:
        # -1 - vitória
        # 0  - empate
        # 1  - derrota

        minv = 2

        qx = None
        qy = None

        result = self.board.hasWinner()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board.state[i][j] == '.':
                    self.board.state[i][j] = 'X'
                    (m, max_i, max_j) = self.max(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.board.state[i][j] = '.'

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)

    def play(self):
        started = False

        while True:
            self.board.draw()

            winner = self.board.hasWinner()
            if winner != None:
                self.board.printWinner(winner)
                self.resetBoard()
                time.sleep(1.4)
                self.play()

            if self.playerTurn == 'X':
                (m, qx, qy) = self.min(-2, 2)
                choice = 0
                choice = int(input('Escolha um campo: '))
                print(choice)
                try:
                    self.board.insertMove(choice, self.playerTurn)
                    started = True
                except:
                    print('Campo não existente. Tente novamente')
                    self.play()

            else:
                if started:
                    (m, i, j) = self.max(-2, 2)
                    self.board.insertMove(
                        self.board.findRefByValue(i, j), self.playerTurn)
                else:
                    self.board.insertMove(random.choice(
                        range(1, 10)), self.playerTurn)
            self.switchPlayer()
