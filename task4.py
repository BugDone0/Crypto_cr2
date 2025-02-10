from mod import find_mod_ring
from counttable import count_table
from sep import sep
filename="output.txt"

def solve_task4(a ,p ):

    sep(4)

    with open(filename, "a") as file:    
        file.write(f"a = {a}, b = {p}\n")

    with open(filename, "a") as file:    
        file.write(f"\nШАГ 4\n")

    a_1 = count_table(a, p, avel="a", bvel="p", mode="qry")
    
    with open(filename, "a") as file:    
        file.write(f"\n {a}^(-1) mod {p} = {a_1}\n")