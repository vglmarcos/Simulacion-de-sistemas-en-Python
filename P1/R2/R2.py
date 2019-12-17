# -*- coding: utf-8 -*-
from caminatav4 import caminataPAR, caminata
from multiprocessing import Pool, cpu_count
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#experimento
if __name__ == "__main__":
    desde = 19
    hasta = 21
    replicas = 50
    resultados_par = []
    resultados_sec = []
    for i in range(desde, hasta + 1, 1):
        pasos = 2**i
        dimensiones = 8
        parametros = [(dimensiones, pasos)] * replicas
        
        for i in range(replicas):
            resultados_par.append(caminataPAR(dimensiones, pasos))

        with Pool(cpu_count() - 1) as pool:
            resultados_sec += pool.starmap(caminata, parametros)

        print(f"Terminando con {pasos} pasos.")

    pasos_tot = [2**x for x in range(desde, hasta + 1, 1) for y in range(replicas)]
    #preparando los datos
    datos_par = {"Pasos" : pasos_tot, "Tiempo" : [x for x in resultados_par]} 
    datos_sec = {"Pasos" : pasos_tot, "Tiempo" : [x for x in resultados_sec]}
    df_par = pd.DataFrame(datos_par)
    df_sec = pd.DataFrame(datos_sec)

    #plot
    sns.set(style = "darkgrid")
    fig, axs = plt.subplots(1, 2, sharey=True)
    sns.boxplot(x = "Pasos", y = "Tiempo", data = df_par, ax = axs[0], palette = "GnBu_d")
    sns.boxplot(x = "Pasos", y = "Tiempo", data = df_sec, ax = axs[1], palette = "BuGn_r")
    axs[0].set_title("Paralelo")
    axs[1].set_title("Secuencial")
    axs[0].set_xlabel('Pasos')
    axs[1].set_xlabel('Pasos')
    axs[0].set_ylabel('Tiempo (ms)')
    axs[1].set_ylabel('')
    plt.savefig('Tiempos.png')
    plt.close()

        
    
