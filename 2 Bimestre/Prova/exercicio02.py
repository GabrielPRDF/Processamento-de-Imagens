#Importar CV2 E Numpy
import cv2
import queue
import numpy as np
#import matplotlib.pyplot as plt

#captura = cv2.VideoCapture('video.mp4')
captura = cv2.VideoCapture(0)

while (1):
    ret, frame = captura.read()
    # Copia da imagem original
    copia = frame.copy()
    # Imagem de saida(copia original)
    saida = frame.copy()
    # Tamanho da Imagem
    linhas, colunas, cor= frame.shape
    # Cria a imagem que recebera binario
    binario = np.ones((linhas, colunas), np.uint8)
    # Encontra o possivel pixel de pele
    for i in range(0, linhas):
        for j in range(0, colunas):
            b = frame.item(i, j, 0)
            r = frame.item(i, j, 2)
            g = frame.item(i, j, 1)
            if r > 95 and g > 40 and b > 20 and abs(r - g) > 15 and r > g and r > b:
                binario.itemset(i, j, 255)
            else:
                binario.itemset(i, j, 0)
    # Mascara 3*3
    mascara = np.ones((3, 3), np.uint8)
    # Dilatacao 2
    binario = cv2.dilate(binario, mascara, iterations=2)
    # Erosao 4
    binario = cv2.erode(binario, mascara, iterations=4)
    # Mascara
    mascara2 = np.ones((10, 10), np.uint8)
    # Dilatacao 6
    binario = cv2.dilate(binario, mascara2, iterations=8)
    # Erosao 1
    binario = cv2.erode(binario, mascara2, iterations=1)

    # For para colocar o pixel correto
    for i in range(0, linhas):
        for j in range(0, colunas):
            for k in range(0, cor):
                aux = binario.item(i, j)
                if aux != 0:
                    #saida.itemset((i, j), copia.item(i, j))
                    saida.itemset((i,j,k), copia.item(i, j, k))
                else:
                    #saida.itemset((i, j), 0)
                    saida.itemset((i, j, k), 0)


    cv2.imshow('Imagem', saida)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows()
