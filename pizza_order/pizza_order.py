
class PizzaOrder:
    def user_input(self) -> tuple:
        size = input("Enter pizza size - S, M, or L ")
        pepperoni = input("Add pepperoni - Y or N ")
        cheese = input("Add extra cheese - Y or N ")

        return size, pepperoni, cheese


    def calculate_bill(self, size, pepperoni, cheese) -> int:
        bill = 0
        if size == "S":
            bill = 15
        if size == "M":
            bill = 20
        if size == "L":
            bill = 25

        return bill


    def print_output(self, bill):
        print(f"Your final bill is: ${bill}.")


if __name__ == "__main__":
    obj = PizzaOrder()
    print("printing", obj.user_input())
    obj.print_output(28)
