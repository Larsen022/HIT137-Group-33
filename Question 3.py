import turtle

def draw_tree(branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0:
        return

    # Change color and pen size depending on depth
    if depth == initial_depth:
        turtle.color("brown")
        turtle.pensize(10)
    else:
        turtle.color("green")
        turtle.pensize(max(1, depth))  # Decrease pen size as it branches

    turtle.forward(branch_length)

    # Saving the turtle’s current state so that we can return to this exact point later
    current_position = turtle.position()
    current_heading = turtle.heading()

    # Draw left branch
    turtle.left(angle_left)
    draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    # Restore and draw right branch
    turtle.setposition(current_position)
    turtle.setheading(current_heading)
    turtle.right(angle_right)
    draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    # Restore to previous state
    turtle.setposition(current_position)
    turtle.setheading(current_heading)
    turtle.backward(branch_length)

def main():
    global initial_depth

    # Get user inputs
    angle_left = float(input("Enter left branch angle (in degrees): "))
    angle_right = float(input("Enter right branch angle (in degrees): "))
    branch_length = float(input("Enter starting branch length (in pixels): "))
    initial_depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))

    # Setup turtle
    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.left(90)         # Point the turtle upwards
    turtle.penup()
    turtle.goto(0, -250)    # Position turtle at the bottom of the screen
    turtle.pendown()

    draw_tree(branch_length, angle_left, angle_right, initial_depth, reduction_factor)

    turtle.done()

if __name__ == "__main__":
    main()
    
## FINAL CODE
