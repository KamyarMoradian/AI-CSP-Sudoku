# TODO: create class sudoku. with following methods:
# 	    *solveSimpleBackTracking -> to run backtracking on sudoku
# 	    *getNextLocation -> to get next empty square
#    	*isSafe(i, j, choice) -> to check if it doesn't violate constraints

from random import choice

class Sudoku:

    def __init__(self, dim, file_dir):
        self.board = []
        self.dim = dim
        self.expanded_nodes = 0
        self.initialize_board(file_dir)

    def initialize_board(self, file_dir):
        with open(file_dir) as fh:
            content = fh.readlines()
            self.board = [list(x.strip()) for x in content]

    def show_board(self):
        for i in range(9):
            for j in range(9):
                if j != 8:
                    print(self.board[i][j], end=' | ')
                else:
                    print(self.board[i][j], end='')
            print('')

    def get_next_location(self) -> (int, int):
        pass

    def is_safe(self, i, j, candidate):
        pass

    def solve_simple_back_tracking(self):
        next_location = self.get_next_location()
        if next_location[0] is None:
            return True
        else:
            self.expanded_nodes += 1
            for candidate in range(1, self.dim + 1):
                if self.is_safe(next_location[0], next_location[1], candidate):
                    self.board[next_location[0]][next_location[1]] = str(candidate)
                    if self.solve_simple_back_tracking():
                        return True
                    self.board[next_location[0]][next_location[1]] = '0'
        return False
