from enum import Enum


class Degree(Enum):
    PAWN = 0
    KING = 1


class Piece:
    def __init__(self):
        self.degree = Degree.PAWN

    def get_piece_degree(self):
        return self.degree
        # if self.degree is Degree.KING:
        #     return "King"
        # return "Pawn"

    def set_king(self):
        self.degree = Degree.KING

    def is_king(self):
        return self.degree == Degree.KING

    def __str__(self):
        return self.degree.name
        # if self.degree is Degree.KING:
        #     return "KING"
        # return "PAWN"
