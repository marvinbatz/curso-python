import random

def selection_random():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        data = []
        for name in f:
            data.append(name)
        
        word = random.choice(data)
        print(word)

        escondido = ""
        for i in word:
            escondido = escondido + "_"
        print (escondido)

        letter = str(input("Ingresa una letra: "))
        print(letter)
        if word == letter:
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