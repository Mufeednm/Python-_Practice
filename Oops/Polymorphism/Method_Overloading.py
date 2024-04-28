class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Create an instance of Calculator
calc = Calculator()

# This will call the second add method, effectively overriding the first one.
print(calc.add(2, 3, 4))  # Output: 9
