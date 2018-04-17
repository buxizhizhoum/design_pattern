#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses
import random
import time
import sys


HEIGHT = 20
WIDTH = 50
SIDE_LENGTH = 3


snake = [(1, 2)]


ch_snake, ch_head, ch_board, ch_food = "X", "X", "#", "@"

curses.initscr()
win = curses.newwin(HEIGHT, WIDTH, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)

win.nodelay(1)
win.border(0)
curses.start_color()


def add_food(win, snake=None, x=None, y=None):
    x = random.randint(1, WIDTH-2) if x is None else x
    y = random.randint(1, HEIGHT-2) if y is None else y
    # ensure food do not generate on snake
    while on_snake_chk((x, y), snake) is True:
        x = random.randint(1, WIDTH - 2) if x is None else x
        y = random.randint(1, HEIGHT - 2) if y is None else y

    win.addch(y, x, ch_food)
    win.refresh()

    return x, y


def on_snake_chk(food_coordinate, snake):
    if food_coordinate in snake:
        return True
    else:
        return False


def border_chk(point, width, height):
    x, y = point
    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        # on border
        return True
    else:
        return False


def move_snake(snake, direction, food_coordinate, width, height):
    snake_head = snake[0]
    snake_tail = snake[-1]

    if direction == "left":
        snake_tmp = snake_head[0] - 1, snake_head[1]

    elif direction == "right":
        snake_tmp = snake_head[0] + 1, snake_head[1]

    elif direction == "top":
        snake_tmp = snake_head[0], snake_head[1] - 1

    elif direction == "down":
        snake_tmp = snake_head[0], snake_head[1] + 1

    else:
        raise ValueError("wrong direction.")

    if border_chk(snake_tmp, width, height):
        # raise SystemExit
        # sys.exit(0)
        # print("Game Over")
        win.addstr(9, 20, "Game Over!")
        win.refresh()
        return

    snake.insert(0, snake_tmp)

    if snake_tmp[0] == food_coordinate[0] \
            and snake_tmp[1] == food_coordinate[1]:

        # erase food
        win.addch(food_coordinate[1], food_coordinate[0], " ")
        win.refresh()

        # set flag_food to instruct that there is no food.
        global flag_food
        flag_food = False
    else:
        snake.pop(-1)  # del tail

    # erase tail by change character to " "
    win.addch(snake_tail[1], snake_tail[0], " ")  # x or y first?
    win.refresh()
    display_initial_snake(snake)


def display_initial_snake(snake):
    if not snake:
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
        win.addch(y, x, ch_snake)
        win.refresh()
    else:
        for pos in snake:
            x, y = pos
            win.addch(y, x, ch_snake)
            win.refresh()


def get_input(win):
    input = win.getch()
    win.nodelay(1)
    if input == ord('w'):
        direction = "top"
    elif input == ord("s"):
        direction = "down"
    elif input == ord("a"):
        direction = "left"
    elif input == ord("d"):
        direction = "right"
    elif input == ord('q'):
        sys.exit(0)
    # reset
    elif input == ord('r'):
        # reset
        reset()
        return
    else:
        direction = None
        # pass

    return direction


def clear(win, width, height):
    for i in range(1, width-1):
        for j in range(1, height-1):
            win.addch(j, i, " ")
            win.refresh()


def reset():
    global flag_food
    flag_food = False
    x = random.randint(1, WIDTH - 2)
    y = random.randint(1, HEIGHT - 2)
    global snake
    snake = [(x, y)]
    # erase all content
    clear(win, WIDTH, HEIGHT)


direction = "right"
flag_food = False
while True:
    # display_initial_snake(snake)
    if flag_food is False:
        food_xy = add_food(win, snake=snake)

        flag_food = True

    time.sleep(0.3)
    direction_input = get_input(win)

    if direction_input is not None:
        direction = direction_input

    # win.addstr(20, 10, direction)
    # win.refresh()
    # print direction

    move_snake(snake, direction, food_xy, WIDTH, HEIGHT)


