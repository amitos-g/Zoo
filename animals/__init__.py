from typing import Any

from pydantic import BaseModel
from enum import Enum


class Color(Enum):
    RED : str = "red"
    BLUE: str = "blue"
    GREEN: str = "green"
    YELLOW: str = "yellow"
    PINK: str = "pink"
    WHITE: str = "white"
    BLACK: str = "black"
    ORANGE: str = "orange"
class AnimalRequest(BaseModel):
    name : str
    color: Color
    size : float
    gender : str

class AnimalResponse:
    id : int
    name : str
    type : str
    color: Color
    size : float
    gender : str

    def __init__(self, args):
        self.id = args[0]
        self.name = args[1]
        self.type = args[2]
        self.color = args[3]
        self.size = args[4]
        self.gender = args[5]
    def __repr__(self):
        return (f"id: {self.id}, "
                f"name: {self.name}, "
                f"type: {self.type}, "
                f"color: {self.color}, "
                f"size: {self.size}, "
                f"gender: {self.gender}")


from .sea import Whale, Shark, Dolphin
from .air import Pigeon, Parrot, Crow
from .land import Tiger, Lion, Monkey

