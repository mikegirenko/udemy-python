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
        column = spot_to_mark[0]
        row = spot_to_mark[1]
        self.treasure_map[int(row) - 1][int(column) - 1] = "x"

        return self.treasure_map

    def print_map(self, this_map):
        print(f"\n{this_map[0]}, \n{this_map[1]}, \n{this_map[2]}")


if __name__ == "__main__":
    obj = TreasureMap()
    spot_to_mark = obj.user_input()
    obj.mark_a_spot(spot_to_mark)
