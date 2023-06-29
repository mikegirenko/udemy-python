"""
Write a program which calculates average height from a list of heights
It can be calculated by adding all the heights and dividing by number of heights
When calculated, it should be rounded to nearest whole number
"""


class AverageHeight:
    def user_input(self):
        list_of_heights = []
        good_input = True
        while good_input:
            user_input = input("Input a list of student heights: ")
            if user_input == "":
                user_input = input("Input a list of student heights: ")
            else:
                good_input = False
        temp_list = user_input.split(",")
        for item in temp_list:
            list_of_heights.append(int(item))

        return list_of_heights

    def calculate_average_height(self, list_of_heights):
        all_heights = 0
        number_of_heights = 0
        for count_of_heights in list_of_heights:
            number_of_heights += 1
        for height in list_of_heights:
            all_heights += height
        average_height = all_heights / number_of_heights

        return round(average_height)


if __name__ == "__main__":
    obj = AverageHeight()
    list_to_calculate = obj.user_input()
    print("Average student height is", obj.calculate_average_height(list_to_calculate))
