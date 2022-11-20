# imports
from src.algorithms.dpll import DPLL
from src.classes.SAT import SAT
import time
import os

if __name__ == "__main__":

    HEURISTIC = "NONE"
    dir = "/home/m_rosa/SAT/SAT_solver/resources/sudokus_extra/"

    line = []
    start = time.time()
    counter = 0
        
    # run algorithm for all sudoku's
    for file in os.listdir(dir):
        counter += 1
        print("sudoku = ", file)
        if counter % 50 == 0: 
            print(counter, "ARE COMPLETED OUT OF 1011")
        sat = SAT(dir + file)
        sat.input()
        dpll_sud = DPLL(sat)
        bool, count =  dpll_sud.run(sat.variables, sat.clauses, sat.set_variables, False, None, HEURISTIC, 2)
    
        
        line.append(str(count))
   
    # save stats file  

    with open('stats/results/stats.txt', 'w') as f:
        f.write(HEURISTIC + " ")     
        for item in line:
            f.write(item + " ")
    f.close()

    print(time.time() - start)