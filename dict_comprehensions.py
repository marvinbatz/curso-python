import math


def run():
# Disccionario cuyas llaves sean los 100 primeros numeros naturales, y sus valores sean esos numeros elevados al cubo.
    # dict = {}

    # for key in range(1,101):
    #     if key % 3 != 0:
    #         dict[key] = key**3

# Disccionario cuyas llaves sean los 100 primeros numeros naturales, y sus valores sean esos numeros elevados al cubo. Con dict Comprenhensions
    # dict = {key: key**3 for key in range(1,101) if key % 3 != 0}

# Diccionarios cuyas llaves sean los 1000 primeros números naturales con sus raíces cuadradas como valores
    dict = {key: round(math.sqrt(key),2) for key in range(1,1001)}
    
    print(dict)

if __name__ == '__main__':
    run()