# Created By: Andrew Hankins, Joey Walker, Brandon Jones, Robert Melton, and Luke Roberts
import random
import turtle
import time

# Create a global data array so that all the functions can access it
sorting_array = [22,15,6,13,23,41,12,24,8,2,48,19,45,28,21,25,32,44,11,27,33,1,37,20,9,14,5,36,50,47,34,17,29,7,31,16,4,39,43,10,38,3,35,30,42,18,40,26,46,49] # A list of input numbers to be sorted
turtles = [] # A list of the different bas that are present on the screen
k_val = 3 # The k value that is being used to determine how many of the top elements are stated
bar_coloring_speed = 0 # the speed at wich the cars are colored
pause_length = 0 # the amount of time the animation is paused

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
SCREEN_WIDTH_PERCENT = 0.9
SCREEN_HEIGHT_PERCENT = 0.9

""" This is the generic partition step in quick sort.
    A pivot element is selected and then  the rest of the items in the array are compared to it, 
    and then if a item in the list is less than the pivot element a swap occurs between two elements at the 
    'less_than_idx' and 'idx' indexies.
    Finally a swap is made between the 'right_idx' and 'less_than_idx + 1'
"""
def partition(sorting_array, left_idx, right_idx):
    # Index will be incremented before use so set it to left_idx
    less_than_idx = left_idx - 1

    # Write a message explaining that the subarray is being sorted
    # around the pivot element
    write_description("Sorting the sublist using the pivot element...",
                     DESCRIPTION_COLOR)

    # Compare each element to the pivot element
    pivot_element = sorting_array[right_idx]
    for idx in range(left_idx, right_idx):
        if sorting_array[idx] < pivot_element:
            # Increment where the next value less than the pivot should go
            less_than_idx += 1
            # Swap the value less than the pivot to the left side of the subarray
            sorting_array[idx], sorting_array[less_than_idx] = \
            sorting_array[less_than_idx], sorting_array[idx]

    # Put the pivot element in its correct position
    sorting_array[less_than_idx + 1], sorting_array[right_idx] = \
    sorting_array[right_idx], sorting_array[less_than_idx + 1]

    # Show the section of the array that was less than the pivot element
    for idx in range(left_idx, less_than_idx + 1):
        turtles[idx].clear()
        draw_bar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                sorting_array[idx],
                LEFT_PIVOT_SUBLIST_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
    # Show the pivot element
    turtles[less_than_idx + 1].clear()
    draw_bar(turtles[less_than_idx + 1],
            BAR_WIDTH * (less_than_idx + 1),
            0,
            sorting_array[less_than_idx + 1],
            PIVOT_COLOR)
    screen.update()
    # Show the section of the array that was greater than the pivot element
    for idx in range(less_than_idx + 2, right_idx + 1):
        turtles[idx].clear()
        draw_bar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                sorting_array[idx],
                RIGHT_PIVOT_SUBLIST_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
    time.sleep(pause_length)

    # Return the pivot's index
    return less_than_idx + 1


""" This funtion grabs a random index from the array between the 'left_idx' and 'right_idx'
"""
def random_partition(sorting_array, left_idx, right_idx):
    # Get a random pivot index in order to partition the section of the array
    pivot_idx = random.randint(left_idx, right_idx)

    # Indicate that we have selected a random pivot element to use
    write_description("Selecting the random pivot element...",
                     DESCRIPTION_COLOR)

    # Show the pivot element that we selected
    turtles[pivot_idx].clear()
    draw_bar(turtles[pivot_idx],
            BAR_WIDTH * pivot_idx,
            0,
            sorting_array[pivot_idx],
            PIVOT_COLOR)
    screen.update()
    time.sleep(pause_length)

    # Move the pivot to the far right hand side of the partition
    sorting_array[pivot_idx], sorting_array[right_idx] = \
    sorting_array[right_idx], sorting_array[pivot_idx]

    # Now that the pivot element is in the last index, sort the partition based on it's value
    return partition(sorting_array, left_idx, right_idx)


