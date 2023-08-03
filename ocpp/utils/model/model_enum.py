from enum import Enum


class ModelEnum(Enum):
    @classmethod
    def choices(cls):
        return [(i.value, i.value) for i in cls]

    @classmethod
    def is_valid(cls, choice):
        choices = {i.value for i in cls}
        return choice in choices

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)
