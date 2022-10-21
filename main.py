from simple_sudoku import SimpleSudoku
from improved_sudoku import ImprovedSudoku
import time


if __name__ == '__main__':
    start_time = time.time()
    simple_sudoku_obj = SimpleSudoku(dim=9, file_dir='board_inits/expert_board.txt')
    simple_sudoku_obj.solve_simple_back_tracking()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s counts ---" % simple_sudoku_obj.expanded_nodes)
    simple_sudoku_obj.show_board()

    start_time = time.time()
    improved_sudoku_obj = ImprovedSudoku(dim=9, file_dir='board_inits/expert_board.txt')
    improved_sudoku_obj.solve_ac3()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s counts ---" % improved_sudoku_obj.expanded_nodes)
    improved_sudoku_obj.show_board()
