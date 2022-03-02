from Saver import Saver
from Chessboard import Chessboard

cb = Chessboard()
s = Saver(cb)


def test_add():
    s.add((2 + 2j, 2 + 3j))
    s.add((2 + 7j, 2 + 6j))
    assert s.quick_saves == [(2 + 2j, 2 + 3j), (2 + 7j, 2 + 6j)]
    s.add((2 + 3j, 2 + 4j))
    s.add((2 + 6j, 2 + 5j))
    assert s.quick_saves == [(2 + 2j, 2 + 3j), (2 + 7j, 2 + 6j), (2 + 3j, 2 + 4j), (2 + 6j, 2 + 5j)]


def test_back_one_move():
    s.back_one_move()
    assert s.quick_saves == [(2 + 2j, 2 + 3j), (2 + 7j, 2 + 6j)]
