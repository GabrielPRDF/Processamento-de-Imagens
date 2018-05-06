#!/usr/bin/python
# Importacao de bibliotecas
import cv2
import numpy as np
def negativo(img):
	saida = np.zeros(img.shape, np.uint8)
	# Obtem o tamanho da minha_imagem
	linhas, colunas = img.shape
	print('linhas:  ' + str(linhas))
	print('colunas: ' + str(colunas))
	#Converte cada pixel para o seu acontrario 255 - pixel
	for i in range(0, linhas):
		for j in range(0, colunas):
			aux = 255 - img.item(i, j)
			saida.itemset((i, j), aux)
	return saida
# Abre a imagem
img = cv2.imread('rengar.jpg', cv2.IMREAD_GRAYSCALE)
imgnegativa = negativo(img)
# Exibe a imagem na tela
cv2.imshow('imagem', img)
cv2.imshow('saida', imgnegativa)
# Espera alguma tecla
tecla = cv2.waitKey(0)
