"""
Program which will calculate a sum of all even numbers from 1 to 100.
Print final total, not every step of calculation
"""


class AddEvenNumbers:
    def add_even_numbers(self):
        total = 0
        all_numbers = []
        even_numbers = []
        for i in range(1, 101):
            all_numbers.append(i)
        for number in all_numbers:
            if number % 2 == 0:
                even_numbers.append(number)
        for even_number in even_numbers:
            total += even_number

        return total


if __name__ == "__main__":
    obj = AddEvenNumbers()
    total = obj.add_even_numbers()
    print(f"Total is {total}")
