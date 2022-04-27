def run():
# los primeros 100 numeros naturales elevados al cuadrado
    # square = []
    # for i in range(1,101,):
    #     square.append(i**2)


# El cuadrado de los numeros que no sean divisibles entre 3
    # square = []
    # for i in range(1,101,):
    #     if i % 3 != 0:
    #         square.append(i**2)


# El cuadrado de los numeros que no sean divisibles entre 3, es como el de arriba, pero con una estructura nueva... Con list Comprehensions
    # square = [i**2 for i in range(1,101) if i %3 != 0]

# Crear un list comprehension de los multiplos de 4 que ala ver tambi[en son multiplos de 6 y de 9 hasta 5 dígitos]
    number = [i for i in range(1,100000) if i %4 == 0 and i %6 == 0 and i %9 == 0]

    print(number)

if __name__ == ('__main__'):
    run()