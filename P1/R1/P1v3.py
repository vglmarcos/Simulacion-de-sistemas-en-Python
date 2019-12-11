# -*- coding: utf-8 -*-
from caminatav3 import caminata
from multiprocessing import Pool, cpu_count
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#experimento
if __name__ == "__main__":
    replicas = 100
    dimensiones = 8
    desde = 12
    hasta = 17
    for dim in range(1, dimensiones + 1, 1):
        resultados = []
        parametros = [(dim, 2**i) for i in range(desde, hasta + 1, 1)] * replicas
        
        with Pool(cpu_count() - 1) as pool:
            resultados.append(pool.starmap(caminata, parametros))
            
        #preparando los datos
        n = replicas * ((hasta + 1) - desde)
        info = [resultados[0][i] for i in range(0, n)]
        datos = {"Pasos":[x[1] for x in info], "Tiempo":[x[0] for x in info]}  
        df = pd.DataFrame(datos)
        promedios = []
        for i in range(desde, hasta + 1, 1):
            promedios.append(sum([tiempo for (tiempo, pasos) in info if pasos == 2**i]) / replicas)

        #plot
        limite = 1000
        step = 100
        sns.set(style = "darkgrid")
        plt.ylim(top = limite, bottom = 0)
        plt.yticks([i for i in range(0, limite + 1, step)])
        ax = sns.boxplot(x = "Pasos", y = "Tiempo", data = df, palette = "GnBu_d")
        pasos = [2**i for i in range(desde, hasta + 1, 1)]
        colores = ['#37535e', '#3b748a', '#4095b5', '#52aec9', '#72bfc4', '#93d0bf']
        for i in range(len(promedios)):
            plt.axhline(promedios[i], c = colores[i] if len(promedios) == 6 else 'r', linestyle = 'dashed',
                        label = f"{round(promedios[i], 2)} ms en {pasos[i]} pasos.", lw = 1)
        ax.set_title(f'Dimensión {dim}')
        ax.set_xlabel('Pasos de la caminata')
        ax.set_ylabel('Tiempo de ejecución (ms)')
        plt.legend(title = "Promedios:", loc = 'upper left')
        plt.savefig(f'dim{dim}.png')
        plt.close()
        print(f'terminando dimensión {dim}')
