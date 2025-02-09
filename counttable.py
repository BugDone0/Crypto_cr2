from writetable import write_table

def count_table(*args, mode="qrx"):
#2 задача 1-3 табл
    if mode == "qrx":
        Ni, ni, i = args
        filename="output.txt"
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

    #3 задача 1 табл
    elif mode == "rma":
        a, m = args
        table = []
        table.append(["r", "a", "b"])  
        if a < m:
            a, m = m, a 

        table.append(["-", m, a])  
        while a != 0:
            r = int(m % a)
            new_m = a
            new_a = r

            table.append([r, new_m, new_a])
            m = new_m
            a = new_a
        
        
        write_table(table)

        return(table[-1][-2])
    
    else:
        raise ValueError("Недопустимый режим. Доступные режимы: 'qrx', 'rma' и тп")
    
    #3 задача 2 табл