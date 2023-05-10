class AIModel:
    AIInstance = None

    @staticmethod
    def intanceAI():
        if AIModel.AIInstance is None:
            AIModel.AIInstance = AIModel()
        return AIModel.AIInstance

    def handlePlay(self):
        pass
