from operator import le
import time
import getpass
import copy
import numpy as np
from sklearn.neighbors import kneighbors_graph
from search_algorithms.breadth_first_search import breadthFirstSearch
from search_algorithms.depth_first_search import depthFirstSearch
from search_algorithms.best_first_search import bestFirstSearch
from search_algorithms.a_search import aSearch
from search_algorithms.a_start_search import aStarSearch
from utils.graph import plotGraphWithPath, printGraphConnectivity
from utils.colors import bcolors

# Search Algorithms
search_algorithms = {
    1: breadthFirstSearch,
    2: depthFirstSearch,
    3: bestFirstSearch,
    4: aSearch,
    5: aStarSearch
}

# Getting OS username
try:
    username = getpass.getuser()
except Exception:
    username = 'usuário'
print(f'{bcolors.HEADER}\nSaudações {username}!\n{bcolors.ENDC}')
print('====================================================================================================')
print(f'{bcolors.UNDERLINE}Este programa permite a criação de um grafo knn com o intuito de encontrar o caminho \n'+
'entre dois vértices utilizando de diferentes tipos de algoritmos de busca. Além disso, é possivel\n'+
'gerar a visualização gráfica do grafo com o caminho encontrado.')
print('====================================================================================================\n')

# Getting number of vertices and number of neighbors
print(f'{bcolors.BOLD}Primeiro, vamos criar um grafo knn!\n')
while True:
    try:
        print(f'{bcolors.WARNING}AVISO: quanto maior o número de vértices e vizinhos maior será o tempo de execução e uso de memória. '+
        'Dê preferência a valores ímpares para o número de vizinhos.\n')
        numberOfVertices = int(input(f'{bcolors.OKBLUE}Digite o número de vértices do grafo: {bcolors.ENDC}'))
        k = int(input(f'{bcolors.OKBLUE}Digite o número de vizinhos de cada vértice: {bcolors.ENDC}'))
        if k > 0 and numberOfVertices > k: 
            break
        else:
            print(f'{bcolors.FAIL}\nERRO: o número de vizinhos deve ser maior do que 0 e o número de vértices deve ser maior que o número de vizinhos.\n{bcolors.ENDC}')
    except Exception:
        print(f'{bcolors.FAIL}\nERRO: digite apenas números inteiros.\n{bcolors.ENDC}')

# Generating ramdom vertices
print(f'\n{bcolors.OKCYAN}Gerando vértices aleatórios...\n{bcolors.ENDC}')
vertexArray = np.random.randint(numberOfVertices, size=(numberOfVertices, 2))
print(f'Vértices gerados com {bcolors.OKGREEN}Sucesso{bcolors.ENDC}!\n')

# Generating knn_graph
print(f'{bcolors.OKCYAN}Criando grafo knn...\n{bcolors.ENDC}')
knn_graph = kneighbors_graph(vertexArray, k, mode='distance')
knn_graph = knn_graph.toarray().tolist()
# Creating copy to be be ploted later
knn_graph_copy = copy.deepcopy(knn_graph)
# Cleaning graph and putting neighbour index
for vertex in range(len(knn_graph)):
    for neighbour in range(len(knn_graph[vertex])):
        if knn_graph[vertex][neighbour]:
            knn_graph[vertex][neighbour] = (neighbour, knn_graph[vertex][neighbour])
        else:
            knn_graph[vertex][neighbour] = -1
    knn_graph[vertex] = list(filter(lambda v: v != -1, knn_graph[vertex]))

#printGraphConnectivity(knn_graph)
print(f'Grafo knn criado com {bcolors.OKGREEN}Sucesso{bcolors.ENDC}!\n')

# Getting two input vertices
print(f'{bcolors.BOLD}Agora vamos tentar encontrar o caminho entre dois vértices!\n')
while True:
    try:
        startVertex = int(input(f'{bcolors.OKBLUE}Vértice inicial: {bcolors.ENDC}'))
        endVertex = int(input(f'{bcolors.OKBLUE}Vértice final: {bcolors.ENDC}'))
        if startVertex >= 0 and endVertex >= 0 and startVertex != endVertex and startVertex < numberOfVertices and endVertex < numberOfVertices:
            break
        else:
            print(f'{bcolors.FAIL}\nERRO: os vértices devem ser maiores ou iguais a 0 e menores do que {numberOfVertices}, não podem ser iguais.\n')
    except Exception:
        print(f'{bcolors.FAIL}\nERRO: digite apenas números inteiros.\n')

# Choosing algorithm to perform search
print(f'\n{bcolors.BOLD}Agora escolha qual algoritmo para realizar a busca (número correspondente):\n{bcolors.ENDC}')
while True:
    try:
        print(f'{bcolors.OKBLUE}1- Busca em largura')
        print('2- Busca em profundidade')
        print('3- Busca best first')
        print('4- A')
        print('5- A*')
        print(f'6- Todos os anteriores\n')
        option = int(input(f'Opção: {bcolors.ENDC}'))
        if option > 0 and option < 6:
            print(f'\n{bcolors.OKCYAN}Procurando caminho...{bcolors.ENDC}')
            start = time.time()
            path = search_algorithms[option](knn_graph, startVertex, endVertex, vertexArray)
            stop = time.time()
            if path: # Path found
                print(f'\nCaminho {bcolors.OKGREEN}encontrado{bcolors.ENDC}!\n')
                print(f'{bcolors.HEADER}Tamanho do caminho: {bcolors.ENDC}{len(path)}')
                print(f'{bcolors.HEADER}Tempo de execução: {bcolors.ENDC}{stop - start} segundos')
                print(f'{bcolors.HEADER}Caminho encontrado: \n{bcolors.ENDC}')
                print(f'{bcolors.OKCYAN}INICIO {bcolors.ENDC}-> ', end='')
                for vertex in path:
                    print(f'{vertex} -> ', end='')
                print(f'{bcolors.OKCYAN}FIM{bcolors.ENDC}\n')
                while True: # Plotting path
                    shouldPlot = input(f'Deseja visualizar o grafo com o caminho encontrado? (s/n): ')
                    if shouldPlot == 's' or shouldPlot == 'S':
                        plotGraphWithPath(knn_graph_copy, vertexArray, path)
                        break
                    elif shouldPlot == 'n' or shouldPlot == 'N':
                        break
                    else:
                        print(f'{bcolors.FAIL}\nERRO: digite "s" para sim ou "n" para não.\n{bcolors.ENDC}')
            else: # Path not found
                print(f'\nCaminho {bcolors.FAIL}não encontrado{bcolors.ENDC}.')
            break
        elif option == 6:
            pass
        else:
            print(f'{bcolors.FAIL}\nERRO: escolha uma das opções de 1 a 6, ou 0 para sair.\n{bcolors.ENDC}')
    except Exception:
        print(f'{bcolors.FAIL}\nERRO: digite apenas números inteiros.\n{bcolors.ENDC}')
print(f'\n{bcolors.HEADER}Tchau Tchau, até a próxima! :){bcolors.ENDC}')