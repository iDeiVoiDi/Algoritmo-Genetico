from config.config import load_config, save_config
from utils import ask_word
from words import word_creator, list_creator
from algorithm import get_puntuation, organizator, get_parents


def main():
    config = load_config()

    azar, OBJETIVE = ask_word()

    if azar:
        OBJETIVE = word_creator()
        print(OBJETIVE)

    config["OBJETIVE_WORD"] = OBJETIVE
    save_config(config)

    GEN = 0
    win = False
    parents = []
    while not win:
        poblation = list_creator(parents)
        puntuation = get_puntuation(poblation)
        poblation, puntuation = organizator(poblation, puntuation)
        parents = get_parents(poblation)

        GEN += 1
        if GEN % 20 == 0:
            print(poblation[0])
            
        if poblation[0] == config["OBJETIVE_WORD"]:
            win = True

    print(f"Conseguido {config["OBJETIVE_WORD"]} {poblation[0]}")

main()