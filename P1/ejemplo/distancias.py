from math import sqrt

def euclideana(p1, p2):
    return sqrt(sum([(c2 - c1)**2 for (c1, c2) in zip(p1, p2)]))

def manhattan(p1, p2):
    return sum([abs(c2 - c1) for (c1, c2) in zip(p1, p2)])

