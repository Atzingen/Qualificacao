# -*- coding: latin-1 -*-
'''  Temperatura 1d - Função conhecida - método SOR  
Cálculo do tempo de execução
'''  
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

for p in range(1,21):
	tic = time.time()
	######################## Condições do problema #######################
	L0 = 0
	Lf = 1
	n  = 100
	deltax  = (Lf - L0)/n
	deltax2 = (Lf - L0)/(n+1)  # verificar n+1
	x       = np.linspace(L0,Lf,n)
	f       = 100*np.exp(x)
	T0      = 20
	Tf      = 60
	u = (100*np.exp(1) - 60)*x + 120 - 100*np.exp(x)  # Solução analítica
	k = 1.9                                           # Overelaxação
	######################################################################
	J = T0 + (Tf-T0)*x      # Temperatura inicial linear
	J2 = J
	erro = 1000
	for l in range(1,3000):
		for i in range(1,n-1):
			Jn = ( J[i-1] + J[i+1] + deltax*deltax*f[i])/2
			J[i] = J[i] + k*( Jn - J[i] )	
	toc = time.time()
	print toc - tic
#plt.plot(J)
#pylab.show()