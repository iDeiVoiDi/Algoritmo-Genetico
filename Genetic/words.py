#==================================================
# WORDS | Creacion de las palabras
#==================================================

import random
import string

from config.config import load_config


# Crea una lista con las palabras 
def list_creator(parents):
    config = load_config()
    poblation = []
    
    if not parents:
        for _ in range(config["WORDS_FOR_GEN"]):
            poblation.append(word_creator())
    else:
        poblation = word_genetic(parents)

    return poblation

# Crea una palabra aleatorizada entre las posibilidades
def word_creator():
    config = load_config()
    possibilities = words_possibilities()
    word = ""

    for _ in range(config["LENGTH_WORD"]):
        palabra = random.choice(possibilities)
        word += palabra

    return word

# Guarda todas las posibles letras
def words_possibilities():
    config = load_config()
    possibilities = ""

    # Solo se pillan las q estan seleccionadas en config
    if config["MINUS"]:
        possibilities += string.ascii_lowercase
    if config["MAYUS"]:
        possibilities += string.ascii_uppercase
    if config["SPACE"]:
        possibilities += " "
    if config["NUM"]:
        possibilities += string.digits
    if config["SIMBOL"]:
        possibilities += string.punctuation

    return possibilities

# Crea los hijos basados en los padres
def word_genetic(parents):
    config = load_config()
    children = []
    # Duplicamos siempre los tres mejores para q no perdamos avances
    children.extend(parents[:3]) 
    parent_slices = get_slices(parents)

    for _ in range(config["WORDS_FOR_GEN"] - 3):
        half1 = random.choice(parent_slices)
        half2 = random.choice(parent_slices)
        word = half1 + half2

        word = mutation(word)

        children.append(word)

    return children

# Trocea los padres para elegir aleatoriamente
def get_slices(parents):
    config = load_config()
    parent_slices = []
    half = config["LENGTH_WORD"] // 2

    for i in parents:
        parent_slices.append(i[:half])
        parent_slices.append(i[half:])

    return parent_slices

def mutation(word):
    config = load_config()
    possibilities = words_possibilities()

    if random.random() <= config["MUTATION_PORCENTAGE"]:
        position = random.randint(0, 19)
        new_letter = random.choice(possibilities)
        
        word_list = list(word)
        word_list[position] = new_letter        
        word = "".join(word_list)

    return word