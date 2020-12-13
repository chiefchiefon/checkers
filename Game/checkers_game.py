from enum import Enum

from Game.Player import Player


class Color(Enum):
    WHITE = 0
    black = 1


def get_position(player, pos):

    while True:
        try:
            pos = int(input(player.name + pos + " [0..63]:"))
            while pos < 0 or pos > 63:
                pos = int(input("an integer between 0 and 63 only is expected; try again: "))
            return pos
        except ValueError:
            print("Please enter an integer")


def is_crowning(source, destination):
    if destination == 57 and source in [48, 43, 50] or destination == 59 and source in [41, 50, 45, 52] or destination == 61 and source in [43, 52, 47, 54] or destination == 63 and source in [45, 54]:
        return True
    if destination == 0 and source in [9, 18] or destination == 2 and source in [16, 9, 20, 11] or destination == 4 and source in [18, 11, 22, 13] or destination == 6 and source in [20, 13, 15]:
        return True
    return False


def calculate_destinations(player, source, opponent):
    basic_steps = (7, 9)
    destinations = set()
    for step in basic_steps:
        polarity = 1 - 2 * player.color.value
        single_step = source + step * polarity
        if single_step not in player.pieces and single_step not in opponent.pieces and\
                0 <= single_step < 64 and single_step // 8 - source // 8 == 1 * polarity:
            destinations.add(single_step)

        double_step = source + 2 * step * polarity
        if single_step in opponent.pieces and double_step not in opponent.pieces and double_step not in player.pieces and\
                0 <= double_step < 64 and double_step // 8 - source // 8 == 2 * polarity:
            destinations.add(double_step)

        if player.pieces[source].is_king():
            king_single_bwd = source - step * polarity
            if 0 <= king_single_bwd < 64 and king_single_bwd // 8 - source // 8 == -1 and\
                    king_single_bwd not in player.pieces and king_single_bwd not in opponent.pieces:
                destinations.add(king_single_bwd)
            king_double_bwd = source - step * 2 * polarity
            if king_double_bwd < 64 and king_double_bwd // 8 - source // 8 == -2 and\
                king_double_bwd not in player.pieces and king_double_bwd not in opponent.pieces and\
                    king_single_bwd in opponent.pieces:
                destinations.add(king_double_bwd)

    return destinations


class CheckersGame:
    def __init__(self):
        self.turn = 0
        self.is_there_win = False
        self.player = {0: Player(Color.WHITE), 1: Player(Color.black)}

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

        destinations = calculate_destinations(player, source, opponent)

        while len(destinations) == 0:
            print("Your ", player.pieces[source].degree.name, " has no where to move.")
            source = get_position(player, "source")
            while source not in player.pieces:
                print(player.name, " there is no piece of yours in ", source, ". Please try again:")
                source = get_position(player, "source")

            destinations = calculate_destinations(player, source, opponent)

        print(player.pieces[source].degree.name, " potential moves:", destinations)
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
        if is_crowning(source, destination):
            player.pieces[destination].set_king()
        player.sub(source)

    def print(self):
        print("--------------------------")
        for i in range(64):
            if i in self.player[0].pieces:
                # print(self.player[0].pieces[i], end=""),
                print("", self.player[0].pieces[i].degree.name.upper()[::3], end='\t')
            elif i in self.player[1].pieces:
                # print(self.player[1].pieces[i], end=""),
                print("", self.player[1].pieces[i].degree.name.lower()[::3], end='\t')
            elif (i // 8 % 2 + i % 2) % 2 == 0:
                print("   ", end='\t')
            else:
                print("  ░", end='\t')

            if (i + 1) % 8 == 0:
                print()

        print("----------------")
        for i in range(8):
            for j in range(8):
                print("", i * 8 + j, end="\t")
            print()

    def check_for_win(self):
        if len(self.player[0].pieces) == 0:
            print(self.player[1].name + " won")
            self.is_there_win = True
        if len(self.player[1].pieces) == 0:
            print(self.player[0].name + " won")
            self.is_there_win = True

        self.turn += 1
