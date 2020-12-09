from enum import Enum


class Degree(Enum):
    PAWN = 0
    KING = 1


class Piece:
    def __init__(self):
        self.degree = Degree.PAWN

    def get_piece_degree(self):
        if self.degree is Degree.KING:
            return "King"
        return "Pawn"
