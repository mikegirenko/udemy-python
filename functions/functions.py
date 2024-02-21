test_h = int(input("Enter height: "))  # Height of wall (m)
test_w = int(input("Enter width: "))  # Width of wall (m)
coverage = 5


def paint_calc(height=0, width=0, cover=0):
    number_of_cans = (height * width) / cover

    return round(number_of_cans)


print(paint_calc(height=test_h, width=test_w, cover=coverage))
