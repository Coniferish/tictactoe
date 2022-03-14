#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
A one-player Python tic-tac-toe game.
"""
mark = "O" # first time alternate_turn is called, mark is changed to "X"
board = [[None, None, None], [None, None, None], [None, None, None]]

def print_board(board):
    for i in range(3):
        print(board[i])


def get_move(position=None):    
    if not position:
        position = input("Enter the position for your next move in '#row# #column#' format\n")
    position = check_move(list(map(int, list(position.split()))))
    return position


def alternate_turn():
    global mark

    if mark == "O":
        mark = "X"
    elif mark =="X":
        mark = "O"


def play_move():
    global board

    position = get_move()
    alternate_turn()
    board[position[0]][position[1]] = mark
    print_board(board)

# NTS: would it be better to create a list of moves already played instead of checking the actual board?
def check_move(position):
    while board[position[0]][position[1]] != None:
        position = input("""That spot has already been filled.\n
        Enter the position for your next move in '#row# #column#' format\n
        """)
        position = list(map(int, list(position.split())))
    return position