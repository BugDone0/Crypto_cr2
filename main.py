from database import get_variant
from sep import sep
#from task1 import solve_task1
from task2 import solve_task2
from task3 import solve_task3
#from task4 import solve_task4
filename="output.txt"


def main():

    sep(0)
    
    # Выбираем вариант
    variant_number = 11
    variables = get_variant(variant_number)

    #solve_task1()
    solve_task2(variables["a1"], variables["a2"], variables["a3"], variables["n1"], variables["n2"], variables["n3"])
    solve_task3(variables["ad"] ,variables["b"] ,variables["m"])
    #solve_task4()
   

if __name__ == "__main__":
    main()
