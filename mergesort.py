import turtle
import time

# Create a global data array so that all of the functions can access it
data    = []
turtles = []
k = 0

# Global turtle objects used in various functions
screen             = turtle.Screen()
status_writer      = turtle.Turtle()
description_writer = turtle.Turtle()

# Customization settings
STATUS_COLOR      = "black"
DESCRIPTION_COLOR = "gray"
DEFAULT_BAR_COLOR = "gray"
SUBLIST_ONE_COLOR = "crimson"
SUBLIST_TWO_COLOR = "white"
MERGED_LIST_COLOR = "gold"
COMPLETION_COLOR  = "green"
SCREEN_BACKGROUND = "light gray"
SCREEN_BORDER     = 10
BAR_WIDTH         = 10

def Merge(lower_idx, middle_idx, upper_idx):
    sorted_data     = []
    left_iter       = lower_idx
    right_iter      = middle_idx + 1

    WriteDescription("Dividing into sublists...", "gray")

    # Indicate the two sections we are merging by their color
    for idx in range(lower_idx, middle_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], SUBLIST_ONE_COLOR)
        screen.update()
        time.sleep(0.1)
    for idx in range(middle_idx + 1, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], SUBLIST_TWO_COLOR)
        screen.update()
        time.sleep(0.1)
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
    WriteDescription("Merging sublists...", DESCRIPTION_COLOR)

    # Update the bar graph to show the resulting sorted data
    for idx in range(lower_idx, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], MERGED_LIST_COLOR)
        screen.update()
        time.sleep(0.1)
    time.sleep(1)
    for idx in range(lower_idx, upper_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], DEFAULT_BAR_COLOR)
    screen.update()
    time.sleep(1)

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
    t.forward(BAR_WIDTH / 2)
    t.write(str(height))
    t.forward(BAR_WIDTH / 2)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

# Set up the screen for creating the animation
def InitScreen():
    # Creates a title for the screen's window
    screen.title("Merge Sort Algorithm")
    # Sets the height and width of the turtle window
    screen.setup(1000, 700)
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

def BeginSorting():
    # Turn off the onkey property so the sorting is not accidently restarted
    screen.onkey(None, "space")

    # Write the sorting status message to the screen
    WriteStatus("Sorting...", STATUS_COLOR)

    # Start the merge sort algorithm
    MergeSort(0, len(data) - 1)

    # Write the completion status message to the screen
    WriteStatus("Complete", COMPLETION_COLOR)

    # Write a description message to the screen
    WriteDescription("Displaying top " + str(k) + " integers", DESCRIPTION_COLOR)

    # Show the top k integers in the data list
    for idx in range(len(data) - k, len(data)):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], COMPLETION_COLOR)
        screen.update()
        time.sleep(0.1)

def WriteStatus(status_message, color):
    status_writer.clear()
    status_writer.hideturtle()
    status_writer.speed("fastest")
    status_writer.color(color)
    status_writer.penup()
    status_writer.goto((BAR_WIDTH * len(data) + SCREEN_BORDER) / 2, (max(data) + SCREEN_BORDER) / 1.1)
    status_writer.pendown()
    status_writer.write(status_message, False, align="center", font=('Courier', 25, 'bold'))
    status_writer.penup()
    screen.update()

def WriteDescription(description_message, color):
    description_writer.clear()
    description_writer.hideturtle()
    description_writer.speed("fastest")
    description_writer.color(color)
    description_writer.penup()
    description_writer.goto((BAR_WIDTH * len(data) + SCREEN_BORDER) / 2, (max(data) + SCREEN_BORDER) / 1.2)
    description_writer.pendown()
    description_writer.color(color)
    description_writer.write(description_message, False, align="center", font=('Courier', 20, 'bold'))
    description_writer.penup()
    screen.update()

def main():
    # Initialize the global data variables that will be used in various functions
    global data
    global turtles
    global k
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
        DrawBar(franklin, BAR_WIDTH * idx, 0, data[idx], DEFAULT_BAR_COLOR)
        turtles.append(franklin)
    screen.update()

    WriteStatus("Press space to begin sorting", STATUS_COLOR)

    screen.onkey(BeginSorting, "space")
    screen.listen()

    # Keep the turtle screen open until mouse is clicked
    screen.mainloop()

if __name__ == "__main__":
    main()
