#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Altere o tamanho do passo para 1  dia e refaça o gráfico das soluções de Euler. Agora eles acompanham de perto as soluções 
#verdadeiras do sistema? Por que ou por que não?

#Numpy para vetor e matplotlib para plotar funções
import numpy as np
import matplotlib.pyplot as plt

#N é o número de iterações
N = 1000
#T é o tempo total
T = 140
#deltat é o tempo total sobre o número de iterações
deltat = T/N

#definimos vetores com N zeros
s = np.zeros(N) #suscetiveis
r = np.zeros(N) #recuperados
i = np.zeros(N) #infectados
t = np.zeros(N) #tempo em dias

#Valores iniciais de t,s,r,i
s[0] = 1.0
i[0] = 1.27*10**(-6)
r[0] = 0
t[0] = 0

#Parametros b e k
b =1/2
k = 1/3

#Método de Euler. Para j variando de 0 até N-2
for j in range(N-1):
    s[j+1] = s[j]-b*s[j]*i[j]*deltat
    i[j+1] = i[j]+(b*s[j]*i[j]-k*i[j])*deltat
    r[j+1] = r[j]+k*i[j]*deltat
    t[j+1] = t[j]+deltat

#Plotamos o resultado
plt.plot(t,s,label="suscetível")
plt.plot(t,i,label="infectado")
plt.plot(t,r,label="recuperado")
plt.legend()
plt.title("Modelo SIR")


# In[ ]:




