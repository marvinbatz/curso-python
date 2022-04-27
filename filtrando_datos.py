from dataclasses import dataclass


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #obteniendo desarrolladores de python de Platzi con list comprehensions
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    #obteniendo desarrolladores de python de Platzi con Hugh order functions
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    #obteniendo trabajadores de Platzi con list comprehensions
    # all_platzi_workers = [worker["name"]  for worker in DATA if worker["organization"] == "Platzi"]

    #obteniendo trabajadores de Platzi con Hugh Order Functions
    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))

    #obteniendo con lambda los trabajadores adultos
    # adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    #para no obtener los datos completos, mas bien solo el nombre, creamos otro lambda map para convertir los datos de adults a solo nombres.
    # adults = list(map(lambda worker: worker["name"], adults))

    #obteniendo adultos con List Comprehensions
    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]

    #el signo | es una suma o concatenación en las funciones. Básicamente estamos agregando un nuevo valor para cada uno de los datos.
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    #agregando nuevo valor "old" para cada uno de los datos con list comprehensions
    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]
    
    # print('Desarrolladores de Python: ' + str(all_python_devs))
    # print('Trabajadores de Platzi: ' + str(all_platzi_workers))
    # print('Trabajadores Adultos: ' + str(adults))
    print('Tercera Edad: ' + str(old_people))


if __name__ == '__main__':
    run()