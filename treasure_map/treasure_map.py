"""
a program that will mark a spot on a 3x3 map with an x
"""


class TreasureMap:
    def __init__(self):
        self.treasure_map = [["⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️"]]

    def user_input(self) -> str:
        spot_to_mark = input("Enter a spot to mark: ")
        if spot_to_mark[0] not in ["1", "2", "3"] or spot_to_mark[1] not in [
            "1",
            "2",
            "3",
        ]:
            raise RuntimeError("Please enter valid input")

        return spot_to_mark

    def mark_a_spot(self, spot_to_mark) -> list:
        row = int(spot_to_mark[1])
        column = int(spot_to_mark[0])
        self.treasure_map[row - 1][column - 1] = "X"

        return self.treasure_map

    def print_map(self, this_map):
        print(f"\n{this_map[0]}, \n{this_map[1]}, \n{this_map[2]}")


if __name__ == "__main__":
    obj = TreasureMap()
    spot_to_mark = obj.user_input()
    updated_map = obj.mark_a_spot(spot_to_mark)
    obj.print_map(updated_map)
