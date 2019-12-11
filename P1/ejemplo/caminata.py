from random import random, randint
from distancias import manhattan, euclideana

def caminata(dim, dur, dist):
    pos = [0] * dim
    mayor = 0
    distancia = "manhattan" if dist == manhattan else "euclideana"
    for t in range(dur):
        cambiar = randint(0, dim - 1)
        cambio = 1 if random() < 0.5 else -1
        pos[cambiar] += cambio
        d = dist(pos, [0] * dim)
        if mayor < d:
            mayor = d
    return(distancia, mayor, dim)
