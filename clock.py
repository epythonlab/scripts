# Digital Clock with Turtle
import turtle
import time

# set up the screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=800,height=600)

# create a turtle for drawing
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color('green')
t.speed(0)
t.pensize(5)

# function to draw the current time
def draw_time(some_turtle,
              time_string):
    some_turtle.clear()
    some_turtle.write(
        time_string,
        align='center',
        font=('Arial',60,'normal')
    )
# continuously update the clock
while True:
    c_time = time.strftime(
        "%H:%M:%S"
    )
    draw_time(t, c_time)
    time.sleep(1)
