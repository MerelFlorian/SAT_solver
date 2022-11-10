# Implements a basic algorithm that loops through all variables in SAT and tries all combinations of boolean values

class DPLL:
    """
    Basic SAT solver using DPLL 
    """
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.count_literals = {}
        self.removed_clauses = []

    def simplify(self):
        """
        Simplifies CNF formula using pure literals, tautologies and unit clauses.
        Removes clause from sudoku clause list when satisfied
        Sets variable to True or False to satisfy in sudoku dict
        """
        
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
                self.sudoku.clauses.remove(clause)
                self.removed_clauses.append(clause)
                continue
            
            # handle tautology
            for literal in clause: 
                if clause in self.removed_clauses:
                    continue
                else: 
                    if "-" in literal and literal.replace("-", "") in clause:
                        self.sudoku.clauses.remove(clause)
                        self.removed_clauses.append(clause)
                        continue

                    # count literals
                    if literal not in self.count_literals.keys():
                        self.count_literals[literal] = [0, clause]
                    self.count_literals[literal][0] += 1

                    # handle pure clauses
                    if literal.replace("-", "") not in self.count_literals.keys() and "-" in literal:
                        self.sudoku.variables[literal.replace("-", "")] = False 
                        self.sudoku.clauses.remove(clause)
                        self.removed_clauses.append(clause)
                        continue
                    # elif "-" + literal not in self.count_literals.keys() and "-" not in literal:
                    #     self.sudoku.variables[literal] = True
                    #     self.sudoku.clauses.remove(clause)
                    #     self.removed_clauses.append(clause)
                        # continue
                    else:
                        continue
        return None
    
    # def dpll(self):
    #     """
    #     Runs dpll algorithm by systematically checking all values for literals, with backtracking.
    #     """
    #     for variable in self.sudoku.variables():


        
    def run(self):
        simple = self.simplify()

        # if simple == True or simple == False:
        #     return simple
        # else:
        #     self.dpll()