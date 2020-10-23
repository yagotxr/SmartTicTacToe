from dumb import Dumb
from medium import Medium
from smart import Smart

def gameMaker(level):
    if level is 1:
        return Dumb()
    if level is 2:
        return Medium()
    if level is 3:
        return Smart()