""" This is the generic quickselect algorithm.
    In this function, we call the 'random_partition' function which does most of the work as far as rearranging the array.
    We then call 'quick_select' recursivly until we have the top k elements.
"""
def quick_select(sorting_array, left_idx, right_idx, k_val):

    write_description(
        "Selecting sublist to be sorted using the pivot element...", DESCRIPTION_COLOR)

    # Show the section we are working on
    for idx in range(left_idx, right_idx + 1):
        turtles[idx].clear()
        draw_bar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                sorting_array[idx],
                ARRAY_SUBLIST_COLOR)
    screen.update()
    time.sleep(pause_length)

    # Sort the array around a random pivot then return the pivot's index
    pivot_idx = random_partition(sorting_array, left_idx, right_idx)

    # Reset the bar's back to their default color
    for idx in range(left_idx, right_idx + 1):
        turtles[idx].clear()
        draw_bar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                sorting_array[idx],
                DEFAULT_BAR_COLOR)
    screen.update()
    time.sleep(pause_length)

    # Number of pivot elements greater than or equal to the pivot index
    num_greater_elems = len(sorting_array) - pivot_idx

    # If we need more elements partition the left side, if we have too many elements
    # partition the right side, if k-1 elements are to the right of the pivot exit
    if num_greater_elems < k_val:
        quick_select(sorting_array, left_idx, pivot_idx - 1, k_val)
    elif num_greater_elems > k_val:
        quick_select(sorting_array, pivot_idx + 1, right_idx, k_val)
    else:
        return

# Use the slowest speed when running the program
def set_speed_one():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.1
    pause_length = 1
    begin_sorting()


# Use the middle speed when running the program
def set_speed_two():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.05
    pause_length = 0.5
    begin_sorting()


# Use the fasted speed when running the program
def set_speed_three():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.025
    pause_length = 0.25
    begin_sorting()


# Function that will kick off the sorting process, should be called after the
# speed has been set
def begin_sorting():
    # Turn off the onkey property so the sorting is not accidently restarted
    screen.onkey(None, "1")
    screen.onkey(None, "2")
    screen.onkey(None, "3")
    # Write the sorting status message to the screen
    write_status("Sorting...", STATUS_COLOR)

    draw_legend(STATUS_COLOR)

    # Start the quick sort algorithm
    quick_select(sorting_array, 0, len(sorting_array) - 1, k_val)

    # Write the completion status message to the screen
    write_status("Complete", COMPLETION_COLOR)

    # Write a description message to the screen
    write_description("Displaying top " + str(k_val) +
                     " integers", DESCRIPTION_COLOR)

    # Show the top k integers in the data list
    for idx in range(len(sorting_array) - k_val, len(sorting_array)):
        turtles[idx].clear()
        draw_bar(turtles[idx],
                BAR_WIDTH * idx,
                0,
                sorting_array[idx],
                COMPLETION_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)

""" Writes what is currently happening in the array, such as whether we are sorting the array or finished sorting the top k elements
"""
def write_status(status_message, color):
    status_writer.clear()
    status_writer.hideturtle()
    status_writer.speed("fastest")
    status_writer.color(color)
    status_writer.penup()
    status_writer.goto((BAR_WIDTH * len(sorting_array)) / 2,
                       (max(sorting_array) + SCREEN_BORDER) / 1.05)
    status_writer.pendown()
    status_writer.write(status_message, False, align="center",
                        font=('Courier', 30, 'bold'))
    status_writer.penup()
    screen.update()

""" This funtion creates the different sections found in the legend, which is located at the
    the top-left of the application
"""
def legend_label(color, position, label):

    # Draw label
    legend_writer.goto(12.5,
                       32.7 + ((max(sorting_array) + SCREEN_BORDER) / position) / 5)
    status_writer.pendown()
    legend_writer.write(label,
                        False,
                        align="left",
                        font=('Courier', 14))
    legend_writer.penup()

    # Draw color
    legend_writer.goto(0,
                       33.5 + ((max(sorting_array) + SCREEN_BORDER) / position) / 5)
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

