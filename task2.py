from mod import find_mod_ring
from counttable import count_table
from sep import sep
filename="output.txt"


def solve_task2(a1, a2, a3, n1, n2, n3):

    sep(2)
    
    N = n1 * n2 * n3
    N1= int(N/n1)
    N2= int(N/n2)
    N3= int(N/n3)

    with open(filename, "a") as file:
        file.write(f"a1 = {a1}, a2 = {a2}, a3 = {a3}\n")
        file.write(f"n1 = {n1}, n2 = {n2}, n3 = {n3}\n\n")

        file.write(f"N = n1 * n2 * n3 = {n1} * {n2} * {n3} = {N}\n\n")
        file.write(f"N1 = N / n1 = {N} / {n1} = {N1}\n")
        file.write(f"N2 = N / n2 = {N} / {n2} = {N2}\n")
        file.write(f"N3 = N / n3 = {N} / {n3} = {N3}\n\n")
        
    u1 = count_table(N1, n1, 1, mode="qrx")
    u2 = count_table(N2, n2, 2, mode="qrx")
    u3 = count_table(N3, n3, 3, mode="qrx")
    x = find_mod_ring(a1 * u1 * N1 + a2 * u2 * N2 + a3 * u3 * N3, N)

    if(find_mod_ring(x,n1) == a1 and find_mod_ring(x,n2) == a2 and find_mod_ring(x,n3) ==a3):
        with open(filename, "a") as file:
            file.write(f"x = ({a1} * {u1} * {N1} + {a2} * {u2} * {N2} + {a3} * {u3} * {N3}) mod {N} = {x} mod {N}\n\n")
            file.write(f"Проверка:\n")
            file.write(f"{x} mod {n1} = {a1}\n")
            file.write(f"{x} mod {n2} = {a2}\n")
            file.write(f"{x} mod {n3} = {a3}\n")
    else:
        with open(filename, "a") as file:
            file.write("Программа не решила задачу №2, решение не прошло проверку")