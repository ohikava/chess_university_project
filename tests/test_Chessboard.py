from Chessboard import Chessboard

cb = Chessboard()


def test_1():
    cb.move(5 + 2j, 5 + 4j)
    cb.move(5 + 7j, 5 + 5j)
    assert not cb.move(5 + 4j, 5 + 5j)[0]


def test_2():
    cb.move(2 + 1j, 3 + 3j)
    cb.move(6 + 8j, 1 + 3j)
    assert cb.move(2 + 2j, 1 + 3j)[0]
    assert not cb.chess_board[2 + 2j]


def test_3():
    cb.move(4 + 8j, 8 + 4j)
    cb.move(8 + 2j, 8 + 3j)
    assert cb.move(8 + 4j, 8 + 3j)[0]
    cb.move(8 + 1j, 8 + 3j)
    assert not cb.chess_board[8 + 1j]
    assert cb.chess_board[8 + 3j].name == 'r' and cb.chess_board[8 + 3j].fraction

def test_4():
    cb.move(4 + 7j, 4 + 6j)
    cb.move(3 + 3j, 2 + 5j)
    cb.move(1 + 7j, 1 + 6j)
    assert cb.move(2 + 5j, 3 + 7j)[0]
    assert cb.chess_board[3 + 7j].name == 'n'
    assert cb.move(3 + 8j, 8 + 3j)[0]

def test_is_king_safe():
    cb.restart()
    assert cb.is_king_safe()[0]
    cb.move(6 + 2j, 6 + 4j)
    cb.move(5 + 7j, 5 + 6j)
    cb.move(1 + 2j, 1 + 3j)
    assert cb.move(4 + 8j, 8 + 4j)[1] == 'Шах от фигуры с позиции h4'
    assert not cb.is_king_safe()[0]
    cb.move(7 + 2j, 7 + 3j)
    assert cb.move(1 + 7j, 1 + 6j)[1] == 'Ход завершен'
    assert cb.is_king_safe()[0]
