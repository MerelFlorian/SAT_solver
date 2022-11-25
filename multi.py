# implements multiprocessing

# imports
from src.algorithms.dpll import DPLL
from src.classes.SAT import SAT
from multiprocessing import Pool, cpu_count
import csv
from operator import itemgetter

def run(heuristic, file):
    path = f"/home/m_rosa/SAT/SAT_solver/resources/sudokus/{file}_sudoku.cnf"
    # run sat solver for 1 sudoku
    sat = SAT(path)
    sat.input()
    dpll_sud = DPLL(sat)
    bool, count =  dpll_sud.run(sat.variables, sat.clauses, sat.set_variables, False, None, heuristic)
    return heuristic, count, file
   
if __name__ == "__main__":
    START = 1 # Jiseon set this to 250, Ruby set this to 500
    TOTAL = 750
    with Pool(processes = cpu_count()) as pool:
        result = pool.starmap(run, [("DPLL" if i <= TOTAL/3 else "MOM" if i <= TOTAL*2/3 else "JW", i if i <= TOTAL/3 else i - TOTAL//3 if i <= TOTAL*2/3 else i - (TOTAL*2)//3) for i in range(1, TOTAL+1)])
        # result = pool.starmap(run, [("DPLL" if i < START + TOTAL/3 else "MOM" if i < START + TOTAL*2/3 else "JW", i if i < START + TOTAL/3 else i - TOTAL//3 if i < START + TOTAL*2/3 else i - (TOTAL*2)//3) for i in range(START, START + TOTAL)])

    result = sorted(result, key=itemgetter(1))
    print(result)
    with open("stats.csv", "w") as f:
        writer = csv.writer(f, delimiter =";", escapechar =' ',quoting=csv.QUOTE_NONE)
        # writer.writerows([[f"{'DPLL' if i == 1 else 'JW' if i == 2 else 'MOM'};{(r[0],r[2])}" if n == 0 else (r[0],r[2]) for n, r in enumerate(result[j:int((i*TOTAL/3))])] for i,j in zip(range(1,4), range(0, TOTAL, 3))])
        writer.writerows(result)
        
