from mod import find_mod_ring
from counttable import count_table
from sep import sep
filename="output.txt"

def solve_task3(a ,b ,m):

    sep(3)
    
    with open(filename, "a") as file:    
        file.write(f"ax = b(mod m)\n")
        file.write(f"a = {a}, b = {b}, m = {m}\n\n")
    d = count_table(a, m, mode ="rma")
    with open(filename, "a") as file:    
        file.write(f"\nNOD(a,m) = NOD({a}, {m}) = {d} = d\n\n")
            

    if d == 1:
        raise ValueError("Вариант решения не рассмотрен на лекции")
    elif d > 1 and b % d != 0:
        raise ValueError("Вариант решения не рассмотрен на лекции")
    else:
        a_ = a/d
        b_ = b/d
        m_ = m/d
        a_1 = count_table(a_, m_, mode="qry")  
        with open(filename, "a") as file:   
            file.write(f"\n{int(a/d)}x ≡ {int(b/d)} mod {int(m/d)}\n")
            file.write(f"¯a = {int(a/d)}, ¯b = {int(b/d)}, ¯m = {int(m/d)}\n")
            file.write(f"{int(a/d)}^-1 mod {int(m/d)} = {a_1}\n\n")


        with open(filename, "a") as file:  
            file.write(f"x = ({int(a_1)} * {int(b_)}) mod {m} = {int(find_mod_ring(a_1 * b_, m_))}\n\n")

        x = find_mod_ring(a_1 * b_, m_)
        results = []
        with open(filename, "a") as file:   
            for k in range(d) :
                result = int(find_mod_ring(x + m_ * k, m))
                results.append(result)
                file.write(f"x{k} = ({int(x)} + {int(m_)} * {k}) mod {m} = {result}\n")
                
        with open(filename, "a") as file:  
            file.write(f"\n\nПроверка:\n")

        with open(filename, "a") as file:   
            for result in results:
                if find_mod_ring(a * result, m) == b:
                    file.write(f"({a} * {result}) mod {m} = {b}\n")  
                else:
                    raise ValueError("Что-то пошло не так: решение 2 задачи оказалось не верным, а помойным")
