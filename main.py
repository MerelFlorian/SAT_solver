# imports
from src.algorithms.dpll import DPLL
from src.game.SAT import SAT

if __name__ == "__main__":
    sat = SAT("/home/m_rosa/SAT/SAT_solver/resources/sudoku1.cnf")
    sat.input()
    dpll_sud = DPLL(sat)
    print(dpll_sud.run(sat.variables, sat.clauses, sat.set_variables, False, None, 0))