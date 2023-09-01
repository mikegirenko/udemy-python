"""
Write a program which play FizzBuzz game.
Print each number from 1 to 100.
If number divisible by 3, print Fizz
If number divisible by 5, print Buzz
If number divisible by 3 and 5 (e.g. 15), print FizzBuzz
"""


class FizzBuzz:
    def __init__(self):
        self.some_variable = None  # can do _ to make it private variable

    def play_fizz_buzz(self):
        for i in range(1, 101):
            if i % 3 != 0 and i % 5 != 0:
                print(i)
            if i % 3 == 0 and i % 5 != 0:
                print("Fizz")
            if i % 5 == 0 and i % 3 != 0:
                print("Buzz")
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")


if __name__ == "__main__":
    obj = FizzBuzz()
    obj.play_fizz_buzz()
    print("Class variable is", obj.some_variable)
