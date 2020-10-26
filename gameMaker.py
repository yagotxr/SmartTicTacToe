from dumb import Dumb
from medium import Medium
from smart import Smart

def gameMaker(level):
    if level == 1:
        return Dumb()
    if level == 2:
        return Medium()
    if level == 3:
        return Smart()
    else:
        raise Exception('Level inválido')
