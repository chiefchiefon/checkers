from Game.Piece import Piece


def init_pieces(color):
    base = 48 * color.value
    return {base + k:  Piece() for k in [0, 2, 4, 6, 9, 11, 13, 15]}


class Player:
    def __init__(self, color):
        self.color = color
        self.name = self.set_name()
        self.pieces = init_pieces(color)

    def set_name(self, name=None):
        if name is None:
            return "Player " + self.color.name
        return name

    def __add__(self, index_piece):
        self.pieces[index_piece["index"]] = index_piece["piece"]

    def add(self, index, piece):
        self.pieces[index] = piece

    def __sub__(self, index):
        self.pieces.pop(index)

    def sub(self, index):
        self.pieces.pop(index)
