# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:29:47 2015

@author: davson
"""
import time
import random
import numpy as np
import matplotlib.pyplot as plt

alist = list
listNumElements = []
listTime = []
    
def drawGraphic():
    a = np.random.rand(10)
    plt.plot(listNumElements, listTime, 'k')
    plt.show()

drawGraphic()

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
       

def executarListas(n):  
    alist = random.sample(range(0,999999), n)
    inicial = time.time()
    bubbleSort(alist)
    final = time.time()
    result = final - inicial
    numElementos = int(len(alist))
    tempo = str(final - inicial)
#   print(len(alist))
    adicionarElementos(len(alist), result)
#    print(alist)
#    print ("%d;%s" %(numElementos, tempo))
    
def adicionarElementos(a, b):
    listNumElements.append(a)
    listTime.append(b)    
    
i = 1
while i <= 100:
    executarListas(i * 5)
    i+=1
    if i == 100:
        drawGraphic()