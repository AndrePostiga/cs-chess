from abc import ABC, abstractmethod


class Piece(ABC):
    # guardar movimento melhor em uma mini matriz ou sla, e deve ser static
    nMovement = 0
    movementType = ""

    def __init__(self, Xpos: int, Ypos: int):
        self.Xpos = Xpos
        self.Ypos = Ypos

    @abstractmethod
    def move(self, table, i, j):
        pass

    def getType(self):
        return self.__class__
