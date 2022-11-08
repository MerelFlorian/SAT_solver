# Sudoku class


# read input (DIMACS file)

class Sudoku:
    def __init__(self, file):
        
        # attributes
        self.file = file
        self.variables = {}
        self.clauses = {}
        self.number_variables = 0
        self.number_clauses = 0
        self.size =  0
    
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

        # make clauses dict 
        for clause in lines[1:]:
            self.clauses[clause.strip("0\n")] = False
        print(self.clauses)

        # make variables dict
        for row in range (1, self.size, 1):
            for column in range (1, self.size, 1):
                for value in range(1, self.size, 1):
                    self.variables[row,column,value] = False


        print(self.variables)
        # fill rest of attributes 
        self.number_clauses = len(self.clauses)

if __name__ == "__main__":
    sudoku = Sudoku("/home/m_rosa/SAT/SAT_solver/resources/sudoku1.cnf")
    sudoku.input()
