# -*- coding: latin-1 -*-
import numpy as np
import cv2
import sys

def trata_imagem(imagem_pura,tipo):
    biscoitos = 0
    # borrar 11 x 11 pixels 
    imagem_blur       = cv2.blur(imagem_pura,(11,11)) 
    # Converte para tons de cinza
    imagem_gray       = cv2.cvtColor(imagem_blur, cv2.COLOR_BGR2GRAY) 
    # limiar adaptativo para imagem binária
    imagem_thresh     = cv2.adaptiveThreshold(imagem_gray,255,1,0,29,0)
    # encontra o contorno das imagens binarias
    imagem_contorno   = imagem_thresh.copy()
    cv2.findContours(imagem_contorno,3,2)
    # Segundo método: Tranformando imagens do espectro RGB para HSV
    imagem_hsv        = cv2.cvtColor(imagem_blur,cv2.COLOR_BGR2HSV)
    # Filtrando a componente das cores (0 a 80)
    imagem_hsv_gray   = cv2.cvtColor(imagem_hsv, cv2.COLOR_BGR2GRAY)
    imagem_hsv_thresh = cv2.inRange(imagem_hsv,np.array((0, 80, 0)), np.array((80, 255, 255)))
    # invertendo as cores para o alimento ficar com valor 1 e fundo valor 0
    cv2.bitwise_not(imagem_hsv_thresh,imagem_hsv_thresh)
    imagem_hsv_blur   = cv2.blur(imagem_hsv_thresh,(3,3))
    # Tipo de imagem que será salva (para acompanhar o tratamento)
    if   tipo == 0:
        depois = imagem_pura
    elif tipo == 1:
        depois = imagem_blur
    elif tipo == 2:
        depois = imagem_gray
    elif tipo == 3:
        depois = imagem_thresh
    elif tipo == 4:
        depois = imagem_contorno
    elif tipo == 5:
        depois = imagem_hsv_gray
    elif tipo == 6:
        depois = imagem_hsv_thresh
    elif tipo == 7:
        depois = imagem_hsv_blur 
    else:
        print 'value error'
    # Encontra circulos na imagem tratada
    circles = cv2.HoughCircles(depois,cv2.cv.CV_HOUGH_GRADIENT,2,80,param1=50,param2=35,minRadius=45,maxRadius=55)
    if circles is not None: # Se forem encontrados circulos na imagem:
        for i in circles[0,:]: # Loop que passa por todos os circulos encontrados
            # Desenha os circulos nos objetos encontrados
            cv2.circle(imagem_pura,(i[0],i[1]),i[2],(255,0,0),5)
            cv2.circle(depois,(i[0],i[1]),i[2],(255,0,0),5)
            biscoitos = biscoitos + 1
    # Descomentar linhas abaixo para mostrar resultado
    #cv2.imshow('resultado',depois)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.imwrite('resultado.jpeg',depois)
    return biscoitos

if len(sys.argv)>1:
    imagem_nome = sys.argv[1]
    print '>1'
else:
    imagem_nome = 'antes.png'
    print '<=1'

imagem = cv2.imread(imagem_nome)   # Abre o arquivo com a imagem
if imagem == None:
    print 'erro ao abrir o arquivo'
else:
    biscoitos = trata_imagem(imagem,6) # chama a funcao de reconhecimento
    print 'imagem tratada,', biscoitos, 'biscoitos' 


















