import turtle
import time

# Create a global data array so that all of the functions can access it
data    = []
turtles = []
k = 0

# Variables used to customize the screen
screen    = turtle.Screen()
writer    = turtle.Turtle()
border    = 10
bar_width = 10

def Merge(lower_idx, middle_idx, upper_idx):
    sorted_data     = []
    left_iter       = lower_idx
    right_iter      = middle_idx + 1

    description = turtle.Turtle()
    description.hideturtle()
    description.speed("fastest")
    description.penup()
    description.goto((bar_width * len(data) + border) / 2, (max(data) + border) / 1.2)
    description.pendown()
    description.color("gray")
    description.write("Dividing into sublists...", False, align="center", font=('Courier', 20, 'bold'))
    description.penup()
    screen.update()

    # Indicate the two sections we are merging by their color
    for idx in range(lower_idx, middle_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], bar_width * idx, 0, data[idx], "crimson")
        screen.update()
        time.sleep(0.2)
    for idx in range(middle_idx + 1, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], bar_width * idx, 0, data[idx], "white")
        screen.update()
        time.sleep(0.2)
    time.sleep(1)

    # Compare elements from either side of the array and add the smaller one to the
    # sorted array
    while left_iter <= middle_idx and right_iter <= upper_idx:
        if data[left_iter] <= data[right_iter]:
            sorted_data.append(data[left_iter])
            left_iter += 1
        else:
            sorted_data.append(data[right_iter])
            right_iter += 1

    # Add any leftover values from the left side of the array to the sorted array
    while left_iter <= middle_idx:
        sorted_data.append(data[left_iter])
        left_iter += 1
    # Add any leftover values from the right side of the array to the sorted array
    while right_iter <= upper_idx:
        sorted_data.append(data[right_iter])
        right_iter += 1

    # Copy the sorted integers back into the data array
    for idx in range(len(sorted_data)):
        data[lower_idx + idx] = sorted_data[idx]

    # Provide a description letting the user know the two sublists are being merged
    description.clear()
    description.goto((bar_width * len(data) + border) / 2, (max(data) + border) / 1.2)
    description.pendown()
    description.color("gray")
    description.write("Merging sublists...", False, align="center", font=('Courier', 20, 'bold'))
    description.penup()
    screen.update()

    # Update the bar graph to show the resulting sorted data
    for idx in range(lower_idx, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], bar_width * idx, 0, data[idx], "gold")
        screen.update()
        time.sleep(0.2)
    time.sleep(1)
    for idx in range(lower_idx, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], bar_width * idx, 0, data[idx], "gray")
    screen.update()
    time.sleep(1)

    # Clear the description message
    description.clear()

# Recursive function to sort sections of the array
def MergeSort(lower_idx, upper_idx):
    if lower_idx >= upper_idx:
        return
    middle_idx = (lower_idx + upper_idx) // 2
    MergeSort(lower_idx, middle_idx)
    MergeSort(middle_idx + 1, upper_idx)
    Merge(lower_idx, middle_idx, upper_idx)

# Draws a bar assuming the turtle is facing east
def DrawBar(t, x, y, height, color):
    t.fillcolor(color)
    t.setheading(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(bar_width / 2)
    t.write(str(height))
    t.forward(bar_width / 2)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

# Set up the screen for creating the animation
def InitScreen():
    # Sets the height and width of the turtle window
    screen.setup(1000, 700)
    # Turns of the screen's auto update feature
    screen.tracer(0)
    # Sets the screens background color
    screen.bgcolor("light grey")
    # Sets the coordinates within the window using the bottom left and
    # upper right coordinates
    screen.setworldcoordinates(0 - border,
                               0,
                               bar_width * len(data) + border,
                               max(data) + border)
    # Creates a title for the screen's window
    screen.title("Merge Sort Algorithm")

def BeginSorting():
    # Write the sorting status message to the screen
    screen.onkey(None, "space")
    writer.clear()
    writer.goto((bar_width * len(data) + border) / 2, (max(data) + border) / 1.1)
    writer.pendown()
    writer.write("Sorting...", False, align="center", font=('Courier', 25, 'bold'))
    writer.penup()

    # Start the merge sort algorithm
    MergeSort(0, len(data) - 1)

    # Write the completion status message to the screen
    writer.clear()
    writer.goto((bar_width * len(data) + border) / 2, (max(data) + border) / 1.1)
    writer.pendown()
    writer.color("green")
    writer.write("Complete", False, align="center", font=('Courier', 25, 'bold'))
    writer.penup()

    # Write a description message to the screen
    description = turtle.Turtle()
    description.hideturtle()
    description.speed("fastest")
    description.penup()
    description.goto((bar_width * len(data) + border) / 2, (max(data) + border) / 1.2)
    description.pendown()
    description.color("gray")
    description.write("Displaying top " + str(k) + " integers", False, align="center", font=('Courier', 20, 'bold'))
    description.penup()
    screen.update()

    # Show the top k integers in the data list
    for idx in range(len(data) - k, len(data)):
        turtles[idx].clear()
        DrawBar(turtles[idx], bar_width * idx, 0, data[idx], "green")
        screen.update()
        time.sleep(0.2)

def main():
    # Must be included to edit the global variables
    global data
    global turtles
    global writer
    global k

    # Store the comma seperated list of integers into the global array
    data_string = input()
    k = int(input())
    data_string_array = data_string.split(',')
    data = [int(x) for x in data_string_array]

    # Initialize the turtle's screen
    InitScreen()

    # Create the initial bar graph using the data list
    for idx in range(len(data)):
        franklin = turtle.Turtle()
        franklin.pensize(3)
        franklin.hideturtle()
        franklin.speed("fastest")
        DrawBar(franklin, bar_width * idx, 0, data[idx], "gray")
        turtles.append(franklin)
    screen.update()

    writer.hideturtle()
    writer.speed("fastest")
    writer.penup()
    writer.goto((bar_width * len(data) + border) / 2, (max(data) + border) / 1.1)
    writer.pendown()
    writer.write("Press space to begin sorting", False, align="center", font=('Courier', 25, 'bold'))
    writer.penup()

    screen.onkey(BeginSorting, "space")
    screen.listen()

    # Keep the turtle screen open until mouse is clicked
    screen.mainloop()

if __name__ == "__main__":
    main()
