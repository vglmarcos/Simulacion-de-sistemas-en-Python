# -*- coding: utf-8 -*-
from caminatav1 import caminata
from distancias import manhattan, euclideana
from multiprocessing import Pool, cpu_count
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#experimento
if __name__ == "__main__":
    resultados = []
    replicas = 100
    pasos = 100
    dimensiones = 8
    parametros = [(d, pasos, manhattan) for d in range(1, dimensiones + 1)] * replicas
    parametros += [(d, pasos, euclideana) for d in range(1, dimensiones + 1)] * replicas
    with Pool(cpu_count() - 1) as pool:
        resultados.append(pool.starmap(caminata, parametros))

    #preparando los datos
    n = replicas * dimensiones
    resultados_manhattan = [resultados[0][i] for i in range(0, n)]
    resultados_euclideana = [resultados[0][i] for i in range(n, n * 2)]
    info_manhattan = [(mayor, dim) for (_ ,mayor, dim) in resultados_manhattan]
    info_euclideana = [(mayor, dim) for (_ ,mayor, dim) in resultados_euclideana]
    datos_manhattan = {"Dimension":[x[1] for x in info_manhattan], "Distancia":[x[0] for x in info_manhattan]}  
    datos_euclideana = {"Dimension":[x[1] for x in info_euclideana], "Distancia":[x[0] for x in info_euclideana]}
    dataframe_manhattan = pd.DataFrame(datos_manhattan)
    dataframe_euclideana = pd.DataFrame(datos_euclideana)
    
    #limite en y
    max_caminata = max([maximo for (_, maximo, _) in resultados[0]])
    step = 10
    limite = (((max_caminata // step) * step) + step)

    #plot manhattan
    #plt.style.use('ggplot')
    sns.set(style = "darkgrid")
    plt.ylim(top = limite, bottom = 0)
    plt.yticks([i for i in range(0, limite + 1, step)])
    ax = sns.boxplot(x = "Dimension", y = "Distancia", data = dataframe_manhattan, palette = "GnBu_d")
    ax.set_title('Manhattan')
    ax.set_xlabel('Dimensión')
    ax.set_ylabel('Distancia máxima')
    plt.savefig('manhattan.png')
    plt.close()
    
    #plot euclideana
    sns.set(style = "darkgrid")
    plt.ylim(top = limite, bottom = 0)
    plt.yticks([i for i in range(0, limite + 1, step)])
    ax = sns.boxplot(x = "Dimension", y = "Distancia", data = dataframe_euclideana, palette = "BuGn_r")
    ax.set_title('Euclideana')
    ax.set_xlabel('Dimensión')
    ax.set_ylabel('Distancia máxima')
    plt.savefig('euclideana.png')
    plt.close()

#print(plt.style.available)
