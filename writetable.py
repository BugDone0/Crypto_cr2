
def write_table(table):
    col_width = [5] * len(table[0])
    filename="output.txt"
    with open(filename, "a") as file:
        header = "|" + "|".join(item.center(col_width[i]) for i, item in enumerate(table[0])) + "|"
        file.write(header + "\n")
        file.write("-" * len(header) + "\n") 
        for row in table[1:]:
            row_str = "|" + "|".join(str(item).center(col_width[i]) for i, item in enumerate(row)) + "|"
            file.write(row_str + "\n")