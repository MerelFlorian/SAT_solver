# Implements a basic algorithm that loops through all variables in SAT and tries all combinations of boolean values

# imports
import copy

class DPLL:
    """
    Basic SAT solver using DPLL 
    """
    def __init__(self, SAT):
        self.SAT = SAT
        self.split = False

    def pure_lit(self, variable: str, clauses: list) -> bool: 
        """
        Counts number of times a variable is present in all clauses (either with negation sign or without).
        Returns True if pure literal.
        Returns False if not pure literal.
        """
        neg = 0
        pos = 0
        # count amount of positive and negative instances of variable in clauses s
        for clause in clauses:
            for literal in clause: 
                if variable in literal and "-" in literal:
                    neg += 1
                elif variable in literal and "-" not in literal:
                    pos += 1
                else:
                    continue
                if neg > 0 and pos > 0:
                    return False, False
        if neg > 0 and pos == 0:
            return False, True
        elif pos > 0 and neg == 0:
            return True, True
        else:
            return False, False
    
    def opposite(self, literal: str) -> str:
        """
        Returns opposite of literal (111-> -111)
        """
        if "-" in literal:
            opposite = literal.replace("-", "")
        else:
            opposite = "-" + literal
        return opposite

    def unit_clause(self, clause: list) -> bool:
        """
        Returns true if clause is unit clause
        """
        if len(clause) == 1: 
            return True
        else: 
            return False
    
    def unit_propagation(self, unit_clause: list, set_variables: dict, clauses: list):
        """
        Sets unit clause to appropriate boolean and rm from unset variables
        """
        # sets variable to True or False
        if "-" not in unit_clause[0]: 
            set_variables[unit_clause[0]] = True

        # remove  or shorten clause from clauses
        opposite = self.opposite(unit_clause[0])
        new_unit_clauses = [] # lijst kan 2x dezelfde waarde hebben
        new_clauses = copy.deepcopy(clauses)
        removed_clauses = 0
        empty = False
        for clause, i in zip(clauses, range(0, len(clauses))):
            for variable in clause:
                if opposite == variable:  # somehow finds 2x 273 as new unit clause 
                    # shorten clause
                    new_clause, empty, new = self.shorten_clause(unit_clause[0], clause) # shortening works, does empty work?
                    new_clauses[i - removed_clauses] = new_clause

                    if empty == True:
                        return new_clauses, empty, new_unit_clauses

                    if new == True:
                        if new_clause not in new_unit_clauses: 
                            new_unit_clauses.append(new_clause)
                    
                elif unit_clause[0] == variable:
                    removed_clauses += 1
                    new_clauses.remove(clause)
        return new_clauses, empty, new_unit_clauses

    def empty_set_clauses(self, clauses: list) -> bool:
        """ 
        Checks for empty (sets of) clauses, returns true if so.
        """
        if len(clauses) == 0: # check if correct
            return True
        else:
            return False

    def empty_clause(self, clause: list) -> bool:
        """
        Returns True if clause is empty
        """
        if len(clause) == 0:
            return True 
        else: 
            return False
    
    def tautology(self, clause: list, literal: str) -> bool:
        """
        Returns True if clause contains tautology
        """
        if "-" in literal and literal.replace("-", "") in clause:
            return True
        else:
            return False
    
    def shorten_clause(self, literal: str, clause: list):
        """
        Makes a clause shorter, removing one literal from it.
        """

        new_clause = copy.deepcopy(clause)
        unit_clause = False
        empty = False
        
        if "-" in literal:
            new_clause.remove(literal.replace("-", ""))
        else:
            new_clause.remove("-"+ literal)

        if len(new_clause) == 0:
            empty = True
        elif len(new_clause) == 1:
            unit_clause = True

        return new_clause, empty, unit_clause

    def run(self, variables:list, clauses: list, set_variables: dict, split: bool, value: bool, run: int) -> bool:
        """
        Runs DPLL algorithm by systematically checking all values for literals, with backtracking.
        Input: variables(list), clauses(list), set_variables(dict), split(Bool), value(Bool)
        Output: CNF file with set variables.
        """
        count_lits = {}
        empty = False
        unit_clauses = []
        new_clauses = copy.deepcopy(clauses)
        remaining = copy.deepcopy(variables)
        removed = 0

        # set variable to true or false if not first run
        if split is not False: 
            variable = variables.pop()
            remaining.remove(variable)
            if value == False:
                variable = "-" + variable
            else:
                set_variables[variable] = True
        else:
            variable = None

        print("variable", variable)
        print(split, value)

        for clause, i in zip(clauses, range(0, len(clauses))):
            for literal in clause:
            
                # if variable is chosen make new set of clauses removing/shortening clauses with variable
                if variable != None:

                    # remove clause 
                    if variable == literal:
                        new_clauses.remove(clause)
                        removed += 1
                        continue
                    elif variable == self.opposite(literal):
                        # shorten clause
                        new_clause, empty, unit_clause = self.shorten_clause(variable, clause)
                        new_clauses[i - removed] = new_clause
                        if unit_clause == True and clause not in unit_clauses:
                            unit_clauses.append(clause)
                        # backtrack if empty clause 
                        if empty == True:
                            return False

            # add unit clauses to list to use later in unit propagation
            if self.unit_clause(clause) and clause not in unit_clauses:
                unit_clauses.append(clause)
        clauses = new_clauses

        # keep doing unit propagation till no unit_clauses are left
        while len(unit_clauses) != 0: 
            empty = False
            total_new_unit_clauses = []
            
            # unit propagation
            for c in unit_clauses:
                clauses, empty, new_unit_clauses = self.unit_propagation(c, set_variables, clauses)# shorten works, does empty work?s
                # remove literal from remaining
                remaining.remove(c[0].replace("-", ""))

                # backtrack if empty clause
                if empty == True:
                    return False
                # update unit_clauses
                for new_unit_clause in new_unit_clauses:
                    in_new_unit_clauses = False
                    for lit in new_unit_clause:
                        for var in total_new_unit_clauses:
                            opposite = self.opposite(lit)
                            if lit in var or opposite in var:
                                in_new_unit_clauses = True
                        else:
                            continue
                    if in_new_unit_clauses == False:
                        total_new_unit_clauses.append(new_unit_clause)
            unit_clauses = total_new_unit_clauses
        print("out of unit clauses")
            
        

        # Handle pure literals until no pure literals are left
        no_pure_literals = False
        new_clauses = copy.deepcopy(clauses)

        while no_pure_literals != True:
            
            # find pure literals
            for lit, i in zip(remaining, range(0, len(remaining))):
                pure_lit, boolean = self.pure_lit(lit, clauses)
                if boolean:
                    if not pure_lit:
                        pure = "-" + lit
                    else:
                        pure = lit
                    remaining.remove(pure.replace("-", ""))
                    # handle pure lit
                    for clause in clauses:
                        if pure in clause:
                            new_clauses.remove(clause)
                elif boolean == False and i == len(remaining) - 1:
                    no_pure_literals = True
                clauses = new_clauses
                        
                
        # check for empty set of clauses 
        if len(clauses) == 0:
            print(set_variables)
            print(len(set_variables))
            return True
        
        run += 1
        return self.run(copy.deepcopy(variables), copy.deepcopy(clauses), copy.deepcopy(set_variables), True, False, run) or  self.run(copy.deepcopy(variables), copy.deepcopy(clauses), copy.deepcopy(set_variables), True, True, run)
        

            








        
                

            
        

