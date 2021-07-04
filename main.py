import getpass
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import kneighbors_graph

# Change output color
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Getting OS username
try:
    username = getpass.getuser()
except Exception:
    username = 'usuário'
print(f'{bcolors.HEADER}\nSaudações {username}!\n{bcolors.ENDC}')
print('====================================================================================================')
print(f'{bcolors.UNDERLINE}Este programa permite a criação e visualização de um grafo knn com o intuito de encontrar o caminho \n'+
'entre dois vértices utilizando de diferentes tipos de algoritmos de busca. Além disso, é possivel\n'+
'gerar diferentes visualizações gráficas do comportamento de cada um dos algortimos.')
print('====================================================================================================\n')

# Getting number of vertices and number of neighbors
print(f'Primeiro, vamos criar um grafo knn!\n')
while True:
    try:
        numberOfVertices = int(input(f'{bcolors.OKBLUE}Digite o número de vértices do grafo: {bcolors.ENDC}'))
        k = int(input(f'{bcolors.OKBLUE}Digite o número de vizinhos de cada vértice: {bcolors.ENDC}'))
        if k > 0 and numberOfVertices > k:
            break
        else:
            print(f'{bcolors.FAIL}ERRO: o número de vizinhos deve ser maior do que 0 e o número de vértices deve ser maior que o número de vizinhos{bcolors.ENDC}')
    except Exception:
        print(f'{bcolors.FAIL}ERRO: digite apenas números inteiros{bcolors.ENDC}')

# Generating ramdom vertices
print(f'\n{bcolors.OKCYAN}Gerando vértices aleatórios...\n{bcolors.ENDC}')
vertexArray = np.random.randint(numberOfVertices, size=(numberOfVertices, 2))
print(f'Vértices gerados com {bcolors.OKGREEN}Sucesso!\n{bcolors.ENDC}')

# Generating knn_graph
print(f'{bcolors.OKCYAN}Criando grafo knn...\n{bcolors.ENDC}')
knn_graph = kneighbors_graph(vertexArray, k, mode='connectivity')
knn_graph = knn_graph.toarray()
print(f'Grafo knn criado com {bcolors.OKGREEN}Sucesso!\n{bcolors.ENDC}')

# Getting two input vertices
print(f'Agora vamos tentar encontrar o caminho entre dois vértices!\n')
while True:
    try:
        startVertex = int(input(f'{bcolors.OKBLUE}Vértice inicial: {bcolors.ENDC}'))
        endVertex = int(input(f'{bcolors.OKBLUE}Vértice final: {bcolors.ENDC}'))
        if startVertex > 0 and endVertex > 0 and startVertex != endVertex and startVertex < numberOfVertices and endVertex < numberOfVertices:
            break
        else:
            print(f'{bcolors.FAIL}ERRO: os vértices devem ser maiores ou iguais a 0 e menores do que {numberOfVertices}, não podem ser iguais{bcolors.ENDC}')
    except Exception:
        print(f'{bcolors.FAIL}ERRO: digite apenas números inteiros{bcolors.ENDC}')


# Ploting knn_graph
print(f'{bcolors.OKCYAN}Plotando grafo knn...\n{bcolors.ENDC}')
for x in range(numberOfVertices):
    for y in range(numberOfVertices):
        if knn_graph[x][y] == 1:
            plt.plot([vertexArray[x][0], vertexArray[y][0]], [vertexArray[x][1], vertexArray[y][1]], 'ro-')
plt.show()