#==================================================
# WORDS | Creacion de las palabras
#==================================================

import random
import string

from config.config import load_config

# Crea una lista con las palabras 
def list_creator(poblation, parents):
    config = load_config()

    poblation = []

    for i in range(config["WORDS_FOR_GEN"]):
        if not parents:
            word_creator()
        else:
            word_genetic(parents)

    return poblation

# Crea una palabra aleatorizada entre las posibilidades
def word_creator():
    config = load_config()
    possibilities = words_possibilities()

    word = []

    for j in range(config["LENGTH_WORD"]):
        palabra = random.choice(possibilities)
        word.append(palabra)

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
        possibilities += string.whitespace
    if config["NUM"]:
        possibilities += string.digits
    if config["SIMBOL"]:
        possibilities += string.punctuation

    return possibilities

def word_genetic(parents):

    for i in parents:
        possibility1 = ""
