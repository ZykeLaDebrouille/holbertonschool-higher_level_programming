#!/usr/bin/python3

# Imprimer l'alphabet en minuscules sans nouvelle ligne sans 'e' ni 'q'
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{:c}".format(i), end="")
