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

    for i in range(config["WORDS_FOR_GEN"]):
        if puntuation[i] < puntuation[i + 1]:
            puntuation[i], puntuation[i + 1] = puntuation[i + 1], puntuation[i]
            poblation[i], poblation[i + 1] = poblation[i + 1], poblation[i]

    return poblation, puntuation

