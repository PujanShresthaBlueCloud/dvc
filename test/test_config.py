import pytest
class NotInRange(Exception):
    """This is the class for giving Not in range error."""
    def __init__(self, message="Value is not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 4
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange

def test_something():
    a = 2
    b = 2
    assert True
