import getpass
import copy
import numpy as np
from sklearn.neighbors import kneighbors_graph
from utils.graph import printGraphConnectivity, findPathAndInfo, plotGraphWithPath
from utils.colors import bcolors

# Getting OS username
try:
    username = getpass.getuser()
except Exception:
    username = 'usuário'
print(f'{bcolors.HEADER}\nSaudações {username}!\n{bcolors.ENDC}')
print('====================================================================================================')
print(f'{bcolors.UNDERLINE}Este programa permite a criação de um grafo knn com o intuito de encontrar o caminho entre dois\n'+
'vértices utilizando de diferentes tipos de algoritmos de busca. Além disso, é possivel gerar a\n'+
'visualização gráfica do grafo com o caminho encontrado.')
print('====================================================================================================\n')

# Getting number of vertices and number of neighbors
print(f'{bcolors.BOLD}Primeiro, vamos criar um grafo knn!{bcolors.ENDC}\n')
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

print(f'Grafo knn criado com {bcolors.OKGREEN}Sucesso{bcolors.ENDC}!\n')

while True: # Ask to show connections
    shouldPlot = input(f'Deseja visualizar as conexões de cada vértice? (s/n): ')
    if shouldPlot == 's' or shouldPlot == 'S':
        printGraphConnectivity(knn_graph)
        break
    elif shouldPlot == 'n' or shouldPlot == 'N':
        break
    else:
        print(f'{bcolors.FAIL}\nERRO: digite "s" para sim ou "n" para não.\n{bcolors.ENDC}')

# Getting two input vertices
print(f'{bcolors.BOLD}\nAgora vamos tentar encontrar o caminho entre dois vértices!{bcolors.ENDC}\n')
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
        print('2- Busca best first')
        print('3- Busca A')
        print('4- Busca A*')
        print('5- Busca em profundidade')
        print(f'6- Todos os anteriores\n')
        option = int(input(f'Opção: {bcolors.ENDC}'))
        if option > 0 and option < 6:
            path = findPathAndInfo(option, knn_graph, startVertex, endVertex, vertexArray)
            if path:
                while True: # Plotting path
                    shouldPlot = input(f'Deseja visualizar o grafo com o caminho encontrado? (s/n): ')
                    if shouldPlot == 's' or shouldPlot == 'S':
                        plotGraphWithPath(knn_graph_copy, vertexArray, path)
                        break
                    elif shouldPlot == 'n' or shouldPlot == 'N':
                        break
                    else:
                        print(f'{bcolors.FAIL}\nERRO: digite "s" para sim ou "n" para não.\n{bcolors.ENDC}')
            break
        elif option == 6:
            for i in range(5):
                path = findPathAndInfo(i+1, knn_graph, startVertex, endVertex, vertexArray)
                if path:
                    while True: # Plotting path
                        shouldPlot = input(f'Deseja visualizar o grafo com o caminho encontrado? (s/n): ')
                        if shouldPlot == 's' or shouldPlot == 'S':
                            plotGraphWithPath(knn_graph_copy, vertexArray, path)
                            break
                        elif shouldPlot == 'n' or shouldPlot == 'N':
                            break
                        else:
                            print(f'{bcolors.FAIL}\nERRO: digite "s" para sim ou "n" para não.\n{bcolors.ENDC}')
            break
        else:
            print(f'{bcolors.FAIL}\nERRO: escolha uma das opções de 1 a 6, ou 0 para sair.\n{bcolors.ENDC}')
    except Exception:
        print(f'{bcolors.FAIL}\nERRO: digite apenas números inteiros.\n{bcolors.ENDC}')
print(f'\n{bcolors.HEADER}Tchau Tchau, até a próxima! :){bcolors.ENDC}')