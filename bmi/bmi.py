class Bmi:
    def user_input(self):
        height = input("Enter your height in m: ")
        weight = input("Enter your weight in kg: ")

        return height, weight

    def calculate_bmi(self, height, weight):
        bmi = int(weight) / (float(height) ** 2)  # here I am using exponent operator

        return round(bmi)  # here I am rounding to nearest whole number

    def interpret_bmi(self, bmi):
        if bmi < 18.5:
            print(f"Your BMI is {bmi}, you are underweight.")
        if 18.5 < bmi < 25:
            print(f"Your BMI is {bmi}, you have a normal weight.")
        if 25 < bmi < 30:
            print(f"Your BMI is {bmi}, you are slightly overweight.")
        if 30 < bmi < 35:
            print(f"Your BMI is {bmi}, you are obese.")
        if 35 < bmi:
            print(f"Your BMI is {bmi}, you are clinically obese.")


if __name__ == "__main__":
    obj = Bmi()
    height, weight = obj.user_input()
    calculated_bmi = obj.calculate_bmi(height, weight)
    obj.interpret_bmi(calculated_bmi)
