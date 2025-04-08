import numpy as np
import os

# print("Current directory:", os.getcwd())
# print("Files here:", os.listdir())
# print("Trying to open:", os.path.abspath('lista0.txt'))
os.chdir(os.path.join("Python", "wordblock"))
n = 4 #numero de caracteres

matriz = np.empty ((n,n), dtype="U1")

f = open("lista0.txt", 'r')
l1 = False
l2 = False
l3 = False 
l4 = False
c1 = ''
c2 = ''
c3 = ''
c4 = ''
matriz[:0] = '_'
while True:
    p = f.readline()
    if len(p)-1 == n:
        if l1 == False:    
            matriz[0] = list(p[:-1])
            print(p)
            print(matriz)
            l1 = True
        elif l2 == False:
            matriz[1] = list(p[:-1])
            print(p)
            print(matriz)
            c1 = ''.join(matriz[:,0])
            print(f'{c1}1')
            c2 = ''.join(matriz[:,1])
            c3 = ''.join(matriz[:,2])
            c4 = ''.join(matriz[:,3])
            p = f.readline()
            if len(p)-1 == n:
                print('sucesso')
                if p.startswith(c1):
                    print(f'{p}2')
                    # p = f.readline()
                    # if p.startswith(c2):
                    exit()
            l2 = True
        elif l2 == True:
            quit()