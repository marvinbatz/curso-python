import random

def selection_random():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        data = []
        for name in f:
            data.append(name.upper())
        
        print(random.choice(data.replace ))


def ahorcado(letter):
    assert 2 > len(letter) > 0 and letter.isalpha(), "Ingresesa solamente una letra"


def run():
    menu = """
        Bienvenido al juego del Ahorcado

        Adivina la palabra secreta

        ________________________________

    """
    print(menu)
    selection_random()
    letter = input("Ingresa una letra: ")
    ahorcado(letter)


if __name__ == '__main__':
    run()