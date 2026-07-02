import turtle

screen = turtle.Screen()
screen.title("Mechanical Drawing - Flange")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Draw a circle
def draw_circle(radius):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)

# Outer flange
draw_circle(100)

# Inner hole
draw_circle(40)

# Bolt holes
positions = [
    (70, 0),
    (0, 70),
    (-70, 0),
    (0, -70)
]

for x, y in positions:
    t.penup()
    t.goto(x, y - 10)
    t.pendown()
    t.circle(10)

# Labels
t.penup()
t.goto(-50, 130)
t.write("Front View of Flange", font=("Arial", 14, "bold"))

t.hideturtle()

screen.mainloop()