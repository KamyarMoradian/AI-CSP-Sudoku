from sudoku import Sudoku
from copy import deepcopy
from collections import deque


class ImprovedSudoku(Sudoku):
    def __init__(self, dim, file_dir):
        super().__init__(dim, file_dir)
        self.arcs = deque([])
        self.initialize_arcs()
        self.rv = self.get_remaining_values()

    @staticmethod
    def calculate_index(node):
        return node[0] * 9 + node[1]

    def initialize_arcs(self):
        for i in range(9):
            for j in range(9):
                self.add_neighbors_to_arcs((i, j))

    def add_neighbors_to_arcs(self, node):
        for i in range(9):
            if i != node[1]:
                self.arcs.append(((node[0], i), node))
            if i != node[0]:
                self.arcs.append(((i, node[1]), node))

        row_start = node[0] - node[0] % 3
        col_start = node[1] - node[1] % 3

        for i in range(3):
            for j in range(3):
                if node[0] == row_start + i and node[1] == col_start + j:
                    continue
                self.arcs.append(((row_start + i, col_start + j), node))

    def apply_ac3(self):
        while len(self.arcs) > 0:
            tail_node, head_node = self.arcs.popleft()
            if self.remove_inconsistent_neighbors(tail_node, head_node):
                if len(self.rv[self.calculate_index(tail_node)]) == 0:
                    return False
                self.add_neighbors_to_arcs(tail_node)
        return True

    def remove_inconsistent_neighbors(self, tail_node, head_node):
        tail_index = self.calculate_index(tail_node)
        head_index = self.calculate_index(head_node)
        if self.board[tail_node[0]][tail_node[1]] != '0' or len(self.rv[head_index]) > 1:
            return False
        current_value = self.rv[head_index][0]
        for value in self.rv[tail_index]:
            if value == current_value:
                self.rv[tail_index].remove(value)
                return True
        return False

    def get_next_location(self) -> (int, int):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.board[i][j] == '0':
                    return i, j
        return None, None

    def solve_ac3(self):
        self.expanded_nodes += 1
        next_location = self.get_next_location()
        if next_location[0] is None:
            return True
        index = self.calculate_index(next_location)
        primary_rv = deepcopy(self.rv)
        for candidate in self.rv[index]:
            self.board[next_location[0]][next_location[1]] = candidate
            self.rv[index] = [candidate]
            self.add_neighbors_to_arcs(node=next_location)
            if not self.apply_ac3():
                self.arcs.clear()
                self.rv = deepcopy(primary_rv)
                continue
            self.rv[index] = ['x']
            if self.solve_ac3():
                return True
            self.rv = deepcopy(primary_rv)
            self.board[next_location[0]][next_location[1]] = '0'
        self.board[next_location[0]][next_location[1]] = '0'
        return False
