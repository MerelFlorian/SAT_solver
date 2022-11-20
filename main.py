# imports
from src.algorithms.dpll import DPLL
from src.classes.SAT import SAT
import time

if __name__ == "__main__":
    sat = SAT("/home/m_rosa/SAT/SAT_solver/resources/sudoku2 (1).cnf")
    sat.input()

    start = time.time()
    dpll_sud = DPLL(sat)
    print(dpll_sud.run(sat.variables, sat.clauses, sat.set_variables, False, None, 0, "MOM", 2))
    print(time.time() - start)