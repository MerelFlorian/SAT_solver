# imports
from code.algorithms.dpll import DPLL
from code.game.SAT import SAT

if __name__ == "__main__":
    sat = SAT("/Users/merelflorian/Documents/AI/KR/SAT_solver/resources/sudoku1.cnf")
    sat.input()
    dpll_sud = DPLL(sat)
    print(dpll_sud.run(sat.variables, sat.clauses, sat.set_variables, False, None))