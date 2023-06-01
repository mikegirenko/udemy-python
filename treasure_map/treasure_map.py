"""
a program that will mark a spot with an x
"""


class TreasureMap:
    def __init__(self):
        self.treasure_map = [['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️']]

    def user_input(self) -> str:
        spot_to_mark = input("Enter a spot to mark")

        return spot_to_mark

    def mark_a_spot(self, spot_to_mark) -> list:
        column = int(spot_to_mark[0])
        row = int(spot_to_mark[1])
        if row == 0:
            row = 0
        else:
            row = row - 1
        if column == 0:
            column = 0
        else:
            column == column - 1

        self.treasure_map[row][column] = "x"

        return self.treasure_map

    def print_map(self, this_map):
        print(f"\n{this_map[0]}, \n{this_map[1]}, \n{this_map[2]}")


if __name__ == "__main__":
    obj = TreasureMap()
    spot_to_mark = obj.user_input()
    obj.mark_a_spot(spot_to_mark)
