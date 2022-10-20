class Sudoku:
    def __init__(self, dim, file_dir):
        self.board = []
        self.dim = dim
        self.expanded_nodes = 0
        self.rv = []
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

    def get_domain(self, row, col):
        # 0. initialize array candidates and populate it with values in range 1 to dim (which is 9 in this scenario)
        candidates = [str(i) for i in range(1, self.dim + 1)]
        # 1. remove occurred values in row
        for i in range(self.dim):
            if self.board[row][i] != '0':
                if self.board[row][i] in candidates:
                    candidates.remove(self.board[row][i])
        # 2. remove occurred values in column
        for i in range(self.dim):
            if self.board[i][col] != '0':
                if self.board[i][col] in candidates:
                    candidates.remove(self.board[i][col])
        # 3. remove occurred values in region
        row_region = row - row % 3
        col_region = col - col % 3
        for i in range(row_region, row_region + 3):
            for j in range(col_region, col_region + 3):
                if self.board[i][j] != 0:
                    if self.board[i][j] in candidates:
                        candidates.remove(self.board[i][j])
        # 4. return all available values for board[row][col]
        return candidates

    def get_remaining_values(self):
        new_rv = []
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] != '0':
                    new_rv.append(['x'])
                else:
                    new_rv.append(self.get_domain(row, col))
        return new_rv
