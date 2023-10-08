
# Colorful spiral pattern
# Import libraries
import turtle
import random
# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spiral = turtle.Turtle()
spiral.speed(0)
spiral.pensize(2)
# Define colors
colors = ["red", "orange", "yellow",
          "green", "blue", "purple"]
# Create a colorful spiral
for _ in range(72):
    spiral.color(random.choice(colors))
    spiral.forward(100)
    spiral.right(30)
    spiral.forward(20)
    spiral.left(60)
    spiral.forward(50)
    spiral.right(30)
    spiral.penup()
    spiral.setposition(0, 0)
    spiral.pendown()
    spiral.right(5)
# Hide the turtle
spiral.hideturtle()
# Close the window on click
screen.exitonclick()




