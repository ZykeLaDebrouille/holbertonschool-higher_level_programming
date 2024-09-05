#!/usr/bin/python3
import sys

if __name__ == "__main__":
    resultat = 0
    for argc in sys.argv[1:]:
        resultat += int(argc)
    print(resultat)
