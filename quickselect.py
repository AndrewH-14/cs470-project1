import sys
import csv
import random
import turtle
import time

# Create a global data array so that all the functions can access it
all_input_nums = list()
turtles = []
k_val = 0

# Global turtle objects used in various functions
screen = turtle.Screen()
status_writer = turtle.Turtle()
description_writer = turtle.Turtle()

# Customization settings
STATUS_COLOR = "black"
ARRAY_SUBLIST_COLOR = "gold"
DESCRIPTION_COLOR = "gray"
DEFAULT_BAR_COLOR = "gray"
COMPLETION_COLOR = "green"
SCREEN_BACKGROUND = "light gray"
PIVOT_COLOR = "crimson"
SCREEN_BORDER = 10
BAR_WIDTH = 10

def quickselect(all_input_nums, left, right, k_val, arr_len):
    if (k_val > 0 and k_val <= right - left + 1):
        part_pos = partition(all_input_nums, left, right)
        # print(f'part_pos = {part_pos}, arr = {arr}')
        if (part_pos - left == k_val - 1):
            return partition(all_input_nums, left, right)
        if (part_pos - left > k_val - 1):
            # print(f'partition positition was higher than the k_val - 1: {part_pos}')
            return quickselect(all_input_nums, left, part_pos - 1, k_val, arr_len)
        else:
            # print(f'partition positition was lower than the k_val - 1: {part_pos}')
            return quickselect(all_input_nums, part_pos + 1, right, k_val - part_pos + left - 1, arr_len)


def partition(all_input_nums, left, right):
    for idx in range(left, right + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, all_input_nums[idx], ARRAY_SUBLIST_COLOR)
        screen.update()
        time.sleep(0.1)

    time.sleep(1)

    DrawBar(turtles[right], BAR_WIDTH * right, 0, all_input_nums[right], PIVOT_COLOR)
    pivot_val = all_input_nums[right]

    i = left
    for j in range(left, right):
        if (all_input_nums[j] <= pivot_val):
            temp = all_input_nums[i]
            all_input_nums[i] = all_input_nums[j]
            all_input_nums[j] = temp
            i += 1
    temp = all_input_nums[i]
    all_input_nums[i] = all_input_nums[right]
    all_input_nums[right] = temp

    for idx in range(left, right + 1):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, all_input_nums[idx], DEFAULT_BAR_COLOR)
        screen.update()
        time.sleep(0.1)

    return i


def BeginSorting():
    # Turn off the onkey property so the sorting is not accidentally restarted
    screen.onkey(None, "space")

    # Write the sorting status message to the screen
    WriteStatus("Sorting...", STATUS_COLOR)

    # Start the quick select algorithm
    list_len = len(all_input_nums)
    quickselect(all_input_nums, 0, list_len - 1, list_len - k_val - 1, list_len)
    print(all_input_nums)

    # Write the completion status message to the screen
    WriteStatus("Complete", COMPLETION_COLOR)

    # Write a description message to the screen
    WriteDescription("Displaying top " + str(k_val) + " integers", DESCRIPTION_COLOR)

    # Show the top k integers in the data list
    for idx in range(len(all_input_nums) - k_val, len(all_input_nums)):
        turtles[idx].clear()
        DrawBar(turtles[idx], BAR_WIDTH * idx, 0, all_input_nums[idx], COMPLETION_COLOR)
        screen.update()
        time.sleep(0.1)


def WriteStatus(status_message, color):
    status_writer.clear()
    status_writer.hideturtle()
    status_writer.speed("fastest")
    status_writer.color(color)
    status_writer.penup()
    status_writer.goto((BAR_WIDTH * len(all_input_nums) + SCREEN_BORDER) / 2,
                       (max(all_input_nums) + SCREEN_BORDER) / 1.1)
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
    description_writer.goto((BAR_WIDTH * len(all_input_nums) + SCREEN_BORDER) / 2,
                            (max(all_input_nums) + SCREEN_BORDER) / 1.2)
    description_writer.pendown()
    description_writer.color(color)
    description_writer.write(description_message, False, align="center", font=('Courier', 20, 'bold'))
    description_writer.penup()
    screen.update()


def InitScreen():
    # Creates a title for the screen's window
    screen.title("Quick Select Algorithm")
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
    global k_val
    global turtles
    global all_input_nums

    file = open(f'{"unsorted_input.txt"}')
    csv_reader = csv.reader(file)
    data = list()
    for line in csv_reader:
        data.append(line)
    for num in data[0]:
        all_input_nums.append(int(num))

    k_val = int(data[1][0])

    # Initialize the turtle's screen
    InitScreen()

    # Create the initial bar graph using the data list
    for idx in range(len(all_input_nums)):
        franklin = turtle.Turtle()
        franklin.pensize(3)
        franklin.hideturtle()
        franklin.speed("fastest")
        DrawBar(franklin, BAR_WIDTH * idx, 0, all_input_nums[idx], DEFAULT_BAR_COLOR)
        turtles.append(franklin)
    screen.update()

    WriteStatus("Press space to begin sorting", STATUS_COLOR)

    screen.onkey(BeginSorting, "space")
    screen.listen()

    # Keep the turtle screen open until mouse is clicked
    screen.mainloop()


if __name__ == "__main__":
    main()