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



"#Definition of fitness function"
#O objetivo desse problema é minimizar os custos.
def fitness_function(individual):
    # Diâmetro alcancado pelas antenas
    dA = individual[0]
    dB = individual[1]
    dC = individual[2]
    custoA = 970*dA
    custoB = 970*dB
    custoC = 970*dC
    custo = custoA + custoB + custoC
    return custo,
# calculo do alcance e das cidades atendidas
def FuncaoDeRestricao(individual):
    # Coordenadas das Cidades
    #cont = 0
    #ID = [1,2,3,4,5,6,7,8,9,10]
    coord = [[18,42], [29,37], [36,28], [35,11], [29,7], [21,15], [8,26], [18,31], [6,4], [50,46]]
    customers = [7571,5274,11082,11879,9226,7942, 6295, 4286, 8132, 11344]
    npoints = 10 # sao 10 cidades
    #Posicao das antenas já dada
    xA = 22
    yA = 11
    xB = 12
    yB = 33
    xC = 41
    yC = 37
    # Diâmetro alcancado pelas antenas
    dA = individual[0]
    dB = individual[1]
    dC = individual[2]
    # Estabelecendo as variáveis
    #alcance = 0
    #cidadesAtendidas = []
    cidades =  []
    
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
            cidadesAtendidasA.append(i) # alocando as cidades atendidas dentro do diâmetro de da antena
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
           cidadesAtendidasC.append(i)
    
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
    # Uma maneira alternativa seria gerar valores de verdadeiro e falso
    # Resultados
    #Alcance total de clientes
    #alcance = alcanceA + alcanceB + alcanceC
    #Cidades 
    cidades = sorted(cidadesAtendidasA + cidadesAtendidasB + cidadesAtendidasC)
    no_cidadesAtendidas = [len(cidadesAtendidasA), len(cidadesAtendidasB),len(cidadesAtendidasC)]
    if(all([1 if i >= 3 else 0 for i in no_cidadesAtendidas]) or (len(cidades) == npoints)):
          return True
    return False

# Função de restrição que o problema tiver (nem todos os problemas contém restrições)
#def FuncaoDeRestricao(individual): 
      #city, A, B, C  =  alcance(individual)
      
      #Restricao
      #Garantindo que cada antena atenda pelo menos a 3 cidades
     
      #elif(any(no_cidadesAtendidas) <= 3):
          #return False
      #return False
      #Garantindo que todas as cidades sejam atendidas (mapeando)
      #i = 0
      #j = 0
      #for i,j in city,ID:
       # if i == j:
        #i = i + 1
      #return True

#GeradorDeIndividuos(ClasseDoIndividuo, FunçãoDeGeraçãoDeNºAleatorio):
def GeradorDeIndividuos(icls, attr_int_function):
  cromossomo = list()
  while True:
      v1 = attr_int_function()
      v2 = attr_int_function()
      v3 = attr_int_function()
      print(v1,v2,v3)
      print(FuncaoDeRestricao([v1, v2, v3]))
      if(FuncaoDeRestricao([v1, v2, v3])):break #caso atenda a condiçao de restrição, eu paro
  cromossomo.append(v1) 
  cromossomo.append(v2)
  cromossomo.append(v3)
  return icls(cromossomo)

 # Função para cálculo da penalização da função objetivo para os casos em que o individuo não satisfaça as restrições
def distance(individual):
  constraintA = 0
  constraintB = 0
  constraintC = 0
  alcanceA = individual[0]
  alcanceB = individual[1]
  alcanceC = individual[2]
  xA = 22
  yA = 11
  xB = 12
  yB = 33
  xC = 41
  yC = 37
  localizacaoAntenasFisica = [(18, 42), (29, 37), (36, 28), (35, 11), (28, 7), (21,15), (8, 26), (18, 31), (6, 4), (50, 46)]
  for localizacaoAntena in localizacaoAntenasFisica:
    dist = (((xA-localizacaoAntena[0])**2) + ((yA-localizacaoAntena[1])**2) + alcanceA)
    if((np.sqrt(((xA-localizacaoAntena[0])**2) + ((yA-localizacaoAntena[1])**2)) > alcanceA)):
      constraintA = constraintA + dist
    dist = (((xB-localizacaoAntena[0])**2) + ((yB-localizacaoAntena[1])**2) + alcanceB)
    if((np.sqrt(((xB-localizacaoAntena[0])**2) + ((yB-localizacaoAntena[1])**2)) > alcanceB)):
      constraintB = constraintB + dist
    dist = (((xC-localizacaoAntena[0])**2) + ((yC-localizacaoAntena[1])**2) + alcanceC)
    if((np.sqrt(((xC-localizacaoAntena[0])**2) + ((yC-localizacaoAntena[1])**2)) > alcanceC)):
      constraintC = constraintC + dist
  return (constraintA**2 + constraintB**2 + constraintC**2)**2   
    

"#Definition and initialization"
#Criacao da classe para a funcao objetivo
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
#Criacao dos classe dos Individuos associada a avaliacao de cada inviduo
creator.create("Individual", list, fitness=creator.FitnessMin)

#Initialization
toolbox = base.Toolbox()

# Gerador de atributos inteiros: nome, tipo das variáveis, intervalo (limites inferior e superior)
toolbox.register("attr_int_function", random.randint, 9, 25) #gerando individuos com (x,y) entre 0 e 60

# Inicializador de indivíduo e população
#serve como container
toolbox.register("individual", GeradorDeIndividuos, creator.Individual, toolbox.attr_int_function)   # argumentos cedidos para Gerador de Individuos
toolbox.register("population", tools.initRepeat, list, toolbox.individual)                  # lista de indivíduos

# Incializador de operadores. First argument as alias to existing function
toolbox.register("evaluate", fitness_function) # função objetivo
# Registro da função de penalidade caso o individuo não obedeça as restrições
toolbox.decorate("evaluate", tools.DeltaPenalty(FuncaoDeRestricao, 0,distance)) ##muito importante!! 
toolbox.register("mate", tools.cxTwoPoint) #offspring from crossover                  
toolbox.register("mutate",  tools.mutFlipBit, indpb=0.05)  #parametrs of probability mutation
toolbox.register("select", tools.selTournament, tournsize=4)

"""## Otimização"""
pop = toolbox.population(n=120)                           # inicialização da pop
hof = tools.HallOfFame(1)                                 # melhor indivíduo
stats = tools.Statistics(lambda ind: ind.fitness.values)  # estatísticas
stats.register("avg", np.mean)
stats.register("std", np.std)
stats.register("min", np.min)
stats.register("max", np.max)

pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.7, ngen=15, stats=stats, halloffame=hof, verbose=True) #aumentei mut = 0.7
# Melhor solução
print("Melhor Indivíduo:")
print(hof[0])

# Verificação da função de restrição
print(FuncaoDeRestricao(hof[0]))

# Melhor resultado da função objetivo
print("Melhor Resultado da Função Objetivo:", fitness_function(hof[0]))

