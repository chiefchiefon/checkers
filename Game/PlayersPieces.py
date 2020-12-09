from Game.Piece import Piece
from Game.Tile import Tile


class PlayersPieces:
    # def __init__(self, color):
    #     self.my_pieces = self.init_pieces(color)

    def init_pieces(self, color):
        # TODO: Should I adopt the recommendation of PyCharm (PEP8?) to take init_pieces out of class player_pieces?
        # TODO: assert color is either Color.White or Color.Black Enum. I may write it as base = 48 * get_color(color)
        #  and make the assertion inside get_color(color)
        base = 48 * color.value
        return {base + k: Tile(base + k, Piece()) for k in [0, 2, 4, 6, 11, 13, 15]}

    def is_valid_move(self, s, d):
        basic_steps = [7, 9]

    def __add__(self, tile):
        self.my_pieces[tile.position] = tile

    def __sub__(self, tile):
        self.my_pieces.pop(tile.position)
