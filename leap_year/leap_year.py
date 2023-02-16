"""
read then write pseudocode (english words instead of code)
1. take user input
2. determine if leap year or not
3. print formatted output to user
"""


class LeapYear:
    def user_input(self) -> int:
        year = input("Which year do you want to check? ")

        return year

    def leap_year_or_not(self):
        pass


if __name__ == "__main__":
    obj = LeapYear()
    obj.user_input()
