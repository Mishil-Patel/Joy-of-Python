from turtle import *

# Define the colors for the gradient
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
num_colors = len(colors)

# RGB values for the colors
color_values = {
    'red': (255, 0, 0),
    'purple': (128, 0, 128),
    'blue': (0, 0, 255),
    'green': (0, 128, 0),
    'orange': (255, 165, 0),
    'yellow': (255, 255, 0)
}

# Function to interpolate between colors
def interpolate_color(color1, color2, t):
    r1, g1, b1 = color_values[color1]
    r2, g2, b2 = color_values[color2]

    # Interpolate the RGB values
    r = int(r1 * (1 - t) + r2 * t)
    g = int(g1 * (1 - t) + g2 * t)
    b = int(b1 * (1 - t) + b2 * t)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# Set up the screen
bgcolor('black')
speed(0)
hideturtle()

# Iterate over each step of the pattern
for i in range(360 * 4):
    # Calculate the index of the current color and the next color
    color_index1 = i % num_colors
    color_index2 = (i + 1) % num_colors

    # Interpolate between the two colors
    t = i % 360 / 360
    current_color = interpolate_color(colors[color_index1], colors[color_index2], t)

    # Set the pen color to the interpolated color
    pencolor(current_color)

    # Adjust pen size and move forward
    pensize(1 + i / 100)
    forward(i / 5)
    left(59.8)

# Done drawing
done()
