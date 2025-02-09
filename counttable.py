from writetable import write_table
filename="output.txt"
def count_table(*args, mode):
#2 задача 1-3 табл
    if mode == "qrx":
        Ni, ni, i = args
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
         
        if a > m:
            a, m = m, a 
            table.append(["r", "a", "m"]) 
        else:
            table.append(["r", "m", "a"]) 

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
    
    #3 задача 2 табл
    elif mode == "qry":
        a, m = args
        y1 = 1
        y2 = 0
        table = []
        if a > m:
            a, m = m, a 
            table.append(["q", "r", "y", "¯a", "¯m", "y2", "y1"]) 
        else:
            table.append(["q", "r", "y", "¯m", "¯a", "y2", "y1"])  

        table.append(["-", "-", "-", int(m), int(a), y2, y1])  

        while a != 0:
            q = int(m // a)
            r = int(m % a)
            y = y2 - q * y1
            new_m = int(a)
            new_a = r
            new_y2 = y1
            new_y1 = y

            table.append([q, r, y, new_m, new_a, new_y2, new_y1])

            m = new_m
            a = new_a
            y1 = new_y1
            y2 = new_y2

        write_table(table)

        return(table[-1][-2])
    
    else:
        raise ValueError("Недопустимый режим. Доступные режимы: 'qrx', 'rma' и тп")
    
