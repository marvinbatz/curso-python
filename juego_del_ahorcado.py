import random, os

def selection_random():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        data = []
        for name in f:
            data.append(name)
        
        word = random.choice(data)
        word = word.replace("\n", "")
        word = word.upper()

        escondido = ""
        for i in word:
            escondido = escondido + "_"
        print (escondido)

        letter = ""
        a = ""

        while (escondido != word):
            letter = str(input("Ingresa una letra: "))
            # A continuación aseguramos que solo se ingresará una letra. y con isalpha que no es ningún otro tipo de caracter.
            assert 2 > len(letter) > 0 and letter.isalpha(), "Ingresesa solamente una letra"
            letter = letter.upper()

            count = 0
            for a in word:
                if letter == a:
                    escondido = escondido[:count] + letter + escondido[count+1:]
                count +=1
                os.system ("clear")
            

            print(escondido)

        if word == escondido:
            print("Bien hecho!")
        else:
            print("No es la palabra")


# def ahorcado(letter):
#     assert 2 > len(letter) > 0 and letter.isalpha(), "Ingresesa solamente una letra"


def run():
    menu = """
        Bienvenido al juego del Ahorcado

        Adivina la palabra secreta:

    """
    print(menu)
    selection_random()
    # letter = input("Ingresa una letra: ")
    # ahorcado(letter)


if __name__ == '__main__':
    run()