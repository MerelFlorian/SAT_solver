# Implements a basic algorithm that loops through all variables in SAT and tries all combinations of boolean values

class DPLL:
    """
    Basic SAT solver using DPLL 
    """
    def __init__(self, sudoku):
        self.sudoku = sudoku
        # self.removed_clauses = []

    def unit_clause(self, clause):
        """
        Returns true if clause is unit clause
        """
        if len(clause) == 1: 
            return True
        else: 
            return False

    def set_unit_clause(self, clause, statement):
        if statement:
            if "-" in clause:
                self.sudoku.variables[clause] = False
            else:
                self.sudoku.variables[clause[0]] = True
        else:
            return 

    def empty_set_clauses(self):
        """ 
        Checks for empty (sets of) clauses, returns true if so.
        """
        if len(self.sudoku.clauses) == 0: # check if correct
            return True
        else:
            return False

    def empty_clause(self, clause):
        """
        Returns True if clause is empty
        """
        if len(clause) == 0:
            return True 
        else: 
            return False
    
    def tautology(self, clause, literal):
        """
        returns True if clause contains tautology
        """
        if "-" in literal and literal.replace("-", "") in clause:
            return True
        else:
            return False
    
    def pure_lits(self, literal):
        if literal.replace("-", "") not in self.sudoku.count_literals.keys() and "-" in literal:
            return False
        elif "-" + literal not in self.sudoku.count_literals.keys() and "-" not in literal:
            return True
        else:
            return None
    
    def shorten_clause(clause, literal):
        self.sudoku.clauses[clause].pop(literal)
        return
          
    def run(self):
        """
        Runs dpll algorithm by systematically checking all values for literals, with backtracking.
        """
        # first check for empty set of clauses
        if self.empty_set_clauses():
            return True

        # loop through all clauses 
        for clause in self.sudoku.clauses:
            
            # check for empty clause 
            if self.empty_clause(clause):
                return False 

            # check unit clause and set it and count lit if True 
            if self.set_unit_clause(clause, self.unit_clause(clause)):
                self.sudoku.count_lits(literal)
                continue
            
            for literal in clause:
                # check for tautology and count literal if clause is not removed
                if self.tautology(clause, literal):
                    self.sudoku.clauses.remove(clause)
                else: 
                    self.sudoku.count_lits(literal)
        
        # check for pure clause
        for clause in self.sudoku.clauses:
            for literal in clause:
                
                if self.pure_lits(literal):
                    self.sudoku.variables[literal] = True
                    self.sudoku.clauses.remove(clause)
                elif self.pure_lits(literal) == False:
                    self.sudoku.variables[literal] = False
                    self.sudoku.clauses.remove(clause)
                else: 
                    continue
        
        # chronological backtracking

        # deep copy

        # assign value

        # change clauses 

        # remove sat clauses

        # check for unit clause -> hard choice 

        # 






                


        
    

            
            

        

        


