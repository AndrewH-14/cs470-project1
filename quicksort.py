# Created By: Andrew Hankins, Joey Walker, Brandon Jones, Robert Melton, and Luke Roberts
import random
import turtle
import time

# Create a global data array so that all the functions can access it
all_input_nums = [22,15,6,13,23,41,12,24,8,2,48,19,45,28,21,25,32,44,11,27,33,1,37,20,9,14,5,36,50,47,34,17,29,7,31,16,4,39,43,10,38,3,35,30,42,18,40,26,46,49]
turtles = []
k_val = 3
bar_coloring_speed = 0
pause_length = 0

# Global turtle objects used in various functions
screen = turtle.Screen()
status_writer = turtle.Turtle()
description_writer = turtle.Turtle()
legend_writer = turtle.Turtle()

# Customization settings
STATUS_COLOR = "black"
ARRAY_SUBLIST_COLOR = "light blue"
DESCRIPTION_COLOR = "gray"
DEFAULT_BAR_COLOR = "gray"
COMPLETION_COLOR = "green"
SCREEN_BACKGROUND = "light gray"
PIVOT_COLOR = "gold"
LEFT_PIVOT_SUBLIST_COLOR = "white"
RIGHT_PIVOT_SUBLIST_COLOR = "crimson"
SCREEN_BORDER = 10
BAR_WIDTH = 10
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def Partition(all_input_nums, left_idx, right_idx):
    # Index will be incremented before use so set it to left_idx
    less_than_idx = left_idx - 1

    # Write a message explaining that the subarray is being sorted
    # around the pivot element
    WriteDescription("Sorting the sublist using the pivot element...",
                     DESCRIPTION_COLOR)

    # Compare each element to the pivot element
    pivot_element = all_input_nums[right_idx]
    for idx in range(left_idx, right_idx):
        if all_input_nums[idx] < pivot_element:
            # Increment where the next value less than the pivot should go
            less_than_idx += 1
            # Swap the value less than the pivot to the left side of the subarray
            all_input_nums[idx], all_input_nums[less_than_idx] = \
            all_input_nums[less_than_idx], all_input_nums[idx]

    # Put the pivot element in its correct position
    all_input_nums[less_than_idx + 1], all_input_nums[right_idx] = \
    all_input_nums[right_idx], all_input_nums[less_than_idx + 1]

    # Show the section of the array that was less than the pivot element
    for idx in range(left_idx, less_than_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                all_input_nums[idx],
                LEFT_PIVOT_SUBLIST_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
    # Show the pivot element
    turtles[less_than_idx + 1].clear()
    DrawBar(turtles[less_than_idx + 1],
            BAR_WIDTH * (less_than_idx + 1),
            0,
            all_input_nums[less_than_idx + 1],
            PIVOT_COLOR)
    screen.update()
    # Show the section of the array that was greater than the pivot element
    for idx in range(less_than_idx + 2, right_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                all_input_nums[idx],
                RIGHT_PIVOT_SUBLIST_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
    time.sleep(pause_length)

    # Return the pivot's index
    return less_than_idx + 1


def RandomPartition(all_input_nums, left_idx, right_idx):
    # Get a random pivot index in order to partition the section of the array
    pivot_idx = random.randint(left_idx, right_idx)

    # Indicate that we have selected a random pivot element to use
    WriteDescription("Selecting the random pivot element...",
                     DESCRIPTION_COLOR)

    # Show the pivot element that we selected
    turtles[pivot_idx].clear()
    DrawBar(turtles[pivot_idx],
            BAR_WIDTH * pivot_idx,
            0,
            all_input_nums[pivot_idx],
            PIVOT_COLOR)
    screen.update()
    time.sleep(pause_length)

    # Move the pivot to the far right hand side of the partition
    all_input_nums[pivot_idx], all_input_nums[right_idx] = \
    all_input_nums[right_idx], all_input_nums[pivot_idx]

    # Now that the pivot element is in the last index, sort the partition based on it's value
    return Partition(all_input_nums, left_idx, right_idx)


def QuickSort(all_input_nums, left_idx, right_idx, k_val):

    WriteDescription(
        "Selecting sublist to be sorted using the pivot element...", DESCRIPTION_COLOR)

    # Show the section we are working on
    for idx in range(left_idx, right_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                all_input_nums[idx],
                ARRAY_SUBLIST_COLOR)
    screen.update()
    time.sleep(pause_length)

    # Sort the array around a random pivot then return the pivot's index
    pivot_idx = RandomPartition(all_input_nums, left_idx, right_idx)

    # Reset the bar's back to their default color
    for idx in range(left_idx, right_idx + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                all_input_nums[idx],
                DEFAULT_BAR_COLOR)
    screen.update()
    time.sleep(pause_length)

    # Number of pivot elements greater than or equal to the pivot index
    num_greater_elems = len(all_input_nums) - pivot_idx

    # If we need more elements partition the left side, if we have too many elements
    # partition the right side, if k-1 elements are to the right of the pivot exit
    if num_greater_elems < k_val:
        QuickSort(all_input_nums, left_idx, pivot_idx - 1, k_val)
    elif num_greater_elems > k_val:
        QuickSort(all_input_nums, pivot_idx + 1, right_idx, k_val)
    else:
        return

# Use the slowest speed when running the program
def SetSpeedOne():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.1
    pause_length = 1
    BeginSorting()


# Use the middle speed when running the program
def SetSpeedTwo():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.05
    pause_length = 0.5
    BeginSorting()


# Use the fasted speed when running the program
def SetSpeedThree():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.025
    pause_length = 0.25
    BeginSorting()


# Function that will kick off the sorting process, should be called after the
# speed has been set
def BeginSorting():
    # Turn off the onkey property so the sorting is not accidently restarted
    screen.onkey(None, "1")
    screen.onkey(None, "2")
    screen.onkey(None, "3")
    # Write the sorting status message to the screen
    WriteStatus("Sorting...", STATUS_COLOR)

    DrawLegend(STATUS_COLOR)

    # Start the quick sort algorithm
    QuickSort(all_input_nums, 0, len(all_input_nums) - 1, k_val)

    # Write the completion status message to the screen
    WriteStatus("Complete", COMPLETION_COLOR)

    # Write a description message to the screen
    WriteDescription("Displaying top " + str(k_val) +
                     " integers", DESCRIPTION_COLOR)

    # Show the top k integers in the data list
    for idx in range(len(all_input_nums) - k_val, len(all_input_nums)):
        turtles[idx].clear()
        DrawBar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                all_input_nums[idx],
                COMPLETION_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)


def WriteStatus(status_message, color):
    status_writer.clear()
    status_writer.hideturtle()
    status_writer.speed("fastest")
    status_writer.color(color)
    status_writer.penup()
    status_writer.goto((BAR_WIDTH * len(all_input_nums)) / 2,
                       (max(all_input_nums) + SCREEN_BORDER) / 1.05)
    status_writer.pendown()
    status_writer.write(status_message, False, align="center",
                        font=('Courier', 30, 'bold'))
    status_writer.penup()
    screen.update()


def LegendLabel(color, position, label):

    # Draw label
    legend_writer.goto(12.5,
                       32.7 + ((max(all_input_nums) + SCREEN_BORDER) / position) / 5)
    status_writer.pendown()
    legend_writer.write(label,
                        False,
                        align="left",
                        font=('Courier', 14))
    legend_writer.penup()

    # Draw color
    legend_writer.goto(0,
                       33.5 + ((max(all_input_nums) + SCREEN_BORDER) / position) / 5)
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
    legend_writer.goto(-5,
                       (max(all_input_nums) + SCREEN_BORDER) / 1.05)
    legend_writer.pendown()
    legend_writer.width(4)
    legend_writer.forward(87)  # Forward turtle by 50 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(8)  # Forward turtle by 7 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(87)  # Forward turtle by 50 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(8)  # Forward turtle by 7 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.penup()

    # Draw legend Title
    legend_writer.goto(32.5,
                       (max(all_input_nums) + SCREEN_BORDER) / 1.075)
    print((max(all_input_nums) + SCREEN_BORDER) / 1.1)
    status_writer.pendown()
    legend_writer.write("Legend",
                        False,
                        align="center",
                        font=('Courier', 15, 'bold'))
    legend_writer.penup()

    # Draw legend labels
    LegendLabel(PIVOT_COLOR, 1.125 / 2, "Pivot")
    LegendLabel(ARRAY_SUBLIST_COLOR, 1.1875 / 2, "Sublist")
    LegendLabel(RIGHT_PIVOT_SUBLIST_COLOR, 1.25 / 2, "Greater than pivot")
    LegendLabel(LEFT_PIVOT_SUBLIST_COLOR, 1.325 / 2, "Less than pivot")
    LegendLabel(COMPLETION_COLOR, 1.41 / 2, "Top " + str(k_val) + " Integers")
    screen.update()


def WriteDescription(description_message, color):
    description_writer.clear()
    description_writer.hideturtle()
    description_writer.speed("fastest")
    description_writer.color(color)
    description_writer.penup()
    description_writer.goto(BAR_WIDTH * len(all_input_nums) / 2,
                            (max(all_input_nums) + SCREEN_BORDER) / 1.1)
    description_writer.pendown()
    description_writer.color(color)
    description_writer.write(description_message,
                             False,
                             align="center",
                             font=('Courier', 20, 'bold'))
    description_writer.penup()
    screen.update()


def InitScreen():
    # Creates a title for the screen's window
    screen.title("Quick Select Algorithm")
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
                               BAR_WIDTH * len(all_input_nums) + SCREEN_BORDER,
                               max(all_input_nums) + SCREEN_BORDER)


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


def main():
    # Initialize the global data variables that will be used in various functions
    global turtles

    # Initialize the turtle's screen
    InitScreen()

    # Create the initial bar graph using the data list
    for idx in range(len(all_input_nums)):
        franklin = turtle.Turtle()
        franklin.pensize(3)
        franklin.hideturtle()
        franklin.speed("fastest")
        DrawBar(franklin, BAR_WIDTH * idx,
                0,
                all_input_nums[idx],
                DEFAULT_BAR_COLOR)
        turtles.append(franklin)
    screen.update()

    # Prompt the user to pick what speed they want the algorithm to run at
    WriteStatus("Select a speed to begin sorting 1, 2, 3", STATUS_COLOR)
    screen.onkey(SetSpeedOne, "1")
    screen.onkey(SetSpeedTwo, "2")
    screen.onkey(SetSpeedThree, "3")
    screen.listen()

    # Keep the turtle screen open until mouse is clicked
    screen.mainloop()


if __name__ == "__main__":
    main()
