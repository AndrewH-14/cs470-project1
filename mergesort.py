# Created By DSS: Andrew Hankins, Joey Walker, Brandon Jones, Robert Melton, and Luke Roberts
import turtle
import time

# Global data variables used in various functions
data = [22,15,6,13,23,41,12,24,8,2,48,19,45,28,21,25,32,44,11,27,33,1,37,20,9,14,5,36,50,47,34,17,29,7,31,16,4,39,43,10,38,3,35,30,42,18,40,26,46,49]
turtles = []
k = 3
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
LEFT_ITERATOR_COLOR = "light green"
RIGHT_ITERATOR_COLOR = "light blue"
SCREEN_BACKGROUND = "light gray"
SCREEN_BORDER = 10
BAR_WIDTH = 10
SCREEN_WIDTH_PERCENT = 0.9
SCREEN_HEIGHT_PERCENT = 0.9
BOX_WIDTH = 10
BOX_HEIGHT = 2
LEGEND_HEIGHT = 20.75
LEGEND_WIDTH = 80

# The merge function combines two subarrays into a single,
# larger sorted array by continuously selecting the smallest element from
# the beginning of both subarrays, until all elements have been exhausted
def merge(lower_idx, middle_idx, upper_idx):
    sorted_data = []
    left_iter = lower_idx
    right_iter = middle_idx + 1

    write_description("Dividing into sublists...", DESCRIPTION_COLOR)

    # Indicate the two sections we are merging by their color
    for idx in range(lower_idx, middle_idx + 1):
        turtles[idx].clear()
        draw_bar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], SUBLIST_ONE_COLOR)
    for idx in range(middle_idx + 1, upper_idx + 1):
        turtles[idx].clear()
        draw_bar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], SUBLIST_TWO_COLOR)
    screen.update()
    time.sleep(pause_length)

    # Compare elements from either side of the array and add the smaller one to the
    # sorted array
    while left_iter <= middle_idx and right_iter <= upper_idx:
        # Draw the current position of the left_iter and right_iter
        draw_bar(turtles[left_iter], BAR_WIDTH * left_iter, 0, data[left_iter], LEFT_ITERATOR_COLOR)
        draw_bar(turtles[right_iter], BAR_WIDTH * right_iter, 0, data[right_iter], RIGHT_ITERATOR_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
        if data[left_iter] <= data[right_iter]:
            sorted_data.append(data[left_iter])
            # Draw the current sorted array
            draw_box(turtles[lower_idx+len(sorted_data)-1], BAR_WIDTH * (lower_idx+len(sorted_data)-1), 0, data[left_iter], MERGED_LIST_COLOR)
            time.sleep(bar_coloring_speed)
            screen.update()
            left_iter += 1
            # Draw the updated position of the left_iter
            draw_bar(turtles[left_iter-1], BAR_WIDTH * (left_iter-1), 0, data[left_iter-1], SUBLIST_ONE_COLOR)
        else:
            sorted_data.append(data[right_iter])
            # Draw the current sorted array
            draw_box(turtles[lower_idx+len(sorted_data)-1], BAR_WIDTH * (lower_idx+len(sorted_data)-1), 0, data[right_iter], MERGED_LIST_COLOR)
            time.sleep(bar_coloring_speed)
            screen.update()
            right_iter += 1
            # Draw the updated position of the right_iter
            draw_bar(turtles[right_iter-1], BAR_WIDTH * (right_iter-1), 0, data[right_iter-1], SUBLIST_TWO_COLOR)

    # Add any leftover values from the left side of the array to the sorted array
    while left_iter <= middle_idx:
        # Draw the updated position of the left_iter
        draw_bar(turtles[left_iter], BAR_WIDTH * left_iter, 0, data[left_iter], LEFT_ITERATOR_COLOR)
        screen.update()
        sorted_data.append(data[left_iter])
        # Draw the current sorted array
        draw_box(turtles[lower_idx+len(sorted_data)-1], BAR_WIDTH * (lower_idx+len(sorted_data)-1), 0, data[left_iter], MERGED_LIST_COLOR)
        time.sleep(bar_coloring_speed)
        screen.update()
        left_iter += 1
        # Recolor the first subarray after the pass of the left_iter
        draw_bar(turtles[left_iter-1], BAR_WIDTH * (left_iter-1), 0, data[left_iter-1], SUBLIST_ONE_COLOR)
    # Add any leftover values from the right side of the array to the sorted array
    while right_iter <= upper_idx:
        # Draw the updated position of the right_iter
        draw_bar(turtles[right_iter], BAR_WIDTH * right_iter, 0, data[right_iter], RIGHT_ITERATOR_COLOR)
        screen.update()
        sorted_data.append(data[right_iter])
        # Draw the current sorted array
        draw_box(turtles[lower_idx+len(sorted_data)-1], BAR_WIDTH * (lower_idx+len(sorted_data)-1), 0, data[right_iter], MERGED_LIST_COLOR)
        time.sleep(bar_coloring_speed)
        screen.update()
        right_iter += 1
        # Recolor the second subarray after the pass of the right_iter
        draw_bar(turtles[right_iter-1], BAR_WIDTH * (right_iter-1), 0, data[right_iter-1], SUBLIST_TWO_COLOR)

    # Copy the sorted integers back into the data array
    for idx in range(len(sorted_data)):
        data[lower_idx + idx] = sorted_data[idx]

    # Provide a description letting the user know the two sublists are being merged
    write_description("Merging sublists...", DESCRIPTION_COLOR)

    # Update the bar graph to show the resulting sorted data
    for idx in range(lower_idx, upper_idx + 1):
        turtles[idx].clear()
        draw_bar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], MERGED_LIST_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)
    time.sleep(pause_length)
    for idx in range(lower_idx, upper_idx + 1):
        turtles[idx].clear()
        draw_bar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], DEFAULT_BAR_COLOR)
    screen.update()
    time.sleep(pause_length)

