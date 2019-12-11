# -*- coding: utf-8 -*-
from caminatav2 import caminata
from distancias import manhattan, euclideana
from multiprocessing import Pool, cpu_count
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#experimento
if __name__ == "__main__":
    desde = 5
    hasta = 10
    replicas = 50
    for i in range(desde, hasta + 1, 1):
        resultados = []
        pasos = 2**i
        dimensiones = 8
        parametros = [(d, pasos, manhattan) for d in range(1, dimensiones + 1)] * replicas
        parametros += [(d, pasos, euclideana) for d in range(1, dimensiones + 1)] * replicas
        with Pool(cpu_count() - 1) as pool:
            resultados.append(pool.starmap(caminata, parametros))

        #preparando los datos
        n = replicas * dimensiones
        info_manhattan = [resultados[0][i] for i in range(0, n)]
        info_euclideana = [resultados[0][i] for i in range(n, n * 2)]
        datos_manhattan = {"Dimension":[x[1] for x in info_manhattan], "Probabilidad":[x[0] for x in info_manhattan]}  
        datos_euclideana = {"Dimension":[x[1] for x in info_euclideana], "Probabilidad":[x[0] for x in info_euclideana]}
        df_manhattan = pd.DataFrame(datos_manhattan)
        df_euclideana = pd.DataFrame(datos_euclideana)

        #plot
        sns.set(style = "darkgrid")
        fig, axs = plt.subplots(1, 2, sharey=True)
        sns.boxplot(x = "Dimension", y = "Probabilidad", data = df_manhattan, ax = axs[0], palette = "GnBu_d")
        sns.boxplot(x = "Dimension", y = "Probabilidad", data = df_euclideana, ax = axs[1], palette = "BuGn_r")
        axs[0].set_title("Manhattan")
        axs[1].set_title("Euclideana")
        axs[0].set_xlabel('Dimensión')
        axs[1].set_xlabel('Dimensión')
        axs[0].set_ylabel('Probabilidad')
        axs[1].set_ylabel('')
        plt.ylim(top = 1, bottom = 0)
        plt.yticks(np.arange(0, 1.1, 0.1))
        plt.savefig(f'{pasos}pasos.png')
        plt.close()
        print(f"terminando {pasos} pasos");
