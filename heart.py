"""
Draw heart using Turtle
"""
import turtle

def draw_heart():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(224)
    turtle.end_fill()
   

if __name__ == "__main__":
    draw_heart()
    turtle.bgcolor("black")
    turtle.done()
