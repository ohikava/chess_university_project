from Chesspiece import Rook, Queen, Knight, King, Pawn, Bishop

horizontal = {"a", "b", "c", "d", "e", "f", "g", "h"}
vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]



class Chess:
    def __init__(self):
        self.chess_board = {
            k + v: None for k in horizontal for v in vertical
        }

        for i in horizontal:
            self.chess_board[i + "2"] = Pawn(True, i + "2")
            self.chess_board[i + "7"] = Pawn(False, i + "7")

        self.chess_board['a1'] = Rook(True, 'a1')
        self.chess_board['b1'] = Knight(True, 'b1')
        self.chess_board['c1'] = Bishop(True, 'c1')
        self.chess_board['d1'] = Queen(True, 'd1')
        self.chess_board['e1'] = King(True, 'e1')
        self.chess_board['f1'] = Bishop(True, 'f1')
        self.chess_board['g1'] = Knight(True, 'g1')
        self.chess_board['h1'] = Rook(True, 'h1')

        self.chess_board['a8'] = Rook(False, 'a8')
        self.chess_board['b8'] = Knight(False, 'b8')
        self.chess_board['c8'] = Bishop(False, 'c8')
        self.chess_board['d8'] = Queen(False, 'd8')
        self.chess_board['e8'] = King(False, 'e8')
        self.chess_board['f8'] = Bishop(False, 'f8')
        self.chess_board['g8'] = Knight(False, 'g8')
        self.chess_board['h8'] = Rook(False, 'h8')


    def restart(self):
        self.__init__()


    def render_chessboard(self):
        print('  ', end=" ")
        for k in sorted(list(horizontal)):
            print(k + "", end=" ")
        print(" ")
        for i in sorted(list(vertical))[::-1]:
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
