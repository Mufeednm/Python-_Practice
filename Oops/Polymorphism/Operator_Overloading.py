class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating two Vector2D objects
v1 = Vector2D(2, 3)
v2 = Vector2D(1, 5)

# Adding two vectors
result_addition = v1 + v2
print("Addition:", result_addition)  # Output: (3, 8)

# Subtracting two vectors
result_subtraction = v1 - v2
print("Subtraction:", result_subtraction)  # Output: (1, -2)

# Multiplying a vector by a scalar
result_multiplication = v1 * 2
print("Multiplication:", result_multiplication)  # Output: (4, 6)
