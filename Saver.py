import uuid
from Chessboard import Chessboard
from typing import Type


class Saver:
    def __init__(self, cb: Type[Chessboard]):
        self.quick_saves = []
        self.white_move = None
        self.black_move = None
        self.name = uuid.uuid1()
        self.cb = cb

    """
    This method saves a current array quick_saves in separate file in folder saves/ with name from 
    variable self.name
    before saving it also translates moves from my notation to full notation with Chessboard's method
    to_full_notation.
    """

    def quicksave(self):
        pass

    def add(self, move: tuple[complex, complex]) -> None:
        if not self.white_move:
            self.white_move = move
        else:
            self.black_move = move
            self.quick_saves.append((self.white_move, self.black_move))
            self.white_move = None
            self.black_move = None

    """
    This method loads a file with full/short notation, translates it with Chessboard methods
    from_full_notation, from_short_notation and puts it into quick_saves_variable
    it also set self.name to name of the file
    """

    def load_file(self, name: str) -> None:
        pass

    """
    This method uses a chessboard instance and loads quicksave to it
    """
    def load_quicksave(self) -> None:
        pass

    def back_one_move(self) -> None:
        self.quick_saves.pop()
        self.load_quicksave()


if __name__ == "__main__":
    s = Saver()
