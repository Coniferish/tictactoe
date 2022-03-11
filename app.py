#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
A one-player Python tic-tac-toe game.
"""

board = [[None, None, None], [None, None, None], [None, None, None]]

def print_board(board):
    for i in range(3):
        print(board[i])

def get_move():
    position = input("Enter the position for your next move in '#row# #column#' format\n")
    return list(map(int, list(position.split())))