import turtle
from random import choice

# Function to draw a colorful spiral
def draw_spiral(t, num_circles, initial_radius, spacing):
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']
    for _ in range(num_circles):
        t.color(choice(colors))  # Randomly select a color
        t.circle(initial_radius + spacing * _)  # Draw a circle with increasing radius
        t.left(10)  # Rotate the turtle slightly

# Main function
def main():
    # Setup
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")

    # Create turtle
    t = turtle.Turtle()
    t.width(2)
    t.speed('fastest')  # Set drawing speed to fastest
    t.hideturtle()

    # Adjust turtle position
    t.up()
    t.goto(0, -250)
    t.down()

    # Draw colorful spiral
    draw_spiral(t, 36, 5, 5)

    # Done
    screen.mainloop()

if __name__ == "__main__":
    main()
