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
    
    def unit_propagation(self, unit_clause, variables, set_variables, clauses):
        """
        Sets unit clause to appropriate boolean and rm from unset variables
        """
        if "-" in unit_clause[0]: 
            set_variables[unit_clause[0]]= False
        else: 
            set_variables[unit_clause[0]]= True
        variables.remove(unit_clause[0])

        for clause in clauses:
            if unit_clause[0] in clause:
                clauses.remove(clause)
        return

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
        if "-" in literal:
            clause.remove(literal.replace("-", ""))
        else:
            clause.remove("-"+ literal)
        return clause
    
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
            set_variables[literal] = False
            return True


    def run(self, variables, clauses, set_variables, split, value):
        """
        Runs DPLL algorithm by systematically checking all values for literals, with backtracking.
        Input: variables(list), clauses(list), set_variables(dict), split(Bool), value(Bool)
        Output: CNF file with set variables.
        """
        count_lits = {}
        clauses = clauses
        set_variables = set_variables
        variables = variables

        # set variable to true or false if not first run
        if split is not False: 
            variable = variables.pop()
            if value == False:
                variable = "-" + variable
                set_variables[variable] = False
            else:
                set_variables[variable] = True
        else:
            variable = None
            # set_variables[variable] = True

        print("variable = ", variable)
        print("split, value = ", split, value)

        # unit propagation while unit literal present in KB
        for clause, i in zip(clauses, range(0, len(clauses))):
            
            if variable != None:
                # make new set of clauses with lit value
                if variable.replace("-", "") in clause and "-" not in variable:
                    clauses.remove(clause)
                elif variable + "-" in clause and "-" in variable:
                    clauses.remove(clause)
                elif variable + "-" in clause and "-" not in variable:
                    new_clause = self.shorten_clause(variable, clause)
                    clauses[i] = new_clause
                elif variable.replace("-", "") in clause and "-" in variable:
                    new_clause = self.shorten_clause(variable, clause) 
                    clauses[i] = new_clause

            for literal in clause:
                # handle tautology if needed
                if self.tautology(clause, literal):
                    clauses.remove(clause)
                else: 
                    # literal counter
                    self.count_lits(literal, count_lits)
                    
            # unit propagation 
            if self.unit_clause(clause):
                self.unit_propagation(clause, variables, set_variables, clauses)

        # print(count_lits)
        # for clause in clauses:    
        #     for literal in clause:
        #         if self.pure_lits(literal, count_lits) != None: 
        #             print("pure lit:", literal)
        #             self.pure_lit_assign(literal, self.pure_lits(literal, count_lits), set_variables, variables)

        # empty set of clauses 
        if self.empty_set_clauses(clauses):
            print(len(set_variables))
            print(clauses)
            print(set_variables)
            return True
        
        # empty clause
        for clause in clauses:
            if self.empty_clause(clause):
                print("EMPTY CLAUSE!!!!!!!")

                return False
        return self.run(copy.deepcopy(variables), copy.deepcopy(clauses), copy.deepcopy(set_variables), True, False) or  self.run(copy.deepcopy(variables), copy.deepcopy(clauses), copy.deepcopy(set_variables), True, True)
        

            








        
                

            
        




    
                   
    # def run(self):
    #     """
    #     Runs DPLL algorithm by systematically checking all values for literals, with backtracking.
    #     """
    #     # first check for empty set of clauses
    #     if self.empty_set_clauses():
    #         return True

    #     # loop through all clauses 
    #     for clause in self.SAT.clauses:
            
    #         # check for empty clause 
    #         if self.empty_clause(clause):
    #             return False 

    #         # check unit clause and set it and count lit if True 
    #         if self.set_unit_clause(clause, self.unit_clause(clause)):
    #             self.SAT.count_lits(literal)
    #             continue
            
    #         for literal in clause:
    #             # check for tautology and count literal if clause is not removed
    #             if self.tautology(clause, literal):
    #                 self.SAT.clauses.remove(clause)
    #             else: 
    #                 self.SAT.count_lits(literal)
        
    #     # check for pure clause
    #     for clause in self.SAT.clauses:
    #         for literal in clause:
                
    #             if self.pure_lits(literal):
    #                 self.SAT.set_variables[literal] = True
    #                 self.SAT.clauses.remove(clause)
    #             elif self.pure_lits(literal) == False:
    #                 self.SAT.set_variables[literal] = False
    #                 self.SAT.clauses.remove(clause)
    #             else: 
    #                 continue
        
    #     # chronological backtracking

    #     # deep copy

    #     # assign value

    #     # change clauses 

    #     # remove sat clauses

    #     # check for unit clause -> hard choice 

    #     # 






                


        
    

            
            

        

        


