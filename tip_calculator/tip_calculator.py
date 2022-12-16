"""
How much each person will pay if bill was $150.00, split between 5 people,
with 12% tip
"""


def calculate_tip(bill, number_of_people, tip_in_percents) -> str:
    tip_in_dollars = tip_in_percents * (bill / 100)
    total_with_tip = bill + tip_in_dollars
    each_person_pay = total_with_tip / number_of_people

    return "{:.2f}".format(each_person_pay)
    # return round(each_person_pay, 2)  # not sure why it still returns 33.6


calculated_each_person_pay = calculate_tip(150, 5, 12)
print(f"Each person will pay ${calculated_each_person_pay}")
