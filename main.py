horizontal = {"a", "b", "c", "d", "e", "f", "g", "h"}
vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]


class Chess:
    def __init__(self):
        self.chess_board = {
            k + v: None for k in horizontal for v in vertical
        }

        for i in horizontal:
            self.chess_board[i + "2"] = "P"
            self.chess_board[i + "7"] = "p"

        self.chess_board['a1'] = "R"
        self.chess_board['b1'] = "N"
        self.chess_board['c1'] = "B"
        self.chess_board['d1'] = "Q"
        self.chess_board['e1'] = "K"
        self.chess_board['f1'] = "B"
        self.chess_board['g1'] = "N"
        self.chess_board['h1'] = "R"

        for i in horizontal:
            self.chess_board[i + "8"] = self.chess_board[i + "1"].lower()

    def restart(self):
        self.__init__()

    def render_chessboard(self):
        print('  ', end=" ")
        for k in sorted(list(horizontal)):
            print(k + "", end=" ")
        print(" ")
        for i in sorted(list(vertical)):
            print(i, end="  ")
            for k in sorted(list(horizontal)):
                if self.chess_board[k+i]:
                    print(self.chess_board[k + i], end=" ")
                else:
                    print(".", end=" ")
            print(" " + i)
        print('  ', end=" ")
        for k in sorted(list(horizontal)):
            print(k + "", end=" ")



if __name__ == "__main__":
    cb = Chess()
    cb.render_chessboard()
