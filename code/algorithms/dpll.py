# Implements a basic algorithm that loops through all variables in SAT and tries all combinations of boolean values



class DPLL:
    """
    Basic SAT solver using DPLL 
    """
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def simplify(self):
         for clause in self.sudoku.clauses:
            # check for empty (sets of) clauses 
            if len(self.sudoku.clauses) == 0:
                return True
           
            # unit clause
            if len(clause) == 0:
                return False   
            # check for empty clause
            elif len(clause) == 1: 
                self.sudoku.variables[clause[0]] = True
            # pure literals
            
                
    def run(self):
        self.simplify