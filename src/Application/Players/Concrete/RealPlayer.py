from Players.PlayerInterf import PlayerInterf


class RealPlayer(PlayerInterf):

    def __init__(self, plnum):
        super().__init__(plnum)

    def handlePlay(self):
        pass

    def senterror(self, errnum: int):
        pass

