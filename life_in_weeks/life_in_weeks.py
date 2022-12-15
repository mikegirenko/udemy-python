"""
Create a program that tells how many days, weeks, and months we have until 90 years old
"""

def calculate_days_left(current_age) -> int:
    days_left = (90 - current_age) * 365

    return days_left


def calculate_weeks_left(current_age) -> int:
    weeks_left = (90 - current_age) * 56

    return weeks_left


def calculate_months_left(current_age) -> int:
    months_left = (90 - current_age) * 12

    return months_left


def life_in_weeks():
    your_current_age = int(input("Enter your current age "))
    days_left = calculate_days_left(your_current_age)
    weeks_left = calculate_weeks_left(your_current_age)
    months_left = calculate_months_left(your_current_age)
    print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


if __name__ == "__main__":
    life_in_weeks()
