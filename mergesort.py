import turtle
import time

# Global data variables used in various functions
data = []
turtles = []
k = 0
bar_coloring_speed = 0
pause_length = 0

# Global turtle objects used in various functions
screen = turtle.Screen()
status_writer = turtle.Turtle()
description_writer = turtle.Turtle()
legend_writer = turtle.Turtle()

# Customization settings
STATUS_COLOR = "black"
DESCRIPTION_COLOR = "gray"
DEFAULT_BAR_COLOR = "gray"
SUBLIST_ONE_COLOR = "crimson"
SUBLIST_TWO_COLOR = "white"
MERGED_LIST_COLOR = "gold"
COMPLETION_COLOR = "green"
SCREEN_BACKGROUND = "light gray"
SCREEN_BORDER = 10
BAR_WIDTH = 10
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
BOX_WIDTH = 10
BOX_HEIGHT = 2

def Merge(lower_idx, middle_idx, upper_idx):
    sorted_data = []
    left_iter = lower_idx
    right_iter = middle_idx + 1

    WriteDescription("Dividing into sublists...", DESCRIPTION_COLOR)

    # Indicate the two sections we are merging by their color
    for idx in range(lower_idx, middle_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], SUBLIST_ONE_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
    for idx in range(middle_idx + 1, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], SUBLIST_TWO_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
    time.sleep(pause_length)

    # Compare elements from either side of the array and add the smaller one to the
    # sorted array
    while left_iter <= middle_idx and right_iter <= upper_idx:
        # Draw the current position of left_iter and right_iter
        DrawBar(turtles[left_iter], BAR_WIDTH * left_iter, 0, data[left_iter], 'red')
        DrawBar(turtles[right_iter], BAR_WIDTH * right_iter, 0, data[right_iter], 'blue')
        screen.update()
        time.sleep(bar_coloring_speed)
        if data[left_iter] <= data[right_iter]:
            sorted_data.append(data[left_iter])
            left_iter += 1
            DrawBar(turtles[left_iter-1], BAR_WIDTH * (left_iter-1), 0, data[left_iter-1], DEFAULT_BAR_COLOR)
        else:
            sorted_data.append(data[right_iter])
            right_iter += 1
            DrawBar(turtles[right_iter-1], BAR_WIDTH * (right_iter-1), 0, data[right_iter-1], DEFAULT_BAR_COLOR)

    # Add any leftover values from the left side of the array to the sorted array
    while left_iter <= middle_idx:
        DrawBar(turtles[left_iter], BAR_WIDTH * left_iter, 0, data[left_iter], 'red')
        screen.update()
        sorted_data.append(data[left_iter])
        left_iter += 1
        DrawBar(turtles[left_iter-1], BAR_WIDTH * (left_iter-1), 0, data[left_iter-1], DEFAULT_BAR_COLOR)
    # Add any leftover values from the right side of the array to the sorted array
    while right_iter <= upper_idx:
        DrawBar(turtles[right_iter], BAR_WIDTH * right_iter, 0, data[right_iter], 'blue')
        screen.update()
        sorted_data.append(data[right_iter])
        right_iter += 1
        DrawBar(turtles[right_iter-1], BAR_WIDTH * (right_iter-1), 0, data[right_iter-1], DEFAULT_BAR_COLOR)

    # Copy the sorted integers back into the data array
    for idx in range(len(sorted_data)):
        data[lower_idx + idx] = sorted_data[idx]

    # Provide a description letting the user know the two sublists are being merged
    WriteDescription("Merging sublists...", DESCRIPTION_COLOR)

    # Update the bar graph to show the resulting sorted data
    for idx in range(lower_idx, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], MERGED_LIST_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
    time.sleep(pause_length)
    for idx in range(lower_idx, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], DEFAULT_BAR_COLOR)
    screen.update()
    time.sleep(pause_length)

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
    #t.setheading(0)
    t.penup()
    t.goto(x, y + 5)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(height/2)
    t.right(90)
    t.forward(BAR_WIDTH / 2)
    t.write(str(height))
    t.forward(BAR_WIDTH / 2)
    t.right(90)
    t.forward(height/2)
    t.right(90)
    t.forward(BAR_WIDTH)
    t.end_fill()
    t.left(180)
    t.forward(BAR_WIDTH)
    
# Draws Box for subarrays  
def DrawBox(t, x, y, height, color):
    # Set up number the number of the box
    t.penup()
    t.goto(x, y + 1)
    t.forward(BOX_WIDTH/2.2)
    t.left(90)
    t.forward(BOX_HEIGHT/3)
    t.right(90)
    t.write(str(height))
    t.right(180)
    t.forward(BOX_WIDTH/2.2)
    t.left(90)
    t.forward(BOX_HEIGHT/3)
    t.left(90)
    # Create the Box
    t.pendown()
    t.forward(BOX_WIDTH)
    t.left(90)
    t.forward(2)
    t.left(90)
    t.forward(BOX_WIDTH)
    t.left(90) 
    t.forward(2)
    t.left(90) 

# Set up the screen for creating the animation

