#Importar CV2 E Numpy
import cv2
import queue
import numpy as np
import matplotlib.pyplot as plt
#Funcao para contar imagem e rotular
def rotula_imagem(binario):
    #Tamanho da Imagem
    linhas, colunas = binario.shape
    lista = []
    rotulo = 100
    alterou = 0
    while (alterou == 0):
        alterou = 1
        for i in range(1, linhas - 1):
            for j in range(1, colunas - 1):
                if binario.item(i, j) != 0:
                    rv = rotulo_vizinho(binario, i, j)
                    if rv == 255:
                        binario.itemset((i, j), rotulo)
                        rotulo += 1
                        alterou = 0
                    elif rv != binario.item(i, j):
                        binario.itemset((i, j), rv)
                        alterou = 0
        #cv2.imshow('imagem', binario)
        #print(alterou)
        #tecla = cv2.waitKey(5)

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            # adiciona o rotulo na lista para fazer a contagem posteriormente
            rotulo = binario.item(i, j)
            if rotulo not in lista and rotulo != 0:
                lista.append(rotulo)

    return lista
def rotulo_vizinho (binario, i, j):
    r = 255
    for ii in range(i-1, i+2):
        #print(r)
        for jj in range(j-1, j+2):
            if binario.item(ii, jj) != 0 and binario.item(ii, jj) < r:
                r = binario.item(ii, jj)
    return r
################
### Imagem A ###
################
# Mascara
mascara = np.ones((3, 3), np.uint8)
#Abre a imagem
img = cv2.imread('img01-a.png',0)
#Cria a imagem binaria e grava
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
binario = thresh1
# Dilatacao 1
binario = cv2.dilate(binario, mascara, iterations=1)
# Erosao 2
binario = cv2.erode(binario, mascara, iterations=2)
# Abertura
binario = cv2.morphologyEx(binario, cv2.MORPH_OPEN, mascara)
# Dilatacao 2
binario = cv2.dilate(binario, mascara, iterations=2)
# Lista com os rotulos
total = 0
# Chama a funcao
total = rotula_imagem(binario)

cv2.imshow('Imagem 1', binario)
print(f'Total Imagem A : {len(total) -1}')


#Qualquer tela para fechar  imagem

#####################
#### Imagem B #######
#####################
# Mascara
mascara2 = np.ones((3, 3), np.uint8)
#Abre a imagem
img = cv2.imread('img01-b.png',0)
#Cria a imagem binaria e grava
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
binario2 = thresh1
# Dilatacao 1
binario2 = cv2.dilate(binario2, mascara2, iterations=1)
# Erosao 2
binario2 = cv2.erode(binario2, mascara2, iterations=2)
# Abertura
binario2 = cv2.morphologyEx(binario2, cv2.MORPH_OPEN, mascara2)
# Dilatacao 3
binario2 = cv2.dilate(binario2, mascara2, iterations=3)

total = rotula_imagem(binario2)

cv2.imshow('Imagem 2', binario2)
print(f'Total Imagem B : {len(total) -1}')
#Qualquer tela para fechar  imagem
tecla = cv2.waitKey(0)