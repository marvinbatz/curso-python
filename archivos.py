def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Marvin", "Lucky", "Byron", "Alejandra", "Josué"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            #Lo que haremos en los siguientes cósigos es escribir un nombre de nuestra lista y luego un saldo de línea, así sucesivamente.
            f.write(name)
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()