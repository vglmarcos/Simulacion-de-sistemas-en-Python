from random import random, randint
from time import time
from multiprocessing import Pool, cpu_count

def caminataPAR(dim, pasos):
    tiempo1 = time()
    pos = [([0] * dim, dim)]
    with Pool(cpu_count() - 1) as pool:
        pool.starmap(paso, pos * pasos)
    tiempo2 = time()
    tiempo = tiempo2 - tiempo1
    return(tiempo * 1000)

def paso(pos, dim):
    cambiar = randint(0, dim - 1)
    cambio = 1 if random() < 0.5 else -1
    pos[cambiar] += cambio
    return(pos)

def caminata(dim, pasos):
    tiempo1 = time()
    pos = [0] * dim
    for t in range(pasos):
        cambiar = randint(0, dim - 1)
        cambio = 1 if random() < 0.5 else -1
        pos[cambiar] += cambio
    tiempo2 = time()
    tiempo = tiempo2 - tiempo1
    return(tiempo * 1000)


