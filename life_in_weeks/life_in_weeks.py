"""
Create a program that tells how many days, weeks, and months we have until 90 years old
"""


def life_in_weeks():
    your_current_age = input("Enter your current age ")
    days_left = (90 - int(your_current_age)) * 365
    weeks_left = (90 - int(your_current_age)) * 56
    months_left = (90 - int(your_current_age)) * 12
    print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


if __name__ == "__main__":
    life_in_weeks()
