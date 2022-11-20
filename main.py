# imports
from src.algorithms.dpll import DPLL
from src.classes.SAT import SAT
import time
import os

if __name__ == "__main__":

    HEURISTIC = "MOM"

    line = []
    start = time.time()
        
    # run algorithm for all sudoku's
    for file in os.listdir("/home/m_rosa/SAT/SAT_solver/resources/sudokus/"):
        sat = SAT("/home/m_rosa/SAT/SAT_solver/resources/sudokus/" + file)
        sat.input()
        dpll_sud = DPLL(sat)
        bool, count =  dpll_sud.run(sat.variables, sat.clauses, sat.set_variables, False, None, HEURISTIC, 2)
    
        # save stats file 
        line.append(str(count))

    with open('stats/stats.txt', 'w') as f:
        f.write(HEURISTIC + ", ")     
        for item in line:
            f.write(item + ", ")

    print(time.time() - start)