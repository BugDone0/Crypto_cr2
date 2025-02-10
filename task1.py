from mod import find_mod_ring
from counttable import count_table
from sep import sep
filename="output.txt"

def solve_task1(a ,p ):

    sep(1)
    a_1 = count_table(a, p, avel="a", bvel="p", mode="qry")  
    with open(filename, "a") as file:   
            file.write(f"\n{int(a)}^(-1) mod {int(p)} = {a_1} mod {int(p)}\n\n")
 