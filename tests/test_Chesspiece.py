from Chesspiece import Pawn, King, Queen, Bishop, Rook, Knight
from Chessboard import Chessboard

cb = Chessboard()

white_p = Pawn(True)
black_p = Pawn(False)
white_k = King(True)
white_q = Queen(True)
white_b = Bishop(True)
white_r = Rook(True)
white_n = Knight(True)


def test_white_p_moving():
    assert white_p.move_to(2 + 2j, 2 + 3j)[0]
    assert white_p.move_to(2 + 2j, 2 + 4j, True)[0]
    assert not white_p.move_to(2 + 2j, 2 + 1j)[0]


def test_black_p_moving():
    assert black_p.move_to(2 + 7j, 2 + 6j)[0]
    assert black_p.move_to(3 + 6j, 3 + 5j)[0]
    assert black_p.move_to(2 + 7j, 2 + 5j, True)[0]


def test_p_attacks():
    assert white_p.attack(4 + 7j, 5 + 8j)[0]
    assert black_p.attack(4 + 7j, 5 + 6j)[0]


def test_king_moving():
    assert white_k.move_to(2 + 2j, 2 + 3j)[0]
    assert white_k.move_to(2 + 2j, 3 + 3j)[0]
    assert white_k.move_to(2 + 2j, 1 + 1j)[0]
    assert not white_k.move_to(2 + 2j, 2 + 4j)[0]


def test_queen_moving():
    assert white_q.move_to(1 + 3j, 1 + 7j)[0]
    assert white_q.move_to(2 + 5j, 1 + 4j)[0]


def test_bishop_moving():
    assert white_b.move_to(3 + 1j, 6 + 4j)[0]
    assert white_b.move_to(4 + 5j, 2 + 3j)[0]


def test_knight_moving():
    assert white_n.move_to(2 + 1j, 3 + 3j)[0]
    assert white_n.move_to(2 + 1j, 1 + 3j)[0]


def test_bishop_trajectory():
    assert white_b.move_to(3 + 3j, 8 + 8j)[2] == [4 + 4j, 5 + 5j, 6 + 6j, 7 + 7j, 8 + 8j]
    assert white_b.move_to(3 + 3j, 1 + 1j)[2] == [2 + 2j, 1 + 1j]
    assert white_b.move_to(3 + 3j, 1 + 5j)[2] == [2 + 4j, 1 + 5j]
    assert white_b.move_to(3 + 3j, 5 + 1j)[2] == [4 + 2j, 5 + 1j]
    assert white_b.move_to(3 + 5j, 1 + 7j)[2] == [2 + 6j, 1 + 7j]


def test_pawn_trajectory():
    assert white_p.move_to(2 + 2j, 2 + 4j)[2] == [2 + 3j, 2 + 4j]
    assert black_p.move_to(2 + 7j, 2 + 6j)[2] == [2 + 6j]


def test_king_trajectory():
    assert white_k.move_to(2 + 3j, 1 + 3j)[2] == [1 + 3j]
    assert white_k.move_to(2 + 3j, 3 + 2j)[2] == [3 + 2j]


def test_queen_trajectory():
    assert white_q.move_to(1 + 1j, 6 + 6j)[2] == [2 + 2j, 3 + 3j, 4 + 4j, 5 + 5j, 6 + 6j]
    assert white_q.move_to(1 + 1j, 5 + 1j)[2] == [2 + 1j, 3 + 1j, 4 + 1j, 5 + 1j]
    assert white_q.move_to(3 + 5j, 6 + 2j)[2] == [4 + 4j, 5 + 3j, 6 + 2j]


def test_knight_trajectory():
    assert white_n.get_trajectory(3 + 3j, 4 + 5j) == [3 + 4j, 3 + 5j, 4 + 5j]
    assert white_n.get_trajectory(4 + 4j, 6 + 3j) == [5 + 4j, 6 + 4j, 6 + 3j]
    assert white_n.get_trajectory(4 + 4j, 6 + 5j) == [5 + 4j, 6 + 4j, 6 + 5j]
    assert white_n.get_trajectory(4 + 4j, 5 + 2j) == [4 + 3j, 4 + 2j, 5 + 2j]
    assert white_n.get_trajectory(4 + 4j, 3 + 2j) == [4 + 3j, 4 + 2j, 3 + 2j]
    assert white_n.get_trajectory(4 + 4j, 2 + 3j) == [3 + 4j, 2 + 4j, 2 + 3j]
    assert white_n.get_trajectory(4 + 4j, 2 + 5j) == [3 + 4j, 2 + 4j, 2 + 5j]
    assert white_n.get_trajectory(4 + 4j, 3 + 6j) == [4 + 5j, 4 + 6j, 3 + 6j]


template = lambda x: (cb.chess_board.get(x), cb.chess_board.get(x).fraction if cb.chess_board.get(x) else None)
def test_get_probable_move_pawns_and_bishops():
    assert white_p.get_probable_attack_trajectory(2 + 2j, template) == {1 + 3j, 3 + 3j}
    assert black_p.get_probable_attack_trajectory(2 + 7j, template) == {1 + 6j, 3 + 6j}
    cb.move(2 + 2j, 2  + 4j)
    cb.move(2 + 7j, 2 + 5j)
    cb.move(3 + 1j, 2 + 2j)
    assert white_b.get_probable_attack_trajectory(2 + 2j, template) == {1 + 3j, 3 + 3j, 4 + 4j, 5 + 5j, 6 + 6j, 7 + 7j, 3 + 1j}
    cb.move(1 + 7j, 1 + 6j)
    cb.move(2 + 2j, 5 + 5j)
    assert white_b.get_probable_attack_trajectory(5 + 5j, template) == {4 + 6j, 6 + 6j, 4 + 4j, 3 + 3j, 2 + 2j, 6 + 4j, 7 + 3j, 7 + 7j, 3 + 7j}

def test_get_probable_move_knights():
    assert white_n.get_probable_attack_trajectory(2 + 1j, template) == {1 + 3j, 3 + 3j}
    cb.move(2 + 1j, 3 + 3j)
    cb.move(8 + 7j, 8 + 6j)
    cb.move(3 + 3j, 5 + 4j)
    assert white_n.get_probable_attack_trajectory(5 + 4j, template) == {3 + 3j, 7 + 3j, 7 + 5j,6 + 6j, 4 + 6j, 3 + 5j}