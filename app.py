#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
A one-player Python tic-tac-toe game.
"""

is_x_turn = True
board = [[None, None, None], [None, None, None], [None, None, None]]

def print_board(board):
    for i in range(len(board)):
        print(board[i])


def get_move(position=None):    
    if not position:
        position = input("Enter the position for your next move in '#row# #column#' format\n")
    position = check_move(list(map(int, list(position.split()))))
    return position


def check_move(position):
    while board[position[0]][position[1]] != None:
        position = input("""That spot has already been filled.\n
        Enter the position for your next move in '#row# #column#' format\n
        """)
        position = list(map(int, list(position.split())))
    return position


def alternate_turn():
    global is_x_turn

    is_x_turn = not is_x_turn


def marker(is_x_turn):
    if is_x_turn:
        return "X"
    else:
        return "O"


def play_move():
    global board

    position = get_move()
    alternate_turn()
    board[position[0]][position[1]] = marker(is_x_turn)
    print_board(board)


if __name__ == '__main__':
    play_move()
