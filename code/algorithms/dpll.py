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

    def count_lits(self, literal, count_literals):
        if literal not in count_literals.keys():
            count_literals[literal] = 0
        count_literals[literal] += 1

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
        unit_clause = unit_clause[0]
        
        if "-" in unit_clause:
            opposite = unit_clause.replace("-", "")
        else:
            opposite = "-" + unit_clause

        empty = False
        new_unit_clauses = []
        for clause, i in zip(clauses, range(0, len(clauses))):
            for variable in clause:
                if opposite == variable:
                    # shorten clause
                    new_clause, empty, new_unit_clause = self.shorten_clause(unit_clause, clause)
                    clauses[i] = new_clause
                    new_unit_clauses.append(new_unit_clause)

                elif unit_clause == variable:
                    clauses.remove(clause)
        return clauses, empty, new_unit_clauses

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

    def pure_lits(self, literal, count_literals):
        if literal.replace("-", "") not in count_literals.keys() and "-" in literal:
            return False
        elif "-" + literal not in count_literals.keys() and "-"  not in literal:
            return True
        else:
            return None
    
    def pure_lit_assign(self, literal, boolean, set_variables, variables):
        """
        Assigns boolean to pure literal and removes from variables list.
        """
        set_variables[literal] = boolean
        variables.remove(literal.replace("-", ""))

        return 
    
    def pure_lit_in_clause(self, literal, clause):
        if literal in clause:
            True
        else: 
            False  
    
    def shorten_clause(self, literal, clause):
        
        # check if empty clause, return False
        if "-" in literal:
            clause.remove(literal.replace("-", ""))
        else:
            clause.remove("-"+ literal)

        if len(clause) == 0:
            empty = True
        elif len(clause) == 1:
            unit_clause = clause
            empty = False
        else: 
            empty = False

        return clause, empty, unit_clause
    
    def assign_literal(self, literal, set_variables):
        """
        Assigns value to literal. If false: tries True. 
        If True, returns false. Else (None in our case) sets variable to False.
        """
        if set_variables[literal] == False:
            set_variables[literal] = True
            return True
        elif set_variables[literal] == True:
            return False
        else:
            return True
    

    def run(self, variables, clauses, set_variables, split, value, run):
        """
        Runs DPLL algorithm by systematically checking all values for literals, with backtracking.
        Input: variables(list), clauses(list), set_variables(dict), split(Bool), value(Bool)
        Output: CNF file with set variables.
        """
        count_lits = {}
        clauses = clauses
        set_variables = set_variables
        variables = variables
        empty = False

        # set variable to true or false if not first run
        if split is not False: 
            variable = variables.pop()
            if value == False:
                variable = "-" + variable
            else:
                set_variables[variable] = True
        else:
            variable = None
            # set_variables[variable] = True

        print("variable = ", variable)
        print("split, value = ", split, value)
        if run % 2 == 0:
            print("WE DID: ", run, "RUNS")

        # unit propagation while unit literal present in KB
        for clause, i in zip(clauses, range(0, len(clauses))):
            
            # if variable is chosen
            if variable != None:
                # make new set of clauses with lit value
                if variable.replace("-", "") in clause and "-" not in variable:
                    clauses.remove(clause)
                    continue
                elif variable + "-" in clause and "-" in variable:
                    clauses.remove(clause)
                    continue
                elif variable + "-" in clause and "-" not in variable:
                    # shorten clause
                    new_clause, empty = self.shorten_clause(variable, clause)
                    clauses[i] = new_clause
                elif variable.replace("-", "") in clause and "-" in variable:
                    # shorten clause
                    new_clause, empty, unit_clause = self.shorten_clause(variable, clause)
                    clauses[i] = new_clause
                
                # unit propagation
                if self.unit_clause(clause):
                    unit_clauses = [clause]
                    print(unit_clauses)
                    
                    # keep doing unit propagation till no unit_clauses are left
                    while len(unit_clauses) != 0:
                        total_new_unit_clauses = []
                        for unit_clause in unit_clauses:
                            clauses, empty, new_unit_clauses = self.unit_propagation(clause, set_variables, clauses)
                            for new_unit_clause in new_unit_clauses:
                                total_new_unit_clauses.append(new_unit_clause)
                        unit_clauses = total_new_unit_clauses

            # check for empty clause
            if empty == True: 
                return False
                
            # check for empty set of clauses 
            if len(clauses) == 0:
                print(set_variables)
                return True
        
                    
           
        # if variable == "-899":
        #     return False

        # print(count_lits)
        # for clause in clauses:    
        #     for literal in clause:
        #         if self.pure_lits(literal, count_lits) != None: 
        #             print("pure lit:", literal)
        #             self.pure_lit_assign(literal, self.pure_lits(literal, count_lits), set_variables, variables)

        run += 1
        return self.run(copy.deepcopy(variables), copy.deepcopy(clauses), copy.deepcopy(set_variables), True, False, run) or  self.run(copy.deepcopy(variables), copy.deepcopy(clauses), copy.deepcopy(set_variables), True, True, run)
        

            








        
                

            
        

