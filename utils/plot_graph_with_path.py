import matplotlib.pyplot as plt
from utils.colors import bcolors

def plotGraphWithPath(graph, dotsArray, path):
    print(f'{bcolors.OKCYAN}\nPlotando grafo knn...{bcolors.ENDC}')
    for x in range(len(dotsArray)):
        for y in range(len(dotsArray)):
            if x in path and y in path:
                plt.plot([dotsArray[x][0], dotsArray[y][0]], [dotsArray[x][1], dotsArray[y][1]], 'bo-')
            elif graph[x][y] == 1:
                plt.plot([dotsArray[x][0], dotsArray[y][0]], [dotsArray[x][1], dotsArray[y][1]], 'ro-')
    plt.show()