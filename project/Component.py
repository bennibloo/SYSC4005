from enum import Enum

class Component(Enum):
    def __str__(self):
        return str(self.value)
    TYPE_1 = 1
    TYPE_2 = 2
    TYPE_3 = 3

