# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:51:24 2020

@author: Gustavo Caldas
"""

###Ferramentas de Otimizacao Usando Algoritmos Genéticos
###Exemplo Inicial - Aula 4 
import random 
import numpy as np
from deap import algorithms 
from deap import base
from deap import creator 
from deap import tools


# Coordenadas
ID = [1,2,3,4,5,6,7,8,9,10]
coord = [[18,42], [29,37], [36,28], [35,11], [29,7], [21,15], [8,26], [18,31], [6,4], [50,46]]
customers = [7571,5274,11082,11879,9226,7942, 6295, 4286, 8132, 11344]

individual = np.empty(6) #each individual is a list with 6 coordinates (3 points)

"#Definition of fitness function"
def objective_function(individual):
    xA = individual[0]
    yA = individual[1]
    xB = individual[2]
    yB = individual[3]
    xC = individual[4]
    yC = individual[5]
    # Diâmetro alcancado pelas antenas
    dA = 15
    dB = 12
    dC = 3
    npoints = 10
    # Estabelecendo as variáveis
    alcance = 0
    # Distancia de A em relacao as cidades
    dxA= xA
    dyA = yA 
    distanciaxA = np.empty(npoints)
    distanciayA = np.empty(npoints)
    distancia_A = np.empty(npoints) 
    alcanceA    = 0
    cidadesAtendidasA = [] 
    coberturaA = []
    # Distancia de B em relacao as cidades
    dxB = xB
    dyB = yB 
    distanciaxB = np.empty(npoints)
    distanciayB = np.empty(npoints)
    distancia_B = np.empty(npoints)
    alcanceB    = 0
    cidadesAtendidasB = [] 
    coberturaB = []
    # Distancia de C em relacao as cidades
    dxC = xC
    dyC = yC 
    distanciaxC = np.empty(npoints)
    distanciayC = np.empty(npoints)
    distancia_C = np.empty(npoints)
    alcanceC   = 0
    cidadesAtendidasC = [] 
    coberturaC = []
    # Assinalando as cidades atendidas a partir das coordenadas
    for i in range(npoints):
        #A
        distanciaxA[i] = (coord[i][0] - dxA)**2
        distanciayA[i] = (coord[i][1] - dyA)**2
        distancia_A[i] = np.sqrt(distanciaxA[i] + distanciayA[i])
        if distancia_A[i] <= dA:
            cidadesAtendidasA.append(i)
        #B
        distanciaxB[i] = (coord[i][0] - dxB)**2
        distanciayB[i] = (coord[i][1] - dyB)**2
        distancia_B[i] = np.sqrt(distanciaxB[i] + distanciayB[i])
        if distancia_B[i] <= dB:
            cidadesAtendidasB.append(i)
        #C        
        distanciaxC[i] = (coord[i][0] - dxC)**2
        distanciayC[i] = (coord[i][1] - dyC)**2
        distancia_C[i] = np.sqrt(distanciaxC[i] + distanciayC[i])
        if distancia_C[i] <= dC:
                cidadesAtendidasC.append(i+1)
    
    #Calculando a Cobertura de A
    for j in range(len(cidadesAtendidasA)):     
        for i in range(npoints):
            if(cidadesAtendidasA[j] == i):
                coberturaA.append(customers[i])
                alcanceA = alcanceA + coberturaA[j]
    #Calculando a Cobertura de B
    j = 0           
    for j in range(len(cidadesAtendidasB)):     
         for i in range(npoints):
             if(cidadesAtendidasB[j] == i):
                 coberturaB.append(customers[i])
                 alcanceB = alcanceB + coberturaB[j]
    #Calculando a Cobertura de C
    j = 0           
    for j in range(len(cidadesAtendidasC)):     
        for i in range(npoints):
            if(cidadesAtendidasC[j] == i):
                coberturaC.append(customers[i]) 
                alcanceC = alcanceC + coberturaC[j]
    alcance = alcanceA + alcanceB + alcanceC
    return(alcance)

# Função de restrição que o problema tiver (nem todos os problemas contém restrições)
def FuncaoDeRestricao(individual):
    return True

#GeradorDeIndividuos(ClasseDoIndividuo, FunçãoDeGeraçãoDeNºAleatorio):
def GeradorDeIndividuos(icls, attr_int_function):
  #i = 0
  cromossomo = list()
  # while True: 
  v1 = attr_int_function()
  v2 = attr_int_function()
  v3 = attr_int_function()
  v4 = attr_int_function()
  v5 = attr_int_function()
  v6 = attr_int_function()
    # if FuncaoDeRestricao(v1, v2, v3, v4, v5, v6):
    #   break
    # i = i + 1
  cromossomo.append(v1)
  cromossomo.append(v2)
  cromossomo.append(v3)
  cromossomo.append(v4)
  cromossomo.append(v5)
  cromossomo.append(v6)
  return icls(cromossomo)

"#Definition and initialization"
#Criacao da classe para a funcao objetivo
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
#Criacao dos classe dos Individuos associada a avaliacao de cada inviduo
creator.create("Individual", list, fitness=creator.FitnessMax)

#Initialization
toolbox = base.Toolbox()

# Gerador de atributos inteiros: nome, tipo das variáveis, intervalo (limites inferior e superior)
toolbox.register("attr_int_function", random.randint, 0, 50) #gerando individuos com (x,y) entre 0 e 60

# Inicializador de indivíduo e população
#serve como container
toolbox.register("individual", GeradorDeIndividuos, creator.Individual, toolbox.attr_int_function)   # argumentos cedidos para Gerador de Individuos
toolbox.register("population", tools.initRepeat, list, toolbox.individual)                  # lista de indivíduos

# Incializador de operadores. First argument as alias to existing function
toolbox.register("evaluate", objective_function) # função objetivo
toolbox.register("mate", tools.cxTwoPoint) #offspring from crossover                  
toolbox.register("mutate",  tools.mutFlipBit, indpb=0.15)  #parametrs of probability mutation
toolbox.register("select", tools.selBest) #select

"""## Otimização"""
population = toolbox.population(n=100)
# quantidade de gerações
NGEN=35
bestIndEachGeneration = []
bestInd = []
for gen in range(NGEN):
  print("Geracao: ", gen)
  offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1) #algoritmo genetico: ver doc
  fits = list(toolbox.map(toolbox.evaluate, offspring)) #individuos gerados e avaliacao
  
  indexes = range(len(offspring)) 
  indexes = [x for _,x in sorted(zip(fits, indexes))]
  fits = [fits[x] for x in indexes] #list comprehension - nested 
  offspring = [offspring[x] for x in indexes]
  print(offspring)
  print(fits)
  for fit, ind in zip(fits, offspring):
    ind.fitness.wvalues = fit
  elites_ind = offspring[:max(1, round(0.15*len(offspring)))] #elitismo selecionando apenas %15 do offspring.
  population = toolbox.select(offspring, len(population)-len(elites_ind))
  population.extend(elites_ind)
  bestIndEachGeneration.append([offspring[fits.index(max(fits))], max(fits)])
  bestInd.append(max(bestIndEachGeneration, key=lambda t:t[1])[1])
  print(" Melhor Avaliação dessa geração: ", bestIndEachGeneration[-1][1], "\n", 
        "Melhor Avaliação Geral", max(bestIndEachGeneration, key=lambda t:t[1])[1], "\n",
        "Da geração: ", bestIndEachGeneration.index(max(bestIndEachGeneration, key=lambda t:t[1])), "\n",
        "Cromossomo: ", max(bestIndEachGeneration, key=lambda t:t[1])[0], "\n"
       )

from matplotlib import style
style.use('dark_background')
import matplotlib.pyplot as plt
plt.plot(bestInd)
plt.ylabel('Maior valor da função de aptidão')
plt.show()



