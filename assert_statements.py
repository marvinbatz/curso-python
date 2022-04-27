def divisors(num):
        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
                divisors.append(i)
        return divisors


def run():
    num = input("Ingresa un número: ")
    #el metodo isnumeric que devuelve True si este string corresponde a un numero -- este assert asegura que el número ingresado es númerico y que no es negativo
    assert num.isnumeric() and int(num) > 0, "!! Debes de ingresar un número positivo"
    print(divisors(int(num)))
    print("Terminó el programa")


if __name__ == '__main__':
    run()