import random
import string
epsilon1 = 0.2
epsilon2 = 0.4

def random_choice_alter():
    options = [True, False]
    weights = [epsilon1, 1-epsilon1]
    return random.choices(options, weights)[0]



def random_choice_alter_type():
    options = [True, False]
    weights = [epsilon2, 1-epsilon2]
    return random.choices(options, weights)[0]


def replace_characters(text):
    new_text = ""
    for char in text:
        if random_choice_alter(): # smaller or bigger or equal:
            if random_choice_alter_type:
                new_text += '*'
            else:
                new_text += random.choice(string.ascii_letters)
        else:
            new_text += char
    return new_text



with open("log.txt", "r") as file:
    lines = file.readlines()
    with open("new_log.txt", "w") as out_file:
        for line in lines:
            new_line = replace_characters(line)
            out_file.write(new_line)


