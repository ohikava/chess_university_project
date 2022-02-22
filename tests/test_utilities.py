from utilities import chess_notation_2_complex_number, complex_number_2_chess_notation


def test_chess_notation_2_complex_number():
    assert 2 + 3j == chess_notation_2_complex_number('b3')
    assert 1 + 1j == chess_notation_2_complex_number('a1')
    assert 8 + 5j == chess_notation_2_complex_number('h5')


def test_complex_number_2_chess_notation():
    assert 'h5' == complex_number_2_chess_notation(8 + 5j)
    assert 'a1' == complex_number_2_chess_notation(1 + 1j)
    assert 'b3' == complex_number_2_chess_notation(2 + 3j)
