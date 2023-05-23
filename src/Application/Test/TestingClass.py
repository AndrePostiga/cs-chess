class TestingClass:
    __test__ = False
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self) -> int:
        return self.a + self.b
