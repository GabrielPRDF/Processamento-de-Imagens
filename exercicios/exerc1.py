#!/usr/bin/python
# Importacao de bibliotecas
import cv2
import numpy as np
def limializacao(img, numero):
	saida = np.zeros(img.shape, np.uint8)
	# Obtem o tamanho da minha_imagem
	linhas, colunas = img.shape
	print('linhas:  ' + str(linhas))
	print('colunas: ' + str(colunas))
	#Converte cada pixel para o seu acontrario 255 - pixel
	for i in range(0, linhas):
		for j in range(0, colunas):
			exc2 = img.item(i, j)
			if(img.item(i, j) < numero):
				exc2 = 0
			if(img.item(i, j) > numero):
				exc2 = 255
			saida.itemset((i, j), exc2)
	return saida
# Abre a imagem
img = cv2.imread('rengar.jpg', cv2.IMREAD_GRAYSCALE)
imglimiar = limializacao(img, 150)
# Exibe a imagem na tela
cv2.imshow('imagem', img)
cv2.imshow('saida', imglimiar)
# Espera alguma tecla
tecla = cv2.waitKey(0)
