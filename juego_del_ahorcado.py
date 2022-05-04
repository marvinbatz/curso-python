import random

def selection_random():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        data = []
        for name in f:
            data.append(name)
        
        print(data)
        WORD = random.choice(data)
        print(WORD)
        letter = str(input("Ingresa una letra: "))
        print(letter)
        if WORD == letter:
            print("Bien hecho!")
        else:
            print("No es la palabra")


# def ahorcado(letter):
#     assert 2 > len(letter) > 0 and letter.isalpha(), "Ingresesa solamente una letra"


def run():
    menu = """
        Bienvenido al juego del Ahorcado

        Adivina la palabra secreta

        ________________________________

    """
    print(menu)
    selection_random()
    # letter = input("Ingresa una letra: ")
    # ahorcado(letter)


if __name__ == '__main__':
    run()