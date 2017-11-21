def print_tree(rows, filepath):
    tree = ["W", "***"]
    sign = "* "
    num_line = 0 # для хранения номера печатаемой строки
    spaces = rows * 3 - 3 # для хранения числа пробелов перед строкой
    low_string = " " * (spaces - 1) + "TTTT"
    try:
        f = open(filepath, "w")
        while num_line < rows:
            if num_line >1:
                str = "@" + sign*(num_line*4-3)
                if num_line % 2 == 1:
                    str = str[::-1]
                spaces -= 3
                tree.append(str)
            else:
                spaces = spaces - num_line
            f.write(" "*spaces + tree[num_line] + "\n")
            num_line +=1
        f.write(low_string + "\n" + low_string)
    except FileNotFoundError as e:
        print(e)
    finally:
        f.close()

print_tree(int(input("Введите число рядов: ")), input("Введите путь к файлу: "))


