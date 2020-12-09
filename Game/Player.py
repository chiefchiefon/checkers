from Game.Piece import Piece


class Player:
    def __init__(self, color):
        self.name = self.set_name()
        self.pieces = self.init_pieces(color)
        self.color = color

    def set_name(self, name=None):
        if name is None:
            return "Player" + self.__name__.toString()
        return name

    def init_pieces(self, color):
        base = 48 * color.value
        return {base + k:  Piece() for k in [0, 2, 4, 6, 11, 13, 15]}

    def __add__(self, index_piece):
        self.pieces[index_piece[0]] = index_piece[1]

    def __sub__(self, index):
        self.pieces.pop(index)