""" This funtion draws the box the contains the contents of the legend,
    as well as, prints the contents of the legend.
    The parameters allow for any color when writing the legend's title
"""
def draw_legend(color):
    legend_writer.clear()
    legend_writer.hideturtle()
    legend_writer.speed("fastest")
    legend_writer.color(color)
    legend_writer.penup()

    # Draw legend square
    legend_writer.goto(-5,
                       (max(sorting_array) + SCREEN_BORDER) / 1.05)
    legend_writer.pendown()
    legend_writer.width(4)
    legend_writer.forward(87)  # Forward turtle by 87 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(8)  # Forward turtle by 8 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(87)  # Forward turtle by 87 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(8)  # Forward turtle by 8 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.penup()

    # Draw legend Title
    legend_writer.goto(32.5,
                       (max(sorting_array) + SCREEN_BORDER) / 1.075)
    print((max(sorting_array) + SCREEN_BORDER) / 1.1)
    status_writer.pendown()
    legend_writer.write("Legend",
                        False,
                        align="center",
                        font=('Courier', 15, 'bold'))
    legend_writer.penup()

    # Draw legend labels
    legend_label(PIVOT_COLOR, 1.125 / 2, "Pivot")
    legend_label(ARRAY_SUBLIST_COLOR, 1.1875 / 2, "Sublist")
    legend_label(RIGHT_PIVOT_SUBLIST_COLOR, 1.25 / 2, "Greater than pivot")
    legend_label(LEFT_PIVOT_SUBLIST_COLOR, 1.325 / 2, "Less than pivot")
    legend_label(COMPLETION_COLOR, 1.41 / 2, "Top " + str(k_val) + " Integers")
    screen.update()

""" This funtion is used to write a more in-depth desciption of what is currently happening in the algorithm.
    This would included stating which part of the sort is being executed.
    The parameters allow for any message and any color for the text.
"""
def write_description(description_message, color):
    description_writer.clear()
    description_writer.hideturtle()
    description_writer.speed("fastest")
    description_writer.color(color)
    description_writer.penup()
    description_writer.goto(BAR_WIDTH * len(sorting_array) / 2,
                            (max(sorting_array) + SCREEN_BORDER) / 1.1)
    description_writer.pendown()
    description_writer.color(color)
    description_writer.write(description_message,
                             False,
                             align="center",
                             font=('Courier', 20, 'bold'))
    description_writer.penup()
    screen.update()

""" This function creates a sceen for the application when it opens
"""
def init_screen():
    # Creates a title for the screen's window
    screen.title("Quick Select Algorithm")
    # Sets the height and width of the turtle window
    screen.setup(width = SCREEN_WIDTH_PERCENT, height = SCREEN_HEIGHT_PERCENT)
    # Sets the screens background color
    screen.bgcolor(SCREEN_BACKGROUND)
    # Turns of the screen's auto update feature
    screen.tracer(0)
    # Sets the coordinates within the window using the bottom left and
    # upper right coordinates
    screen.setworldcoordinates(0 - SCREEN_BORDER,
                               0,
                               BAR_WIDTH * len(sorting_array) + SCREEN_BORDER,
                               max(sorting_array) + SCREEN_BORDER)

""" This funtion draws an individual bar on the screen.
    With these parameters you are able to start a drawing at any (x,y) coordinate and set the height to any value,
    but we use it to set it height to the value found in the sorting array at a certain position, the color is also customizable
"""
def draw_bar(t, x, y, height, color):
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

# This is the main function that begins all the processes that occur on the screen
def main():
    # Initialize the global data variables that will be used in various functions
    global turtles

    # Initialize the turtle's screen
    init_screen()

    # Create the initial bar graph using the data list
    for idx in range(len(sorting_array)):
        franklin = turtle.Turtle()
        franklin.pensize(3)
        franklin.hideturtle()
        franklin.speed("fastest")
        draw_bar(franklin, BAR_WIDTH * idx,
                0,
                sorting_array[idx],
                DEFAULT_BAR_COLOR)
        turtles.append(franklin)
    screen.update()

    # Prompt the user to pick what speed they want the algorithm to run at
    write_status("Select a speed to begin sorting 1, 2, 3", STATUS_COLOR)
    screen.onkey(set_speed_one, "1")
    screen.onkey(set_speed_two, "2")
    screen.onkey(set_speed_three, "3")
    screen.listen()

    # Keep the turtle screen open until mouse is clicked
    screen.mainloop()


if __name__ == "__main__":
    main()
