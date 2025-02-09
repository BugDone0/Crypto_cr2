from mod import find_mod_ring

filename="output.txt"



# Функция для записи таблицы в файл
def write_table(table):
    col_width = [5, 5, 5, 5, 5, 5, 5]  
    with open(filename, "a") as file:
        header = "|" + "|".join(item.center(col_width[i]) for i, item in enumerate(table[0])) + "|"
        file.write(header + "\n")
        file.write("-" * len(header) + "\n") 
        for row in table[1:]:
            row_str = "|" + "|".join(str(item).center(col_width[i]) for i, item in enumerate(row)) + "|"
            file.write(row_str + "\n")

def count_table(Ni, ni, i):
    x1 = 0
    x2 = 1
    table = []
    table.append(["q", "r", "x", "Ni", "ni", "x2", "x1"])  
    table.append(["-", "-", "-", Ni, ni, x2, x1])  

    while ni != 0:
        q = int(Ni // ni)
        r = int(Ni % ni)
        x = x2 - q * x1
        new_Ni = ni
        new_ni = r
        new_x2 = x1
        new_x1 = x

        table.append([q, r, x, new_Ni, new_ni, new_x2, new_x1])

        Ni = new_Ni
        ni = new_ni
        x1 = new_x1
        x2 = new_x2

    write_table(table)

    with open(filename, "a") as file:
        file.write(f"\nu{i} = {table[-1][-2]}\n\n\n")

    return(table[-1][-2])

def solve_task2(a1, a2, a3, n1, n2, n3):
    # заполняется по вариантам
    a1=10
    a2=8
    a3=3
    n1=16
    n2=11
    n3=23

    N = n1 * n2 * n3
    N1= int(N/n1)
    N2= int(N/n2)
    N3= int(N/n3)

    with open(filename, "a") as file:
        file.write(f"Решение 2 задачи\n\n")
        file.write(f"a1 = {a1}, a2 = {a2}, a3 = {a3}\n")
        file.write(f"n1 = {n1}, n2 = {n2}, n3 = {n3}\n\n")

        file.write(f"N = n1 * n2 * n3 = {n1} * {n2} * {n3} = {N}\n\n")
        file.write(f"N1 = N / n1 = {N} / {n1} = {N1}\n")
        file.write(f"N2 = N / n2 = {N} / {n2} = {N2}\n")
        file.write(f"N3 = N / n3 = {N} / {n3} = {N3}\n\n")
        
    u1 = count_table(N1, n1, 1)
    u2 = count_table(N2, n2, 2)
    u3 = count_table(N3, n3, 3)
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