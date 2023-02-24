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

    def leap_year_or_not(self):  # this should return true/false
        pass

    def print_output(self, leap_flag):  # this should have logic to print Leap year or Not leap year
        if leap_flag:
            print("Leap year")
        else:
            print("Not a leap year")


if __name__ == "__main__":
    obj = LeapYear()
    obj.user_input()
