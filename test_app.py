from app import *

position = (0,0)

def test_print_board():
    assert print_board != None

def test_board_rows():
    assert len(board) == 3

# may need to change so it is three individual asserts
def test_board_columns():
    for i in range(3):
        assert len(board[i]) == 3

def test_updated_position():
    initial = board[position[0]][position[1]]
    updated = board[position[0]][position[1]]
    assert initial != updated
