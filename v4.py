import numpy as np
import os
import time

os.chdir(os.path.join("Python", "wordblock"))
n = 4
matriz = np.empty ((n,n),dtype='U1')

f = open('listalimpa.txt','r', encoding='utf-8')

lista = []
pos_lista_max = 0 #posição maxima da lista
linha_atual = 0

def TxtpraLista(listaselecionada:list): #Transforma o doc txt numa lista 
    global lista
    with open('listalimpa.txt', 'r', encoding='utf-8') as f:
        listaselecionada = [line.strip() for line in f if line.strip()]
        lista = listaselecionada
    # print(lista)
    # print(lista[100])
    
def getline(linha:int, pos_lista:int):      #pega um elemento da lista e coloca numa coluna da matriz
    print('getline')
    matriz[linha] = list(lista[pos_lista])
    print(matriz)
    global pos_lista_max
    global linha_atual
    linha_atual = linha_atual + 1
    if pos_lista == pos_lista_max:
        pos_lista_max = pos_lista_max + 1
        print(f'linhas da lista visitadas: {pos_lista_max}')
    # if pos_lista == 902: #tentando solucionar o erro (nao deu certo)
    #     pos_lista_max = 0
    print(f'linha da matriz atual: {linha_atual}')
    print('')
    verifycolumn(matriz,lista)

def verifycolumn(matriz,lista): #verifica se a coluna pode ou nao se tornar palavra
    print('verifycolumn')
    columns = []
    global linha_atual
    global pos_lista_max
    time.sleep(0)
    
    for i in range(4): #tranforma as colunas numa lista onde cada elemento sao as 'palavras' formadas por cada coluna
        column_str = ''.join(str(row[i]) for row in matriz)
        columns.append(column_str)
    print(columns)
    
    if all(any(s.startswith(columns[i])for s in lista)for i in range(4)): #verifies if all of the prefixes are the starting 
        print('Todas as colunas formam possiveis palavras')               #strings of any of the strings inside a list
        if all(any(row.startswith(columns[i])for row in lista) for i in range(4)):
            if linha_atual != 4:                                               #(ta escrito em ingles pq eu nao quis traduzir oq
                print(f'partindo para a proxima linha ({linha_atual+1})')     #eu tava falando pro deepseek); Difici esse conceito
                print('')
                pos_lista_max = 0
                #getline(linha_atual,pos_lista_max)
            else:
                print(matriz)
                quit()
            return True
        else: 
            linha_atual = linha_atual - 1
            print(f'alguma coluna nao pode formar palavra')
            print(f'linha da matriz atual: {linha_atual + 1}')
            print('')
            try:
                print('trying to getline()')
                getline(linha_atual,pos_lista_max)
            except:
                pass
            return False

    else: 
        linha_atual = linha_atual - 1
        print(f'alguma coluna nao pode formar palavra')
        print(f'linha da matriz atual: {linha_atual + 1}')
        print('')
        try:
            print('trying to getline()')
            getline(linha_atual,pos_lista_max)
        except:
            pass
        return False


TxtpraLista(lista)

print('')
getline(linha_atual,pos_lista_max)
getline(linha_atual,pos_lista_max)
getline(linha_atual,pos_lista_max)
getline(linha_atual,pos_lista_max)
getline(linha_atual,pos_lista_max)
# #getlineOnce(linha_atual, pos_lista_max)
# verifycolumn(matriz, lista)


