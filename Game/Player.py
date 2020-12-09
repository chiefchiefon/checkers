from Game.PlayersPieces import PlayersPieces


class Player:
    def __init__(self, color):
        self.name = self.set_name()
        self.pieces = PlayersPieces(color)

    def set_name(self, name=None):
        if name is None:
            return "Player" + self.__name__.toString()
        return name
