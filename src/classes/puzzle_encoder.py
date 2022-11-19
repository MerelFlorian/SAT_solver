# Create DIMACS file from sudoku puzzle file.

import math

file = "/Users/ruby/Documents/GitHub/SAT_solver/resources/test_sets/4x4.txt"
with open(file, "r") as f:
    a = len(f.readline())-1

    for line in f.readlines():
        print("new")
        r = 1
        c = 1
        for i in line:

            # Emergency break
            if (r * c == a):
                break

        # Keep track of placement
            if i == ".":
                if c == 4:
                    c = 1
                    r += 1
                else: c += 1

        # Create
            else:
                with open("newpuzzle.txt", "a") as n:
                    n.write(''.join(str(e) for e in [r, c, i, " ", 0])+"\n")
                    print(r, c, i)
                    if c == 4:
                        c = 1
                        r += 1
                    else:
                        c +=1
