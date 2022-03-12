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


def get_move():
    global board

    position = input("Enter the position for your next move in '#row# #column#' format\n")
    position = list(map(int, list(position.split())))
    if board[position[0]][position[1]] != None:
        get_move()
    return position


def alternate_turn():
    global mark

    if mark == "O":
        mark = "X"
    elif mark =="X":
        mark = "O"


def play_move():
    global mark
    global board

    position = get_move()
    alternate_turn()
    board[position[0]][position[1]] = mark
    print_board(board)