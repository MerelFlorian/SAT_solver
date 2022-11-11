# imports
from code.algorithms.dpll import DPLL
from code.game.sudoku import Sudoku

if __name__ == "__main__":
    sudoku = Sudoku("/Users/merelflorian/Documents/AI/KR/SAT_solver/resources/sudoku1.cnf")
    sudoku.input()
    dpll_sud = DPLL(sudoku)
    dpll_sud.run()