from abc import ABC, abstractmethod


class Piece(ABC):
    # guardar movimento melhor em uma mini matriz ou sla, e deve ser static
    nMovement = 0
    movementType = ""

    def __init__(self, x_pos: int, y_pos: int):
        self.x_pos = x_pos
        self.y_pos = y_pos

    @abstractmethod
    def move(self, table, i, j):
        pass

    def getType(self):
        return self.__class__
