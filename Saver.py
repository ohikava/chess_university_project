import uuid
from Chessboard import Chessboard
from typing import Type
from glob import glob

class Saver:
    def __init__(self, cb: Type[Chessboard]):
        self.quick_saves = []
        self.name = uuid.uuid1()
        self.cb = cb

    def restart(self):
        self.__init__(self.cb)

    """
    This method saves a current array quick_saves in separate file in folder saves/ with name from 
    variable self.name
    before saving аit also translates moves from my notation to full notation with Chessboard's method
    to_full_notation.
    """

    def quicksave(self):
        pass

    def add(self, move: tuple[complex, complex]) -> None:
        self.quick_saves.append(move)

    """
    This method loads a file with full/short notation, translates it with Chessboard methods
    from_full_notation, from_short_notation and puts it into quick_saves_variable
    it also set self.name to name of the file
    """

    def load_file(self, name: str) -> None:
        with open(f"notations/{name}.txt") as file:
            self.quick_saves = []
            while raw_string := file.readline():
                try:
                    i = raw_string.rstrip()
                    i = i.split()
                    self.quick_saves.append(self.cb.short_notation_to_complex_numbers(i[1]))
                    self.cb.queue = not self.cb.queue
                    self.quick_saves.append(self.cb.short_notation_to_complex_numbers(i[2]))
                    self.cb.queue = not self.cb.queue
                except:
                    print(i[0])

            self.name = name
            self.cb.queue = True


    """
    This method uses a chessboard instance and loads quicksave to it
    """

    def load_quicksave(self) -> None:
        self.cb.restart()
        for i in self.quick_saves:
            self.cb.move(i[0], i[1])

    def back_one_move(self) -> None:
        self.quick_saves.pop()
        self.quick_saves.pop()
        self.load_quicksave()

    def get_list_savings(self):
        res = list(map(lambda x: x.replace('.txt', '').replace('notations\\', ''), glob('notations/*')))
        return res

if __name__ == "__main__":
    cb = Chessboard()
    s = Saver(cb)
    s.load_file('notations/test1.txt')