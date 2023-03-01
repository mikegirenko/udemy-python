"""
pseudocode (english words instead of code)
1. take user input
2. determine if leap year or not
3. print formatted output to user
"""


class LeapYear:
    def user_input(self) -> int:
        year = input("Which year do you want to check? ")

        return int(year)

    def leap_year_or_not(self, year_to_check) -> bool:
        leap = False
        if year_to_check % 4 != 0:
            leap = False
        if year_to_check % 4 == 0:
            if year_to_check % 100 != 0 or year_to_check % 400 == 0:
                leap = True

        return leap

    def print_output(self, leap_flag):
        if leap_flag:
            print("Leap year.")
        else:
            print("Not a leap year.")


if __name__ == "__main__":
    obj = LeapYear()
    year = obj.user_input()
    flag = obj.leap_year_or_not(year)
    obj.print_output(flag)
