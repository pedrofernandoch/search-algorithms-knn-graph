import time
import matplotlib.pyplot as plt
from search_algorithms.breadth_first_search import breadthFirstSearch
from search_algorithms.depth_first_search import depthFirstSearch
from search_algorithms.best_first_search import bestFirstSearch
from search_algorithms.a_search import aSearch
from search_algorithms.a_star_search import aStarSearch
from utils.colors import bcolors

# Search Algorithms
search_algorithms = {
    1: {'func': breadthFirstSearch, 'title': 'Busca em largura'},
    2: {'func': bestFirstSearch, 'title': 'Busca best first'},
    3: {'func': aSearch, 'title': 'Busca A'},
    4: {'func': aStarSearch, 'title': 'Busca A*'},
    5: {'func': depthFirstSearch, 'title': 'Busca em profundidade'},
}

def plotGraphWithPath(graph, dotsArray, path):
    print(f'{bcolors.OKCYAN}\nPlotando grafo knn...{bcolors.ENDC}')
    for x in range(len(dotsArray)):
        for y in range(len(dotsArray)):
            if x in path and y in path:
                plt.plot([dotsArray[x][0], dotsArray[y][0]], [dotsArray[x][1], dotsArray[y][1]], 'bo-')
            elif graph[x][y]:
                plt.plot([dotsArray[x][0], dotsArray[y][0]], [dotsArray[x][1], dotsArray[y][1]], 'ro-')
    plt.show()

def printGraphConnectivity(graph):
    comma = ', '
    rightSquareBracket = ' ]'
    for i in range(len(graph)):
        print(f'Vértice {i} está conectado com os vértices: [ ', end='')
        length = len(graph[i])
        for j in range(length):
            print(f'{graph[i][j][0]}{comma if j != (length -1) else rightSquareBracket}', end='')
        print()

def findPathAndInfo(option, knn_graph, startVertex, endVertex, vertexArray):
    title = search_algorithms[option]['title']
    print(f'\n{bcolors.OKCYAN}Procurando caminho usando {title}...{bcolors.ENDC}')
    start = time.time()
    path = search_algorithms[option]['func'](knn_graph, startVertex, endVertex, vertexArray)
    stop = time.time()
    execTime = stop - start
    if path: # Path found
        print(f'\nCaminho {bcolors.OKGREEN}encontrado{bcolors.ENDC}!\n')
        print(f'{bcolors.HEADER}Tamanho do caminho: {bcolors.ENDC}{len(path)}')
        print(f'{bcolors.HEADER}Tempo de execução: {bcolors.ENDC}{execTime} segundos')
        print(f'{bcolors.HEADER}Caminho encontrado: \n{bcolors.ENDC}')
        print(f'{bcolors.OKCYAN}INICIO {bcolors.ENDC}-> ', end='')
        for vertex in path:
            print(f'{vertex} -> ', end='')
        print(f'{bcolors.OKCYAN}FIM{bcolors.ENDC}\n')
        return path
    else: # Path not found
        print(f'\nCaminho {bcolors.FAIL}não encontrado{bcolors.ENDC}.')
        return None