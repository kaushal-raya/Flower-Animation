from turtle import *

import colorsys


# Set up the turtle environment

speed(0)

bgcolor("black")  # Set the background color to black

h = 0  # Initialize the hue variable


# Create the pattern

for i in range(16):

    for j in range(18):

        c = colorsys.hsv_to_rgb(h, 1, 1)  # Convert HSV to RGB

        color(c)  # Set the turtle color

        h += 0.005  # Increment the hue


        rt(90)  # Turn right 90 degrees

        circle(150 - j * 6, 90)  # Draw a circle segment

        lt(90)  # Turn left 90 degrees

        circle(150 - j * 6, 90)  # Draw another circle segment

        rt(180)  # Turn around


    circle(40, 24)  # Draw a small circle at the end of each iteration


done()