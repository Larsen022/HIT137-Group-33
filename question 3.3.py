import turtle

def draw_tree(branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0:
        return

    # Draw the main branch
    turtle.forward(branch_length)

    # Saving the turtle’s current state so that we can return to this exact point later
    current_position = turtle.position()
    current_heading = turtle.heading()

    # Draw left branch
    turtle.left(angle_left)
    draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    # Restore position and heading before drawing right branch
    turtle.setposition(current_position)
    turtle.setheading(current_heading)

    # Draw right branch
    turtle.right(angle_right)
    draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    # Move back to the parent branch base
    turtle.setposition(current_position)
    turtle.setheading(current_heading)
    turtle.backward(branch_length)

def main():
    # Get user inputs
    angle_left = float(input("Enter left branch angle (in degrees): "))
    angle_right = float(input("Enter right branch angle (in degrees): "))
    branch_length = float(input("Enter starting branch length (in pixels): "))
    depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))

    # Setup turtle
    turtle.speed("fastest")
    turtle.left(90)         # Point the turtle upwards
    turtle.penup()
    turtle.goto(0, -250)    # Position turtle at the bottom of the screen
    turtle.pendown()
    turtle.color("green")

    # Draw the initial trunk and start branching from there
    draw_tree(branch_length, angle_left, angle_right, depth, reduction_factor)

    # Wait for user to close the window
    turtle.done()

if __name__ == "__main__":
    main()