from config.config import load_config
from words import words_possibilities

# Pide una palabra objetivo valida con la configuracion
def ask_word():
    config = load_config()
    possibilities = words_possibilities()

    question = config["QUESTION"].format(**config)

    while True:
        answer = input(f"{question}").strip()

        if answer.lower() == "x":
            return True, ""

        is_length_valid = len(answer) == config["LENGTH_WORD"]
        is_chars_valid = all(char in possibilities for char in answer)

        if is_length_valid and is_chars_valid:
            return False, answer

        print(f"| Tiene q tener {config['LENGTH_WORD']} caracteres permitidos o x para aleatoria")