import math

class Triangle:
    def __init__(self, a, b, c):
        # Initialize side lengths
        self.a = a
        self.b = b
        self.c = c

    def Is_valid(self):
        """Check if the triangle is valid."""
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return "Valid"
        else:
            return "Invalid"
    
    def Side_Classification(self):
        """Classify the triangle based on the side lengths."""
        if self.Is_valid() == "Invalid":
            return "Invalid"
        
        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isosceles"
        else:
            return "Scalene"
    
    def Angle_Classification(self):
        """Classify the triangle based on its angles using Pythagorean theorem."""
        if self.Is_valid() == "Invalid":
            return "Invalid"
        
        # Sort sides so that a <= b <= c
        sides = sorted([self.a, self.b, self.c])
        a, b, c = sides
        
        if a**2 + b**2 > c**2:
            return "Acute"
        elif a**2 + b**2 == c**2:
            return "Right"
        else:
            return "Obtuse"
    
    def Area(self):
        """Calculate the area of the triangle using Heron's formula."""
        if self.Is_valid() == "Invalid":
            return "Invalid"
        
        # Semi-perimeter
        s = (self.a + self.b + self.c) / 2
        # Heron's formula for the area
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

# Taking user input for the sides of the triangle
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))

# Create a Triangle object with the given side lengths
T = Triangle(a, b, c)

# Print the results for each method
print(T.Is_valid())             # Check if the triangle is valid
print(T.Side_Classification())  # Classify by sides
print(T.Angle_Classification()) # Classify by angles
print(T.Area())                # Calculate the area
