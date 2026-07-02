import turtle

screen = turtle.Screen()
screen.title("2D Floor Plan")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Function to draw a room
def draw_room(x, y, width, height, name):
    t.penup()
    t.goto(x, y)
    t.pendown()

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.penup()
    t.goto(x + width/4, y + height/2)
    t.write(name, font=("Arial", 12, "bold"))

# Draw rooms
draw_room(-200, 0, 150, 120, "Bedroom 1")
draw_room(-50, 0, 150, 120, "Bedroom 2")
draw_room(-200, -150, 250, 120, "Living Room")
draw_room(100, -150, 100, 80, "Kitchen")
draw_room(100, -70, 100, 70, "Bathroom")

t.hideturtle()

screen.mainloop()