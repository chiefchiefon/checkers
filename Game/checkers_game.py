from enum import Enum

from Game.Player import Player


class Color(Enum):
    WHITE = 0
    BLACK = 1


def get_position(player, pos):
    pos = int(input(player.name + "enter your" + pos + "please [0..63]:"))
    try:
        while pos < 0 or pos > 63:
            pos = int(input("an integer between 0 and 63 only is expected"))
    except ValueError:
        print("Please enter an integer")

    return pos


class CheckersGame:
    def __init__(self):
        self.turn = 0
        self.is_there_win = False
        self.player = {0: Player(Color.WHITE), 1: Player(Color.BLACK)}

    def run(self):
        while not self.is_there_win:
            pass
            # print_pieces
            # make_next_move()
            # check_for_win()

    def make_next_move(self):
        player = self.player[self.turn % 2]
        opponent = self.player[(self.turn + 1) % 2]

        source = get_position(player, "source")
        while source not in player.pieces:
            print(player.name, "there is no piece of yours in", source, ". Please try again:")
            source = get_position(player, "source")

        basic_steps = [7, 9]
        # destinations = [source + i for i in basic_steps if (source + i)//8 - source//8 == 1]
        destinations = [source + i * (1 - 2 * player.color.value) for i in basic_steps if
                        source + i * (1 - 2 * player.color.value) not in player.pieces and
                        source + i * (1 - 2 * player.color.value) not in opponent.pieces and
                        0 <= source + i * (1 - 2 * player.color.value) < 64 and
                        (source + i * (1 - 2 * player.color.value)) // 8 - source // 8 == 1 * (1 - 2 * player.color.value)]
        destinations.extend([source + i * (1 - 2 * player.color.value) for i in basic_steps if
                            source + i * (1 - 2 * player.color.value) in opponent.pieces and
                            0 <= source + i * (1 - 2 * player.color.value) < 64 and
                            (source + i * (1 - 2 * player.color.value)) // 8 - source // 8 == 2 * (1 - 2 * player.color.value)])
        destinations.extend(player.pieces[source].degree * [source + i * 2 for i in basic_steps if
                                                            source + i * 2 < 64 and
                                                            source + i * 2 not in player.pieces and
                                                            source + i * 2 not in opponent.pieces and
                                                            (source + i * 2) // 8 - source // 8 == 2])
        destinations.extend(player.pieces[source].degree * [source - i * 2 for i in basic_steps if
                                                            source - i * 2 >= 0 and
                                                            source - i * 2 not in player.pieces and
                                                            source - i * 2 not in opponent.pieces and
                                                            (source - i * 2) // 8 - source // 8 == -2])
        print("Potentially, your", player.pieces[source].degree, "could move to one of:", destinations)

        destination = get_position(player, "destination")
        while destination in player.pieces:
            print(player.name, ", the destination you've chosen is occupied by a",
                  player.pieces[destination].degree, "of yours; you can't move there.")
            destination = get_position(player, "destination")

        if abs(destination - source) > 9:
            opponent.pieces -= abs(destination - source) // 2

        player.pieces += (source, player.pieces[source])
        player.pieces -= source
