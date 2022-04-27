def divisors(num):
        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
                divisors.append(i)
        return divisors


def run():
    #Con "try" intenta ejecutar las lineas de código
    try:
        num = int(input("Ingresa un número: "))
        if num < 0:
            raise Exception("Solo se permiten positivos")
        print(divisors(num))
        print("Terminó el programa")
    #En caso se encuentre con un error, ejecutará el siguiente mensaje
    except ValueError:
        print("Debes de ingresar un número")
    except Exception as ve:
        print(ve)


if __name__ == '__main__':
    run()