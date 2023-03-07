class PizzaOrder:
    def user_input(self) -> tuple:
        size = input("Enter pizza size - S, M, or L ")
        pepperoni = input("Add pepperoni - Y or N ")
        extra_cheese = input("Add extra cheese - Y or N ")

        return size, pepperoni, extra_cheese

    def calculate_bill(self, size, pepperoni, extra_cheese) -> int:
        bill = 0
        if size == "S":
            bill = 15
            if pepperoni == "Y":
                bill = bill + 2
        if size == "M":
            bill = 20
            if pepperoni == "Y":
                bill = bill + 3
        if size == "L":
            bill = 25
            if pepperoni == "Y":
                bill = bill + 3
        if extra_cheese == "Y":
            bill = bill + 1

        return bill

    def print_output(self, bill):
        print(f"Your final bill is: ${bill}.")


if __name__ == "__main__":
    obj = PizzaOrder()
    size, pepperoni, extra_cheese = obj.user_input()
    bill = obj.calculate_bill(size, pepperoni, extra_cheese)
    obj.print_output(bill)
