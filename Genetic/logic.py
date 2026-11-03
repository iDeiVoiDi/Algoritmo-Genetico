from config.config import load_config, save_config
from utils import ask_word
from words import word_creator, list_creator
from algorithm import get_puntuation, organizator


def main():
    config = load_config()

    azar, OBJETIVE = ask_word()

    if azar:
        OBJETIVE = word_creator()

    config["OBJETIVE_WORD"] = OBJETIVE
    save_config(config)

    GEN = 0
    win = False
    parents = []
    while not win:
        poblation = list_creator(parents)
        puntuation = get_puntuation(poblation)
        poblation, puntuation = organizator(poblation, puntuation)
        