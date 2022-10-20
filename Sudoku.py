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
        for i in range(self.dim):
            for j in range(self.dim):
                if self.board[i][j] == '0':
                    return i, j
        return None, None

    def is_safe_row(self, row, candidate) -> bool:
        for i in range(self.dim):
            if self.board[row][i] == str(candidate):
                return False
        return True

    def is_safe_column(self, col, candidate) -> bool:
        for i in range(self.dim):
            if self.board[i][col] == str(candidate):
                return False
        return True

    def is_safe_region(self, row, col, candidate) -> bool:
        row_region = row - row % 3
        col_region = col - col % 3
        for i in range(row_region, row_region + 3):
            for j in range(col_region, col_region + 3):
                if self.board[i][j] == str(candidate):
                    return False
        return True

    def is_safe(self, row, col, candidate):
        if not self.is_safe_row(row, candidate):
            return False
        if not self.is_safe_column(col, candidate):
            return False
        if not self.is_safe_region(row, col, candidate):
            return False
        return True

    def solve_simple_back_tracking(self):
        self.show_board()
        print("---------------------------------------------------------------------")
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
