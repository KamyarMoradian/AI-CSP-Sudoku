from sudoku import Sudoku


class SimpleSudoku(Sudoku):
    def __init__(self, dim, file_dir):
        super().__init__(dim, file_dir)

    def get_next_location(self) -> (int, int):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.board[i][j] == '0':
                    return i, j
        return None, None

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
