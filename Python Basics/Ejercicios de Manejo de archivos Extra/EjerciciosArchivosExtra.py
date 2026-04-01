def one_liner(p_path):
    with open(p_path, "r") as v_file, open("one_line_"+p_path, "w") as new_file:
        new_file.write(" ".join(v_file.read().splitlines()))

one_liner("canciones.txt")

def word_count(p_path):
    counter = 0
    with open(p_path, "r") as v_file:
        for line in v_file.readlines():
            counter += len(line.split())
    return counter

print(f"Este archivo contiene {word_count("canciones.txt")} palabras")

def upper_file(p_path):
    with open(p_path, "r") as v_file, open("UPPER_"+p_path.upper(), "w") as new_file:
        for line in v_file.readlines():
            new_file.write(line.upper())

upper_file("canciones.txt")

def append_text(p_text, p_path):
    with open(p_path, "a") as v_file:
        v_file.write(p_text)

append_text(input("Ingrese un texto: "), "appendable.txt")