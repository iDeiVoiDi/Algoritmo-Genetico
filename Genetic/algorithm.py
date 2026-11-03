from config.config import load_config

def get_puntuation(poblation):
    config = load_config()
    objetive = config["OBJETIVE_WORD"]
    puntuation = []

    for i in poblation:
        word_puntuation = 0

        for char_p, char_o in zip(i, objetive):
            if char_p == char_o:
                word_puntuation += 1
        
        puntuation.append(word_puntuation)

    return puntuation

def organizator(poblation, puntuation):
    config = load_config()

    for i in range(config["WORDS_FOR_GEN"] - 1):
        for j in range(config["WORDS_FOR_GEN"] - i - 1):
            if puntuation[j] < puntuation[j + 1]:
                puntuation[j], puntuation[j + 1] = puntuation[j + 1], puntuation[j]
                poblation[j], poblation[j + 1] = poblation[j + 1], poblation[j]

    return poblation, puntuation

def get_parents(poblation):
    config = load_config()
    parents = []

    for i in range(config["PARENTS_WORDS"]):
        parents.append(poblation[i])

    return parents


