import turtle

def draw_tree(branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0:
        return
    
    # Draw the main branch
    turtle.forward(branch_length)
    
    # Draw left branch
    turtle.left(angle_left)
    draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
    turtle.right(angle_left)  # Return to original position
    
    # Draw right branch
    turtle.right(angle_right)
    draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
    turtle.left(angle_right)  # Return to original position
    
    # Move back to parent branch position
    turtle.backward(branch_length)

def main():
    # Get user inputs
    angle_left = int(input("Enter left branch angle: "))
    angle_right = int(input("Enter right branch angle: "))
    branch_length = int(input("Enter starting branch length: "))
    depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor: "))
    
    # Setup turtle
    turtle.speed("fastest")
    turtle.left(90)  # Point the turtle upwards
    turtle.up()
    turtle.backward(branch_length * 0.5)  # Position turtle at the bottom of the screen
    turtle.down()
    
    # Draw the tree
    draw_tree(branch_length, angle_left, angle_right, depth, reduction_factor)
    
    # Finish
    turtle.done()

if __name__ == "__main__":
    main()


## OUTPUT PROBLEM: the right branch is being drawn from the end of the left branch, not from the main branch's end point.