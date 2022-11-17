# Oppgave 1
import random

def random_string_list(length): 
    return ["".join([chr(random.randint(97, 122)) for _ in range(10)]) for _ in range(length)]



