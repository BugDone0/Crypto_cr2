filename="output.txt"
separator = "---------"

def sep(i, variant_number = 12 ):
    if i == 0:
        with open(filename, "w") as file: 
            file.write(f"\nРешение 2 контрольной работы \nВариант №{variant_number}\n")
    else:
        with open(filename, "a") as file:
            file.write(f"\n\n{separator *2}\nРешение {i} задачи | \n{separator *2}\n\n")