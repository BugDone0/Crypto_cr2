filename="output.txt"
separator = "---------"

def sep(i):
    if i == 0:
        with open(filename, "w") as file: 
            file.write(f"\nРешение 2 контрольной работы \n\n")
    else:
        with open(filename, "a") as file:
            file.write(f"\n\n{separator *2}\nРешение {i} задачи | \n{separator *2}\n\n")