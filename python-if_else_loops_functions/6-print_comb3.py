#!/usr/bin/python3

# chaque combinaisons des dizaines avec chaque unité (différent de la dizaine)
for dizaine in range(10):
    for unité in range(dizaine + 1, 10):
        print("{:d}{:d}".format(dizaine, unité), end=", " if i < 8 else "\n")
