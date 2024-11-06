import turtle

# Function to draw a fractal tree
def draw_tree(t, branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(t, branch_len - 7)
        t.left(40)
        draw_tree(t, branch_len - 7)
        t.right(20)
        t.backward(branch_len)

# Main function
def main():
    # Setup
    screen = turtle.Screen()
    #screen.setup(width=2700, height=1300)
    screen.bgcolor("black")

    # Create turtle
    t = turtle.Turtle()
    t.color("green")
    t.speed('fastest')
    t.width(2)
    t.left(90)
    t.up()
    t.backward(350)
    t.down()

    # Draw fractal tree
    draw_tree(t, 100)

    # Hide turtle
    t.hideturtle()

    # Done
    screen.mainloop()

if __name__ == "__main__":
    main()
