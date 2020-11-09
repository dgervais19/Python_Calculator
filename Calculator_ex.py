# Creating our Calculator class
class Calculator:

    def __init__(self):
        # We do not need any variables within __init__
        print("Welcome!")

# Create the appropriate calculator schedule
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:  # You cannot divide by zero
            return "Please divide by a number other than 0"
        else:
            return num1 / num2

    def modulo(self, num1, num2):
        if num2 == 0:
            return "Please divide by a number other than 0"
        else:
            return num1 % num2

    def divisible(self, num1, num2):
        if self.modulo(num1, num2) == 0:
            return True
        else:
            return False

    def triangle_area(self, base, height):
        return base * height * 0.5

    def inch_to_cm(self, num_inches):
        return self.multiply(num_inches, 2.54)

# Create our object for the calculator class so that we can test our calculator
calculator = Calculator()
print(calculator.add(4, 7))
print(calculator.subtract(10, 5))
print(calculator.multiply(3, 9))
print(calculator.divide(12, 4))
print(calculator.divide(12, 0))
print(calculator.modulo(30, 7))
print(calculator.divisible(30, 6))
print(calculator.triangle_area(4, 6))
print(calculator.inch_to_cm(6))

