# Implements a basic algorithm that loops through all variables in SAT and tries all combinations of boolean values

class DPLL:
    """
    Basic SAT solver using DPLL 
    """
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.count_literals = {}
        self.tautologies = {}

    def simplify(self):
        
        for clause in self.sudoku.clauses:
            # check for empty (sets of) clauses 
            if len(self.sudoku.clauses) == 0:
                return True
           
            # check for empty clause
            if len(clause) == 0:
                return False   
            # unit clause
            elif len(clause) == 1: 
                self.sudoku.variables[clause[0]] = True
            
            # count literals + handle tautology
            for literal in clause: 
                if "-" in literal and literal.replace("-", "") in clause:
                    self.tautologies[literal] = clause

                if literal not in self.count_literals.keys():
                    self.count_literals[literal] = [0, clause] 
                self.count_literals[literal][0] += 1

        # handle pure clauses 
        for literal in self.count_literals.keys():
            
            if literal.replace("-", "") not in self.count_literals.keys() and "-" in literal:
                self.sudoku.variables[literal.replace("-", "")] = False
            elif "-" + literal not in self.count_literals.keys() and "-" not in literal:
                self.sudoku.variables[literal] = True
        print(self.pure_literals)

  
    def run(self):
        self.simplify()