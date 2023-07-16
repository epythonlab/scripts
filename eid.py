import turtle

def draw_eid_mubarak():
    turtle.speed("slowest")  # Set the drawing speed (optional)

    # Create turtle screen
    screen = turtle.Screen()
    screen.bgcolor("gold")  # Set the background color to gold

    # Draw "Eid"
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.color("darkblue")  # Set the text color to dark blue
    turtle.write("Eid", font=("Arial", 60, "bold"))
    
    # Draw "Mubarak"
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()
    turtle.color("darkblue")  # Set the text color to dark blue
    turtle.write("Mubarak!", font=("Arial", 60, "bold"))

    turtle.done()

if __name__ == "__main__":
    draw_eid_mubarak()