def InitScreen():
    # Creates a title for the screen's window
    screen.title("Merge Sort Algorithm")
    # Sets the height and width of the turtle window
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    # Sets the screens background color
    screen.bgcolor(SCREEN_BACKGROUND)
    # Turns of the screen's auto update feature
    screen.tracer(0)
    # Sets the coordinates within the window using the bottom left and
    # upper right coordinates
    screen.setworldcoordinates(0 - SCREEN_BORDER,
                               0,
                               BAR_WIDTH * len(data) + SCREEN_BORDER,
                               max(data) + SCREEN_BORDER)


def SetSpeedOne():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.1
    pause_length = 1
    BeginSorting()


def SetSpeedTwo():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.05
    pause_length = 0.5
    BeginSorting()


def SetSpeedThree():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.025
    pause_length = 0.25
    BeginSorting()


def BeginSorting():
    # Turn off the onkey property so the sorting is not accidently restarted
    screen.onkey(None, "1")
    screen.onkey(None, "2")
    screen.onkey(None, "3")

    # Write the sorting status message to the screen
    WriteStatus("Sorting...", STATUS_COLOR)

    # D
    DrawLegend(STATUS_COLOR)

    # Start the merge sort algorithm
    MergeSort(0, len(data) - 1)

    # Write the completion status message to the screen
    WriteStatus("Complete", COMPLETION_COLOR)

    # Write a description message to the screen
    WriteDescription("Displaying top " + str(k) +
                     " integers", DESCRIPTION_COLOR)

    # Show the top k integers in the data list
    for idx in range(len(data) - k, len(data)):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], COMPLETION_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)


def WriteStatus(status_message, color):
    status_writer.clear()
    status_writer.hideturtle()
    status_writer.speed("fastest")
    status_writer.color(color)
    status_writer.penup()
    status_writer.goto((BAR_WIDTH * len(data)) / 2,
                       (max(data) + SCREEN_BORDER) / 1.1)
    status_writer.pendown()
    status_writer.write(status_message, False, align="center",
                        font=('Courier', 25, 'bold'))
    status_writer.penup()
    screen.update()


def LegendLabel(color, position, label):

    # Draw label
    legend_writer.goto((5) /
                       2, (max(data) + SCREEN_BORDER) / position)
    status_writer.pendown()
    legend_writer.write(label, False, align="left",
                        font=('Courier', 14))
    legend_writer.penup()

    # Draw color
    legend_writer.goto((75) /
                       2, 1 + (max(data) + SCREEN_BORDER) / position)
    legend_writer.fillcolor(color)
    legend_writer.begin_fill()
    legend_writer.forward(10)
    legend_writer.right(90)
    legend_writer.forward(1)
    legend_writer.right(90)
    legend_writer.forward(10)
    legend_writer.right(90)
    legend_writer.forward(1)
    legend_writer.right(90)
    legend_writer.end_fill()


def DrawLegend(color):
    legend_writer.clear()
    legend_writer.hideturtle()
    legend_writer.speed("fastest")
    legend_writer.color(color)
    legend_writer.penup()

    # Draw legend square
    legend_writer.goto((0) /
                       2, (max(data) + SCREEN_BORDER) / 1.01)
    legend_writer.pendown()
    legend_writer.width(4)
    legend_writer.forward(50)  # Forward turtle by 50 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(7.5)  # Forward turtle by 7 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(50)  # Forward turtle by 50 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(7.5)  # Forward turtle by 7 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.penup()

    # Draw legend Title
    legend_writer.goto((50) /
                       2, (max(data) + SCREEN_BORDER) / 1.07)
    status_writer.pendown()
    legend_writer.write("Legend", False, align="center",
                        font=('Courier', 15, 'bold'))
    legend_writer.penup()

    # Draw legend labels
    LegendLabel(SUBLIST_ONE_COLOR, 1.125, "Left Sublist")
    LegendLabel(SUBLIST_TWO_COLOR, 1.1875, "Right Sublist")
    LegendLabel(MERGED_LIST_COLOR, 1.25, "Merged List")
    LegendLabel(COMPLETION_COLOR, 1.325, "Top " + str(k) + " Integers")
    screen.update()


def WriteDescription(description_message, color):
    description_writer.clear()
    description_writer.hideturtle()
    description_writer.speed("fastest")
    description_writer.color(color)
    description_writer.penup()
    description_writer.goto((BAR_WIDTH * len(data)) / 2,
                            (max(data) + SCREEN_BORDER) / 1.2)
    description_writer.pendown()
    description_writer.color(color)
    description_writer.write(description_message, False,
                             align="center", font=('Courier', 20, 'bold'))
    description_writer.penup()
    screen.update()


def main():
    # Initialize the global data variables that will be used in various functions
    global data
    global turtles
    global k
    file = open("unsorted_input.txt", "r")
    data_string = file.readline()
    k = int(file.readline())
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
        DrawBar(franklin, BAR_WIDTH * idx, 0, data[idx], DEFAULT_BAR_COLOR)
        turtles.append(franklin)
    screen.update()

    WriteStatus("Select a speed to begin sorting 1, 2, 3", STATUS_COLOR)
    screen.onkey(SetSpeedOne, "1")
    screen.onkey(SetSpeedTwo, "2")
    screen.onkey(SetSpeedThree, "3")
    screen.listen()

    # Keep the turtle screen open until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()
