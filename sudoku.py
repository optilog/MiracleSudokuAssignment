from optilog.modelling import *
from optilog.formulas import CNF
from optilog.solvers.sat import Glucose41
from sudoku_base import read_sudoku, var, visualize
import sys
from sys import exit


def solve(path):
    p = Problem()
    sudoku = read_sudoku(path)
    SUBGROUP_LENGTH = sudoku.subgroup_length
    SUBGROUP_HEIGHT = sudoku.subgroup_height
    VALUES = SUBGROUP_HEIGHT * SUBGROUP_LENGTH

    # Fixed
    for j in range(VALUES):
        for i in range(VALUES):
            v = sudoku.cells[i][j]
            if v is not None:
                p.add_constr(var(i, j, v))

    # Cells

    # Row

    # Column

    # Subgroup

    # Miracle Sudoku

    # Cells reachable with a knight move can not contain same value
    # - YOUR CODE HERE -

    # Cells reachable with a king move can not contain same value
    # - YOUR CODE HERE -

    # Cells reachable with a king move (without diagonal one) can not contain a consecutive value
    # - YOUR CODE HERE -

    cnf = p.to_cnf_dimacs()

    s = Glucose41()
    s.add_clauses(cnf.clauses)
    has_solution = s.solve()
    print("Has solution?", has_solution)

    if has_solution:
        interp = s.model()
        visualize(cnf.decode_dimacs(interp), sudoku)


if __name__ == "__main__":
    solve(sys.argv[1])
