from enum import Enum

from Game.Player import Player


class Color(Enum):
    WHITE = 0
    BLACK = 1


def get_position(player, pos):
    pos = int(input(player.name + pos + " please [0..63]:"))
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
            self.print()
            self.make_next_move()
            self.check_for_win()

    def make_next_move(self):
        player = self.player[self.turn % 2]
        opponent = self.player[(self.turn + 1) % 2]

        source = get_position(player, " source")
        while source not in player.pieces:
            print(player.name, " there is no piece of yours in ", source, ". Please try again:")
            source = get_position(player, "source")

        basic_steps = [7, 9]
        # destinations = [source + i for i in basic_steps if (source + i)//8 - source//8 == 1]
        destinations = [source + i * (1 - 2 * player.color.value) for i in basic_steps if
                        source + i * (1 - 2 * player.color.value) not in player.pieces and
                        source + i * (1 - 2 * player.color.value) not in opponent.pieces and
                        0 <= source + i * (1 - 2 * player.color.value) < 64 and
                        (source + i * (1 - 2 * player.color.value)) // 8 - source // 8 == 1 * (1 - 2 * player.color.value)]
        destinations.extend([source + i * 2 * (1 - 2 * player.color.value) for i in basic_steps if
                            source + i * (1 - 2 * player.color.value) in opponent.pieces and
                            0 <= source + i * 2 * (1 - 2 * player.color.value) < 64 and
                            (source + i * 2 * (1 - 2 * player.color.value)) // 8 - source // 8 == 2 * (1 - 2 * player.color.value)])
        destinations.extend(player.pieces[source].degree.value * [source + i * 2 for i in basic_steps if
                                                            source + i * 2 < 64 and
                                                            source + i * 2 not in player.pieces and
                                                            source + i * 2 not in opponent.pieces and
                                                            (source + i * 2) // 8 - source // 8 == 2])
        destinations.extend(player.pieces[source].degree.value * [source - i * 2 for i in basic_steps if
                                                            source - i * 2 >= 0 and
                                                            source - i * 2 not in player.pieces and
                                                            source - i * 2 not in opponent.pieces and
                                                            (source - i * 2) // 8 - source // 8 == -2])
        print(player.pieces[source].degree.name, " potential moves:", destinations)

        while len(destinations) == 0:
            print("Your ", player.pieces[source].degree.name, " has no where to move.")
            source = get_position(player, "source")

        destination = get_position(player, "destination")
        while destination not in destinations:
            print("Destination ", destination, " is not in destinations options. Try again.")
            destination = get_position(player, "destination")
        while destination in player.pieces:
            print(player.name, ", the destination you've chosen is occupied by a",
                  player.pieces[destination].degree, "of yours; you can't move there.")
            destination = get_position(player, " destination")

        if abs(destination - source) > 9:
            opponent.sub((destination + source) // 2)

#        player.pieces += [source, player.pieces[source]]
#        player.pieces += {"index": source, "piece": player.pieces[source]}
#        player.pieces -= source
        player.add(destination, player.pieces[source])
        player.sub(source)

    def print(self):
        print("--------------------------")
        for i in range(64):
            if i in self.player[0].pieces:
                # print(self.player[0].pieces[i], end=""),
                print("P", end='\t')
            elif i in self.player[1].pieces:
                # print(self.player[1].pieces[i], end=""),
                print("p", end='\t')
            elif (i // 8 % 2 + i % 2) % 2 == 0:
                print(" ", end='\t')
            else:
                print("░", end='\t')

            if (i + 1) % 8 == 0:
                print()

        print("----------------")
        for i in range(8):
            for j in range(8):
                print(i * 8 + j, end="\t")
            print()

    def check_for_win(self):
        if len(self.player[0].pieces) == 0:
            print(self.player[1].name + "won")
            self.is_there_win = True
        if len(self.player[1].pieces) == 0:
            print(self.player[0].name + "won")
            self.is_there_win = True

        self.turn += 1
