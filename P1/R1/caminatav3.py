from random import random, randint
from time import time

def caminata(dim, pasos):
    tiempo1 = time()
    pos = [0] * dim
    for t in range(pasos):
        cambiar = randint(0, dim - 1)
        cambio = 1 if random() < 0.5 else -1
        pos[cambiar] += cambio
    tiempo2 = time()
    tiempo = tiempo2 - tiempo1
    return(tiempo * 1000, pasos)
