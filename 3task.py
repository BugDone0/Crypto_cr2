filename="output3.txt"

from mod import find_mod_ring
a = 300
b = 162
m = 1000

def write_table(table):
    col_width = [5, 5, 5]  
    with open(filename, "a") as file:
        header = "|" + "|".join(item.center(col_width[i]) for i, item in enumerate(table[0])) + "|"
        file.write(header + "\n")
        file.write("-" * len(header) + "\n") 
        for row in table[1:]:
            row_str = "|" + "|".join(str(item).center(col_width[i]) for i, item in enumerate(row)) + "|"
            file.write(row_str + "\n")

def count_table(a, m):
    table = []
    table.append(["r", "m", "a"])  
    table.append(["-", m, a])  
    if m>a:
        a = m
    while a != 0:
        r = int(m % a)
        new_m = a
        new_a = r

        table.append([r, new_m, new_a])
        m = new_m
        a = new_a

    
    write_table(table)

    with open(filename, "a") as file:
        file.write(f"\nd = {table[-1][-2]}\n\n\n")

    return(table[-1][-2])


def solve_task3():
    with open(filename, "a") as file:    
        file.write(f"ax = b(mod m)\n")
        file.write(f"a = {a}, b = {b}, m = {m}\n\n")
        d = count_table(a, m)
        file.write(f"NOD(a,m) = NOD({a}, {m}) = {d}\n\n")

solve_task3()