from functools import reduce

def run():
    ##LAMBDA FILTER
     
    # my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    #obtener los impares de la lista con list comprrehensions
    # odd = [i for i in my_list if i %2 != 0]

    #obtener los impares de la lista con lambda
    # odd = list(filter(lambda x: x % 2 != 0, my_list))

    # print(odd)

    ##LAMBDA MAP
    # my_list = [1, 2, 3, 4, 5]
    #obtener el cuadrado de los valores de la lista con list comprehensions
    # squares = [i**2 for i in my_list]

    #obteniendo el cuadrado de los valores de la lista con lambda
    # squares = list(map(lambda x: x**2, my_list))
    
    # print(squares)

    ##LAMBDA REDUCE
    my_list = [2, 2, 2, 2, 2]

    #obteniendo la multiplicación de todos los valores de la lista entre sí con un for
    # all_prod = 1
    # for i in my_list:
    #     all_prod = all_prod * i

    #obteniendo la multiplicación de todos los valores de la lista entre sí con lambda REDUCE, ojo que se debe de importar una libreria
    all_prod = reduce(lambda x, y: x * y, my_list)
    
    print(all_prod)

if __name__ == '__main__':
    run()