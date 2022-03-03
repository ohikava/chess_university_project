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


def test_is_king_safe():
    cb.restart()
    assert cb.is_king_safe()[0]
    cb.move(6 + 2j, 6 + 4j)
    cb.move(5 + 7j, 5 + 6j)
    cb.move(1 + 2j, 1 + 3j)
    assert cb.move(4 + 8j, 8 + 4j)[1] == 'Шах от фигуры с позиции h4'
    assert not cb.is_king_safe()[0]
    assert not cb.check_move(1 + 3j, 1 + 4j)
    assert cb.check_move(7 + 2j, 7 + 3j)
    assert cb.move(1 + 3j, 1 + 4j)[1] == "Вы не можете так ходить, пока вам стоит шах"
    assert cb.move(7 + 2j, 7 + 3j)[0]
    assert cb.move(1 + 7j, 1 + 6j)[1] == 'Ход завершен'
    assert cb.is_king_safe()[0]


def test_check_checkmate_1():
    cb.restart()
    cb.move(7 + 2j, 7 + 4j)
    cb.move(5 + 7j, 5 + 5j)
    cb.move(6 + 2j, 6 + 3j)
    cb.move(4 + 8j, 8 + 4j)
    assert cb.check_checkmate()[0]
    assert cb.check_checkmate()[1] == set()


def test_check_checkmate_2():
    cb.restart()
    cb.move(6 + 2j, 6 + 3j)
    cb.move(5 + 7j, 5 + 5j)
    cb.move(1 + 2j, 1 + 3j)
    cb.move(4 + 8j, 8 + 4j)

    assert not cb.is_king_safe()[0]
    assert not cb.check_checkmate()[0]
    assert cb.check_checkmate()[1] == {(7 + 2j, 7 + 3j)}


def test_chessboard_with_checkmate():
    cb.restart()
    cb.move(5 + 2j, 5 + 4j)
    cb.move(5 + 7j, 5 + 5j)
    cb.move(6 + 1j, 3 + 4j)
    cb.move(2 + 8j, 3 + 6j)
    cb.move(4 + 1j, 8 + 5j)
    cb.move(7 + 8j, 6 + 6j)
    assert cb.move(8 + 5j, 6 + 7j)[1] == 'Игра завершена, Чёрным поставлен мат'

def test_update_pawn():
    cb.restart()
    assert cb.update_pawn(1 + 8j, 'Ферзь')[0]
    assert cb.chess_board[1 + 8j].name == 'q'
    assert not cb.chess_board[1 + 8j].fraction

    cb.restart()
    cb.move(1 + 2j, 1 + 3j)
    assert cb.update_pawn(2 + 1j, 'Ладья')[0]
    assert cb.chess_board[2 + 1j].name == 'r'
    assert cb.chess_board[2 + 1j].fraction

    assert not cb.update_pawn(2 + 3j, 'sdf')[0]


def test_make_an_passant():
    cb.restart()
    cb.move(2 + 2j, 2 + 4j)
    cb.move(8 + 7j, 8 + 5j)
    cb.move(2 + 4j, 2 + 5j)
    cb.move(1 + 7j, 1 + 5j)
    assert cb.make_en_passant(2 + 5j, 1 + 6j)
    assert not cb.chess_board[1 + 5j]
    assert cb.chess_board[1 + 6j]

    cb.restart()

    cb.move(4 + 2j, 4 + 4j)
    cb.move(3 + 7j, 3 + 5j)
    cb.move(4 + 4j, 4 + 5j)
    cb.move(8 + 7j, 8 + 5j)
    assert not cb.make_en_passant(4 + 5j, 3 + 6j)
    cb.move(1 + 2j, 1 + 3j)
    cb.move(5 + 7j, 5 + 5j)
    assert cb.make_en_passant(4 + 5j, 5 + 6j)

    cb.restart()
    cb.move(4 + 2j, 4 + 4j)
    cb.move(5 + 7j, 5 + 5j)
    cb.move(4 + 4j, 4 + 5j)
    cb.move(3 + 7j, 3 + 5j)
    assert not cb.move(4 + 5j, 5 + 6j)[0]
    assert cb.move(4 + 5j, 3 + 6j)[0]


