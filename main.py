from simple_sudoku import SimpleSudoku

if __name__ == '__main__':
    sudoku = SimpleSudoku(dim=9, file_dir='board_inits/easy_board.txt')
    sudoku.solve_simple_back_tracking()
    sudoku.show_board()
