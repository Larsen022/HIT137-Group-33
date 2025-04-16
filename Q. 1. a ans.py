def can_form_triangle(a, b, c):
    # Sum of any two sides must be greater than the third
    return a + b > c and a + c > b and b + c > a

# Get user input and convert it to float
side1 = float(input("Enter the first side: "))      # Prompt user for first side length
side2 = float(input("Enter the second side: "))     # Prompt user for second side length
side3 = float(input("Enter the third side: "))      # Prompt user for third side length

# Check if it forms a triangle
if can_form_triangle(side1, side2, side3):
    print("Yes, these three lengths can form a triangle.")
else:
    print("No, these three lengths cannot form a triangle.")
    ifelse
    print("wrong command")

#yes I can
# No i cant