# Mergesort works by dividing an array into two subarrays, sorting them
# recursively and then merging them back into a single, sorted array
def mergesort(lower_idx, upper_idx):
    if lower_idx >= upper_idx:
        return
    middle_idx = (lower_idx + upper_idx) // 2
    mergesort(lower_idx, middle_idx)
    mergesort(middle_idx + 1, upper_idx)
    merge(lower_idx, middle_idx, upper_idx)

# Draws a bar assuming the turtle is facing east
def draw_bar(t, x, y, height, color):
    t.fillcolor(color)
    t.setheading(0)
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

# Draws a Box for an element in the subarray
def draw_box(t, x, y, height, color):
    # Set up number the number inside the box
    t.penup()
    t.goto(x, y + 1.2)
    t.forward(BOX_WIDTH/3)
    t.left(90)
    t.forward(BOX_HEIGHT/4)
    t.right(90)
    t.write(str(height))
    t.right(180)
    t.forward(BOX_WIDTH/3)
    t.left(90)
    t.forward(BOX_HEIGHT/4)
    t.left(90)
    # Create the Box
    t.pendown()
    t.forward(BOX_WIDTH)
    t.left(90)
    t.forward(1.8)
    t.left(90)
    t.forward(BOX_WIDTH)
    t.left(90)
    t.forward(1.8)
    t.left(90)

# Set up the screen for creating the animation
def initial_screen():
    # Creates a title for the screen's window
    screen.title("Merge Sort Algorithm")
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
                               BAR_WIDTH * len(data) + SCREEN_BORDER,
                               max(data) + SCREEN_BORDER)

# Sets the animation speed of the program to the slowest option
def set_speed_one():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.1
    pause_length = 1
    begin_sorting()

# Sets the animation speed of the program to the medium speed option
def set_speed_two():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.05
    pause_length = 0.5
    begin_sorting()

# Sets the animation speed of the program to the fastest option
def set_speed_three():
    global bar_coloring_speed
    global pause_length
    bar_coloring_speed = 0.025
    pause_length = 0.25
    begin_sorting()

