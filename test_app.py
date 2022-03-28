import app
from unittest.mock import patch
import unittest

position = (0,0)

# def test_print_board_exists():
#     assert print_board() == None

def test_board_rows():
    assert len(app.board) == 3

def test_board_columns():
    columns = 0
    for i in range(len(app.board)):
        columns += 1
    assert columns == 3


def test_alternate_turn():
    temp = app.is_x_turn
    app.alternate_turn()
    assert app.is_x_turn != temp

def test_marker_x_turn():
    assert app.marker(True) == "X"

def test_marker_o_turn():
    assert app.marker(False) == "O"

# todo
# def test_updated_position():
#     position = [1, 1]
#     initial = board[position[0]][position[1]]
#     with patch('builtins.input', side_effect=position):
#         play_move()
#     updated = board[position[0]][position[1]]
#     assert initial != updated

# def test_get_move_len():
#     get_move()
