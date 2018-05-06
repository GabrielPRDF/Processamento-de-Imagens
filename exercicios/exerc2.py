#!/usr/bin/python
# Importacao de bibliotecas
import cv2
import numpy as np
def gama(img, g):
	saida = np.zeros(img.shape, np.uint8)
	# Obtem o tamanho da minha_imagem
	linhas, colunas = img.shape
	print('linhas:  ' + str(linhas))
	print('colunas: ' + str(colunas))
	#Converte cada pixel para o seu acontrario 255 - pixel
	for i in range(0, linhas):
		for j in range(0, colunas):
			#aux = n * img.item(i, j) ** g
			aux = 255 * ((img.item(i,j) / 255.0) ** g)
			saida.itemset((i, j), aux)
	return saida
# Abre a imagem
img = cv2.imread('rengar.jpg', cv2.IMREAD_GRAYSCALE)
imglimiar = gama(img, 1.5)
# Exibe a imagem na tela
cv2.imshow('imagem', img)
cv2.imshow('saida', imglimiar)
# Espera alguma tecla
tecla = cv2.waitKey(0)
