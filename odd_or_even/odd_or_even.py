class OddOrEven:

    def determine_odd_or_even(self, given_number):
        odd_or_even = ""
        if int(given_number) % 2 == 0:
            odd_or_even = "even number"
        if int(given_number) % 2 != 0:
            odd_or_even = "odd number"

        return odd_or_even


if __name__ == "__main__":
    user_input = input("Which number do you want to check? ")
    obj = OddOrEven()
    number_to_check = obj.determine_odd_or_even(user_input)
    print(f"This is an {number_to_check}.")
