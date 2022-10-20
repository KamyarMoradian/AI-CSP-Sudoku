import Sudoku

if __name__ == '__main__':
    sudoku = Sudoku.Sudoku(dim=9, file_dir='board_inits/medium_board.txt')
    sudoku.solve_simple_back_tracking()
    sudoku.show_board()
