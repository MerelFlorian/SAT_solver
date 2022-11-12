# SAT class

# read input (DIMACS file)

class SAT:
    def __init__(self, file):
        
        # attributes
        self.file = file
        self.variables = []
        self.clauses = []
        self.count_literals = {}
        self.size =  0
        self.set_variables = {}
    
    def input(self):
        """
        Reads input and makes clauses dict and variables dict. 
        Sets booleans of clauses and variables to False on default.
        """
        # open file and read lines
        with open(self.file) as f:
            lines = [line for line in f]
            info = lines[0].split(" ") 
            self.size = int([*info[2]][0])
            self.number_variables = self.size**2

        # make variables dict
        for row in range (1, self.size, 1):
            for column in range (1, self.size, 1):
                for value in range(1, self.size, 1):
                    # make (to be) set variables dict
                    self.variables[str(row)+str(column)+str(value)] = None
                    # make list of unset variables 
                    self.variables.append(str(row)+str(column)+str(value))
                    
        
        # make clauses list
        self.clauses = [clause.strip(" 0\n").split(" ") for clause in lines[1:]]

        # fill rest of attributes 
        self.number_clauses = len(self.clauses)

    

    def remove_lit_clause(self, literal, clause):
        # remove literal from 


