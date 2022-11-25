# main.py implements simple sat solver and writes DIMACS file with output.

# imports
from src.algorithms.dpll import DPLL
from src.classes.SAT import SAT
import time
import os
import csv
from sys import argv

if __name__ == "__main__":

    heuristic = "DPLL"
    file = 5 

def run(heuristic, file):
    path = f"/home/m_rosa/SAT/SAT_solver/resources/sudokus/{file}_sudoku.cnf"
    # run sat solver for 1 sudoku
    sat = SAT(path)
    sat.input()
    dpll_sud = DPLL(sat)
    bool, count, set_variables =  dpll_sud.run(sat.variables, sat.clauses, sat.set_variables, False, None, heuristic)
    return heuristic, count, file, set_variables

def output(set_variables):
    # Make DIMACS file

    with open("solution.cnf", "w") as f:
        f.write(f"p cnf {len(set_variables)} {len(set_variables)}\n")
        for key in set_variables.keys(): 
            f.write('%s\n' % (key))

if __name__ == "__main__":
        # check command line
    if len(argv) != 3:
        print("Usage: python3 main.py [sudoku_number: int] MOM/JW/DPLL")
        exit(1)
    # Load the requested files
    if len(argv) == 3:
        file = argv[1]
        heuristic = str(argv[2])

    results = run(heuristic, file)
    output(results[3])