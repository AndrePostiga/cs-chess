from src.Application.Players.AI.AIModel import AIModel
from src.Application.Players.PlayerInterf import PlayerInterf


class Bot(PlayerInterf):

    def __init__(self, plnum):
        super().__init__(plnum)
        self.aiInstance = AIModel.intanceAI()

    def senterror(self, errnum: int):
        pass

    def handlePlay(self):
        self.aiInstance.handlePlay()
        pass
