#!/usr/bin/python3

# chaque combinaisons des dixNs avec chaque unité (différent de la dixN)
for dixN in range(10):
    for unité in range(dixN + 1, 10):
        print("{:d}{:d}".format(dixN, unité), end=", " if dixN < 8 else "\n")
