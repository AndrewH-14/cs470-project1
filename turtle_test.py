# Python program to draw a turtle
import turtle

# Function that draws the turtle
def drawBar(t, height, color):

    # Get turtle t to draw one bar
    # of height

    # Start filling this shape
    t.fillcolor(color)
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)

    # stop filling the shape
    t.end_fill()

# Driver Code

xs = [48, 117, 200, 96, 134, 260, 99]
clrs = ["green", "red", "yellow", "black",
        "pink", "brown", "blue"]

maxheight = max(xs)
numbers = len(xs)
border = 10

# Set up the window and its
# attributes
wn = turtle.Screen()
wn.setworldcoordinates(0 - border, 0 - border,
                       40 * numbers + border,
                       maxheight + border)

# Create tess and set some attributes
tess = turtle.Turtle()
tess.pensize(3)
tess.speed(0)

for i in range(len(xs)):

    drawBar (tess, xs[i],
             clrs[i])

wn.exitonclick()