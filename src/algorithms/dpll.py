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

    def pure_lit(self, variable, clauses):
        """
        Counts number of times a variable is present in all clauses (either with negation sign or without).
        Returns True if pure literal.
        Returns False if not pure literal.
        """
        
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
                    return False
        if neg > 0 or pos > 0:
            return True

        
    
    def opposite(self, literal):
        """
        Returns opposite of literal (111-> -111)
        """
        if "-" in literal:
            opposite = literal.replace("-", "")
        else:
            opposite = "-" + literal
        return opposite


    def unit_clause(self, clause):
        """
        Returns true if clause is unit clause
        """
        if len(clause) == 1: 
            return True
        else: 
            return False
    
    def unit_propagation(self, unit_clause, set_variables, clauses):
        """
        Sets unit clause to appropriate boolean and rm from unset variables
        """
        # sets variable to True or False
        if "-" not in unit_clause[0]: 
            set_variables[unit_clause[0]] = True

        # remove  or shorten clause from clauses
        opposite = self.opposite(unit_clause[0])

        empty = False
        new_unit_clauses = [] # lijst kan 2x dezelfde waarde hebben
        new_clauses = copy.deepcopy(clauses)
        removed_clauses = 0
        
        for clause, i in zip(clauses, range(0, len(clauses))):
            
            for variable in clause:
                if opposite == variable:  # somehow it does not do all clauses (does not find all matches)
                    # shorten clause
                    new_clause, empty, new = self.shorten_clause(unit_clause[0], clause) # shortening works, does empty work?
                    new_clauses[i - removed_clauses] = new_clause

                    if new == True:
                        if new_clause not in new_unit_clauses: 
                            new_unit_clauses.append(new_clause)
                    
                elif unit_clause[0] == variable:
                    removed_clauses += 1
                    new_clauses.remove(clause)

        return new_clauses, empty, new_unit_clauses

    def empty_set_clauses(self, clauses):
        """ 
        Checks for empty (sets of) clauses, returns true if so.
        """
        if len(clauses) == 0: # check if correct
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
        Returns True if clause contains tautology
        """
        if "-" in literal and literal.replace("-", "") in clause:
            return True
        else:
            return False
    
    def pure_lit_assign(self, literal, boolean, set_variables, variables):
        """
        Assigns boolean to pure literal and removes from variables list.
        """
        set_variables[literal] = boolean
        variables.remove(literal.replace("-", ""))

        return 
    
    def shorten_clause(self, literal, clause):
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
    
    

    def run(self, variables, clauses, set_variables, split, value, run):
        """
        Runs DPLL algorithm by systematically checking all values for literals, with backtracking.
        Input: variables(list), clauses(list), set_variables(dict), split(Bool), value(Bool)
        Output: CNF file with set variables.
        """
        count_lits = {}
        empty = False
        unit_clauses = []
        new_clauses = copy.deepcopy(clauses)

        # set variable to true or false if not first run
        if split is not False: 
            variable = variables.pop()
            if value == False:
                variable = "-" + variable
            else:
                set_variables[variable] = True
        else:
            variable = None

        # print("variable = ", variable)
        # print("split, value = ", split, value)

        # unit propagation while unit literal present in KB
        for clause, i in zip(clauses, range(0, len(clauses))):
            for literal in clause:
            
                # if variable is chosen
                if variable != None:

                    # make new set of clauses with lit value\

                    # remove clause 
                    if variable == literal:
                        clauses.remove(clause)
                        continue
                    elif variable == self.opposite(literal):
                        # shorten clause
                        new_clause, empty, unit_clause = self.shorten_clause(variable, clause)
                        clauses[i] = new_clause
                        if unit_clause == True and clause not in unit_clauses:
                            unit_clauses.append(clause)
                    if empty == True:
                        return False
                
            # add unit clauses to list to use later in unit propagation
            if self.unit_clause(clause) and clause not in unit_clauses:
                unit_clauses.append(clause)

        # keep doing unit propagation till no unit_clauses are left
        while len(unit_clauses) != 0: 
            empty = False
            total_new_unit_clauses = []
    
            for c in unit_clauses:
                clauses, empty, new_unit_clauses = self.unit_propagation(c, set_variables, clauses)# shorten works, does empty work?s
                if empty == True:
                    return False
            
                for new_unit_clause in new_unit_clauses:
                    total_new_unit_clauses.append(new_unit_clause)
            unit_clauses = total_new_unit_clauses
        
        # Handle pure literals untill no pure literals are left
        pure_literals = []
        while len(pure_literals) != 0:
            print(pure_literals)
            
            # find pure literals
            new_pure_literals = []

            for variable in variables:
                if self.pure_lit(variable):
                    new_pure_literals.append(variable)
                else:
                    continue
            
            # reset pure literals
            pure_literals = new_pure_literals

            # handle pure literals
            for pure in pure_literals:
                for clause in clauses:
                    for literal in clause:
                        if pure in literal and "-" in literal:
                            clauses.remove(clause)
                        elif pure in literal and "-" not in literal:
                            set_variables[literal] = True
                            clauses.remove(clause)
                if len(clauses) == 0:
                    return True
                variables.pop(pure)
                
        # check for empty set of clauses 
        if len(clauses) == 0:
            print(set_variables)
            return True
        
        
        
                    
        
        run += 1
        return self.run(copy.deepcopy(variables), copy.deepcopy(clauses), copy.deepcopy(set_variables), True, False, run) or  self.run(copy.deepcopy(variables), copy.deepcopy(clauses), copy.deepcopy(set_variables), True, True, run)
        

            








        
                

            
        

