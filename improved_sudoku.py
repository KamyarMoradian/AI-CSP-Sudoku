from sudoku import Sudoku


class ImprovedSudoku(Sudoku):
    def __init__(self, dim, file_dir):
        super().__init__(dim, file_dir)
        self.rv = self.get_remaining_values()

    def solve_improved_back_tracking_util(self):
        # TODO: Complete method
        pass

    def solve_improved_back_tracking(self):
        self.rv = self.get_remaining_values()
        return self.solve_improved_back_tracking_util()

