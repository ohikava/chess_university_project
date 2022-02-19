from Chesspiece import Pawn, King, Queen, Bishop, Rook, Knight

white_p = Pawn(True)
black_p = Pawn(False)
white_k = King(True)
white_q = Queen(True)
white_b = Bishop(True)
white_r = Rook(True)
white_n = Knight(True)


def test_1():
    assert white_p.move_to(2 + 2j, 2 + 3j)[0]


def test_2():
    assert white_p.move_to(2 + 2j, 2 + 4j, True)[0]


def test_3():
    assert not white_p.move_to(2 + 2j, 2 + 1j)[0]


def test_4():
    assert black_p.move_to(2 + 7j, 2 + 6j)[0]


def test_5():
    assert black_p.move_to(3 + 6j, 3 + 5j)[0]


def test_6():
    assert not black_p.move_to(2 + 7j, 2 + 5j, True)[0]


def test_7():
    assert white_p.attack(4 + 7j, 5 + 8j)[0]


def test_8():
    assert black_p.attack(4 + 7j, 5 + 6j)[0]


def test_9():
    assert white_k.move_to(2 + 2j, 2 + 3j)[0]


def test_10():
    assert white_k.move_to(2 + 2j, 3 + 3j)[0]


def test_11():
    assert white_k.move_to(2 + 2j, 1 + 1j)[0]


def test_12():
    assert not white_k.move_to(2 + 2j, 2 + 4j)[0]


def test_13():
    assert white_q.move_to(1 + 3j, 1 + 7j)[0]


def test_14():
    assert white_q.move_to(2 + 5j, 1 + 4j)[0]


def test_15():
    assert white_b.move_to(3 + 1j, 6 + 4j)[0]


def test_15():
    assert white_b.move_to(4 + 5j, 2 + 3j)[0]


def test_16():
    assert white_n.move_to(2 + 1j, 3 + 3j)[0]


def test_17():
    assert white_n.move_to(2 + 1j, 1 + 3j)[0]

def test_18():
    assert white_b.move_to(3 + 3j, 8 + 8j)[2] == [4 + 4j, 5 + 5j, 6 + 6j, 7 + 7j, 8 + 8j]

def test_19():
    assert white_b.move_to(3 + 3j, 1 + 1j)[2] == [2 + 2j, 1 + 1j]

def test_20():
    assert white_b.move_to(3 + 3j, 1 + 5j)[2] == [2 + 4j, 1 + 5j]

def test_21():
    assert white_b.move_to(3 + 3j, 5 + 1j)[2] == [4 + 2j, 5 + 1j]

def test_22():
    assert white_p.move_to(2 + 2j, 2 + 4j)[2] == [2 + 3j, 2 + 4j]

def test_23():
    assert black_p.move_to(2 + 7j, 2 + 6j)[2] == [2 + 6j]