# Disables changing animation speed, writes the sorting status,
# begins the mergesort() algorithm, writes the amount of the top integers
# written to the screen, and visualizes the top k elements.
def begin_sorting():
    # Turn off the onkey property so the sorting is not accidently restarted
    screen.onkey(None, "1")
    screen.onkey(None, "2")
    screen.onkey(None, "3")

    # Write the sorting status message to the screen
    write_status("Sorting...", STATUS_COLOR)

    # Draw the legend border and contents
    draw_legend(STATUS_COLOR)

    # Start the merge sort algorithm
    mergesort(0, len(data) - 1)

    # Write the completion status message to the screen
    write_status("Complete", COMPLETION_COLOR)

    # Write a description message to the screen
    write_description("Displaying top " + str(k) +
                     " integers", DESCRIPTION_COLOR)

    # Show the top k integers in the data list
    for idx in range(len(data) - k, len(data)):
        turtles[idx].clear()
        draw_bar(turtles[idx], BAR_WIDTH * idx, 0, data[idx], COMPLETION_COLOR)
        screen.update()
        time.sleep(bar_coloring_speed)

# Write a status of what is going on with the animation
def write_status(status_message, color):
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

# Adds an element and color block to the legend
def legend_label(color, position, label):

    # Draw label in the legend
    legend_writer.goto((5) /
                       2, (max(data) + SCREEN_BORDER) / position)
    status_writer.pendown()
    legend_writer.write(label, False, align="left",
                        font=('Courier', 14))
    legend_writer.penup()

    # Draw color in the legend
    legend_writer.goto((130) /
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

# Draw the legend border and contents
def draw_legend(color):
    legend_writer.clear()
    legend_writer.hideturtle()
    legend_writer.speed("fastest")
    legend_writer.color(color)
    legend_writer.penup()

    # Draw legend rectangle
    legend_writer.goto((0) /
                       2, (max(data) + SCREEN_BORDER) / 1.01)
    legend_writer.pendown()
    legend_writer.width(4)
    legend_writer.forward(LEGEND_WIDTH)  # Forward turtle by 50 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(LEGEND_HEIGHT)  # Forward turtle by 7 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(LEGEND_WIDTH)  # Forward turtle by 50 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.forward(LEGEND_HEIGHT)  # Forward turtle by 7 units
    legend_writer.right(90)  # Turn turtle by 90 degree
    legend_writer.penup()

    # Draw legend title
    legend_writer.goto((80) /
                       2, (max(data) + SCREEN_BORDER) / 1.07)
    status_writer.pendown()
    legend_writer.write("Legend", False, align="center",
                        font=('Courier', 15, 'bold'))
    legend_writer.penup()

    # Draw legend labels
    legend_label(SUBLIST_ONE_COLOR, 1.125, "Left Sublist")
    legend_label(SUBLIST_TWO_COLOR, 1.1875, "Right Sublist")
    legend_label(MERGED_LIST_COLOR, 1.25, "Merged List")
    legend_label(COMPLETION_COLOR, 1.325, "Top " + str(k) + " Integers")
    legend_label(LEFT_ITERATOR_COLOR, 1.405, "Left Iterator")
    legend_label(RIGHT_ITERATOR_COLOR, 1.485, "Right Iterator")
    screen.update()

# Write a description of what is going on with the animation
def write_description(description_message, color):
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

# The main function initializes global variables used in the various functions,
# initializes the turtle screen, creates the initial bar graph using the data list,
# prompts the user to select a speed at which the program is animated,
# and keeps the turtle screen open until the window is closed.
# It calls three functions: initial_screen(), draw_bar(), and write_status().
def main():
    # Initialize the global data variables that will be used in various functions
    global turtles

    # Initialize the turtle's screen
    initial_screen()

    # Create the initial bar graph using the data list
    for idx in range(len(data)):
        franklin = turtle.Turtle()
        franklin.pensize(3)
        franklin.hideturtle()
        franklin.speed("fastest")
        draw_bar(franklin, BAR_WIDTH * idx, 0, data[idx], DEFAULT_BAR_COLOR)
        turtles.append(franklin)
    screen.update()

    # Prompt to select the speed at which the program is animated
    write_status("Select a speed to begin sorting 1, 2, 3", STATUS_COLOR)
    screen.onkey(set_speed_one, "1")
    screen.onkey(set_speed_two, "2")
    screen.onkey(set_speed_three, "3")
    screen.listen()

    # Keep the turtle screen open until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()
