from src.Application.Players.Concrete.Bot import Bot
from src.Application.Players.Concrete.RealPlayer import RealPlayer


class PlayerFacto:
    # TIPO FACTORY
    factory = None

    @staticmethod
    def chamarfactory():
        if PlayerFacto.factory is None:
            PlayerFacto.factory = PlayerFacto()
        return PlayerFacto.factory

    def __init__(self):
        self.numberPlayer = 0
        self.numberBot = 0

    def createPlayer(self):
        self.numberPlayer = self.numberPlayer + 1
        return RealPlayer(self.numberPlayer + self.numberBot)

    def createBot(self):
        self.numberBot = self.numberBot + 1
        return Bot(self.numberBot + self.numberPlayer)
