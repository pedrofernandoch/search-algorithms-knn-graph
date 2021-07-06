from operator import length_hint
import matplotlib.pyplot as plt
from numpy import string_
from utils.colors import bcolors

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
        print(f'{i}: [ ', end='')
        length = len(graph[i])
        for j in range(length):
            print(f'{graph[i][j][0]}{comma if j != (length -1) else rightSquareBracket}', end='')
        print()