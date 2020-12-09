class Piece:
    def __init__(self):
        self.isKing = False

    def get_piece_degree(self):
        if self.isKing:
            return "King"
        return "Pawn"
