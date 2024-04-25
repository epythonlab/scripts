# @epthonlab on Telegram
# Happy new year, 20024

import time 
import random 
import turtle

screen_width = 600
screen_height = 400

def draw_star(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.dot(size, color)
    
def draw_digit(digit, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('white')
    t.write(digit, font=("rial", size, "normal"))
    
def draw_text(text, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.write(text, align="center",
            font=("Arial", size, "normal"))

screen = turtle.Screen()
screen.setup(width=screen_width,
             height=screen_height)
screen.bgcolor("midnightblue")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

for _ in range(100):
    draw_star(random.randint(-300,300),
              random.randint(-200, 200),
              random.randint(2, 6), 'white')
    
time.sleep(0.5)
draw_digit("2", -50, 0, 36)
time.sleep(0.5)
draw_digit("0", 0, 0, 36)
time.sleep(0.5)
draw_digit("2", 50, 0, 36)
time.sleep(0.5)
draw_digit("4", 100, 0, 36)

time.sleep(0.5)

draw_text("HAPPY NEW YEAR!", 0, -50, 18)

screen.exitonclick()