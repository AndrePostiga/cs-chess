import pytest
from src.Application.Teste.ClasseParaTestar import ClasseParaTestar

class TestExample:

    # maintain test_ prefix for pytest discovering
    def test_upper(self):
        assert 'foo'.upper() == 'FOO'


    def test_isupper(self):
        assert 'FOO'.isupper() is True
        assert 'Foo'.isupper() is False


    def test_split(self):
        s = 'hello world'
        assert s.split() == ['hello', 'world']
        # check that s.split fails when the separator is not a string
        with pytest.raises(TypeError):
            s.split(2)

    def test_classe_para_testar(self):
        sum = ClasseParaTestar(5, 10)
        assert (5 + 10) == sum.soma()