from simple_sudoku import SimpleSudoku
from statistics import mean
from improved_sudoku import ImprovedSudoku
import time
N = 10


# def test(solver, mode):
#     times = []
#     nodes = []
#     for i in range(N):
#         start_time = time.time()
#         solver.solve(mode=mode)
#         times.append(time.time() - start_time)
#         print(time.time() - start_time)
#         nodes.append(solver.expanded_nodes)
#         if i == N - 1:
#             solver.show_board()
#     print("--- %s seconds ---" % (mean(times)))
#     print("--- %s nodes expanded ---" % (mean(nodes)))


if __name__ == '__main__':
    sudoku_mode = input('Enter mode of sudoku [easy, medium, hard, expert]: ')
    print("\n---------------------------------------------------------\n")

    print("--- Simple Backtracking : Late Test ---")
    simple_sudoku_obj = SimpleSudoku(dim=9, file_dir=f'board_inits/{sudoku_mode}_board.txt')
    start_time = time.time()
    simple_sudoku_obj.solve(mode='LT')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s nodes expanded ---" % (simple_sudoku_obj.expanded_nodes))
    simple_sudoku_obj.show_board()
    # test(simple_sudoku_obj, mode='LT')

    print("\n---------------------------------------------------------\n")

    print("--- Simple Backtracking : Early Test ---")
    simple_sudoku_obj = SimpleSudoku(dim=9, file_dir=f'board_inits/{sudoku_mode}_board.txt')
    start_time = time.time()
    simple_sudoku_obj.solve(mode='ET')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s nodes expanded ---" % (simple_sudoku_obj.expanded_nodes))
    simple_sudoku_obj.show_board()
    # test(simple_sudoku_obj, mode='ET')

    print("\n---------------------------------------------------------\n")

    print("--- Arc Consistency ---")
    improved_sudoku_obj = ImprovedSudoku(dim=9, file_dir=f'board_inits/{sudoku_mode}_board.txt')
    start_time = time.time()
    improved_sudoku_obj.solve(mode='AC')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s nodes expanded ---" % (improved_sudoku_obj.expanded_nodes))
    improved_sudoku_obj.show_board()
    # test(improved_sudoku_obj, mode='AC')

    print("\n---------------------------------------------------------\n")

    print("--- Arc Consistency & MRV ---")
    improved_sudoku_obj = ImprovedSudoku(dim=9, file_dir=f'board_inits/{sudoku_mode}_board.txt')
    start_time = time.time()
    improved_sudoku_obj.solve(mode='MRV')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s nodes expanded ---" % (improved_sudoku_obj.expanded_nodes))
    improved_sudoku_obj.show_board()
    # test(improved_sudoku_obj, mode='MRV')
