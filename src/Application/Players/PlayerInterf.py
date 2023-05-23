from abc import abstractmethod, ABC


class PlayerInterf(ABC):

    def __init__(self, plnum):
        self.numPlayer = plnum

    @abstractmethod
    def handlePlay(self):
        pass

    def setNumPlayer(self, num: int):
        self.numPlayer = num

    @abstractmethod
    def senterror(self, errnum: int):
        pass
