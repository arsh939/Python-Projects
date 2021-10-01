import turtle
pen = turtle.Turtle()

# initial length of the square-like shapes
size = 50

# Changing shape of the turtle
pen.shape("turtle")

# Changing Background color
turtle.bgcolor("blue")

# Changing color of the pen
pen.color("yellow")

# Increasing speed of the pen
pen.speed(100)

# Running a loop with 300 iterations
for i in range(300):
    # after 200 white squares change the color
    if i==200:
        pen.color("white")
    # moving the pen in forward direction
    pen.forward(size)
    # rotating the pen
    pen.left(89)
    # increasing the length
    size+=1
