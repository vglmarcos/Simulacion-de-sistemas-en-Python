from random import random, randint
from distancias import manhattan, euclideana

def caminata(dim, pasos, dist):
    pos = [0] * dim
    origen = 0
    tipo_dist = "manhattan" if dist == manhattan else "euclideana"
    for t in range(pasos):
        cambiar = randint(0, dim - 1)
        cambio = 1 if random() < 0.5 else -1
        pos[cambiar] += cambio
        d = dist(pos, [0] * dim)
        if d == 0:
            origen += 1
    return(origen/pasos, dim, tipo_dist)
