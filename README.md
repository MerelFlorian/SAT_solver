# SAT solver 
## Merel Florian

## Purpose
This program has implemented a SAT solver that can solve any SAT-problem. Heuristics that can be used are Maximum Occurrences in clauses of Minimum Size (MOM) and Jorslow-Wang(JW). Other features include a stats.py file to run statistics based on our results and multi.py to run multiprocessing. To see how to run that basic SAT_solver for one sudoku, see usage.

## Getting Started

### Requirements basic SAT solver
- Python 3.8.10

### Further requirements (see requirements.txt in SAT_solver folder):
matplotlib==3.4.2
numpy==1.20.3
pandas==1.2.4
pingouin==0.5.2
scikit_posthocs==0.7.0
scipy==1.8.0
seaborn==0.12.1
statannot==0.2.3

### Usage basic sudoku solver     
1. Usage: python3 main.py [Sudoku number: (int)][MOM/JW/DPLL] 
    - example: python3 main.py 1 MOM
2. open solution.cnf to see DIMACS output file

### Usage stats
1. change into directory "stats": cd stats
2. run "python3 stats.py"

### Usage multi.py (multiprocessing)
#### For multiprocessing 3 versions of DPLL at the same time (DPLL, JW, MOM)
1. Change "START" variable to where you want to start in the sudoku files.
2. Change "TOTAL" to 3x(amount of sudokus to solve). So to run multi.py for sudokus 250-500: TOTAL = 750
3. run "python3 multi.py"
