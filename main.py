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

# Get OS username
try:
    username = getpass.getuser()
except Exception:
    username = 'usuário'
print(f'{bcolors.HEADER}\nSaudações {username}!\n')

# Get number of vertices and number of neighbors
while True:
    try:
        numberOfVertices = int(input(f'{bcolors.OKBLUE}Digite o número de vértices:{bcolors.ENDC} '))
        k = int(input(f'{bcolors.OKBLUE}Digite o número de vizinhos:{bcolors.ENDC} '))
        break
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

# Ploting knn_graph
print(f'{bcolors.OKCYAN}Plotando grafo knn...\n{bcolors.ENDC}')
for x in range(numberOfVertices):
    for y in range(numberOfVertices):
        if knn_graph[x][y] == 1:
            plt.plot([vertexArray[x][0], vertexArray[y][0]], [vertexArray[x][1], vertexArray[y][1]], 'ro-')
plt.show()