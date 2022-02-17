from utilities import chess_notation_2_complex_number, complex_number_2_chess_notation


def test1():
    assert 2 + 3j == chess_notation_2_complex_number('b3')


def test2():
    assert 1 + 1j == chess_notation_2_complex_number('a1')


def test3():
    assert 8 + 5j == chess_notation_2_complex_number('h5')


def test4():
    assert 'h5' == complex_number_2_chess_notation(8 + 5j)

def test5():
    assert 'a1' == complex_number_2_chess_notation(1 + 1j)


def test6():
    assert 'b3' == complex_number_2_chess_notation(2 + 3j)
