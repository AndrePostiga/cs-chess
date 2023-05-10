from src.Application.Players.AI.AIModel import AIModel
from src.Application.Players.PlayerInterf import PlayerInterf


class Bot(PlayerInterf):

    def __init__(self, plnum):
        super().__init__(plnum)
        self.ai_instance = AIModel.intanceAI()

    def senterror(self, errnum: int):
        pass

    def handlePlay(self):
        self.ai_instance.handlePlay()
        pass
