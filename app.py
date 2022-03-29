#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
A one-player Python tic-tac-toe game.
"""

is_x_turn = True
board = [[None, None, None], [None, None, None], [None, None, None]]


def print_board():
    for i in range(len(board)):
        print(board[i])


def get_move():    
    position = check_if_empty_position(
        convert_indices(
            position_to_list(
                input(
                    """Enter the position for your next move in '#row# #column#' format\n"""
                )
            )
        )
    )
    return position


def convert_indices(position):
    adjusted = [x-1 for x in position]
    return adjusted


def position_to_list(position: str):
    return list(map(int, list(position.split())))


def check_if_empty_position(position):
    while board[position[0]][position[1]] != None:
        position = position_to_list(input("""That spot has already been filled.\n
        Enter the position for your next move in '#row# #column#' format\n
        """))
    return position


def alternate_turn():
    global is_x_turn

    is_x_turn = not is_x_turn


def marker(is_x_turn):
    if is_x_turn:
        return "X"
    else:
        return "O"


def turn():
    position = get_move()
    alternate_turn()
    update_board(position)
    print_board()


def update_board(position):
    global board
    
    board[position[0]][position[1]] = marker(is_x_turn)


def player_win(turns):
    if turns < 4:
        pass
    else:
        return False


if __name__ == '__main__':
    turns = 0
    while not player_win(turns) and turns <= 8:
        turn()
        turns += 1
    print("Game Over.")
    

