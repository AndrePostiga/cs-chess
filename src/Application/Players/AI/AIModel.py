class AIModel:
    ai_instance = None

    @staticmethod
    def intanceAI():
        if AIModel.ai_instance is None:
            AIModel.ai_instance = AIModel()
        return AIModel.ai_instance

    def handlePlay(self):
        pass
