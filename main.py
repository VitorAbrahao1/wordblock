import numpy as np
import os
import time
os.chdir(os.path.join("Python", "wordblock"))

n = int(input('Por favor, digite o tamanho da matriz: '))
matriz = np.empty((n,n),dtype='U1')
f = open('listalimpa.txt','r', encoding='utf-8')

global linha_atual
global  n_linhas_listas

linha_atual = 0
contador = [0]*n
lista  = []
n_linhas_listas = []
for i in range(n):
    lista.append([]) #criam-se as variaveis que vao carregar as listas e a variavel que guarda o tamanho de tais listas
    n_linhas_listas.append([])

def Limpalista(size): #pega a lista geral (um dicionario normal) e separa apenas as palavras com numero n de letras
    f = open('lista1.txt', 'r', encoding='utf-8')
    r = open('listalimpa.txt', 'w', encoding='utf-8')
    for line in f:
        p = f.readline()
        if len(p)-1 == size:
            r.write(f'{p}')

def TxtpraLista(listaselecionada:list): #Transforma o doc txt feito na função Limpalista numa lista 
    print('TxtpraLista')
    global n_linhas_listas
    with open('listalimpa.txt', 'r', encoding='utf-8') as f:
        for i in range(n):
            if linha_atual == i:
                listaselecionada[i] = [line.strip() for line in f if line.strip()]
                n_linhas_listas[i] = len(listaselecionada[i])
                #print(listaselecionada)
                print(n_linhas_listas)
    
def getline(linha:int, pos_lista:int, lista, list_max_size):      #pega um elemento da lista e coloca numa linha da matriz
    #print(f'getline',{linha},{pos_lista})
    global linha_atual
    matriz[linha] = list(lista[linha_atual][contador[linha]]) 
    contador[linha] = contador[linha] + 1
    print(f'posições das listas:        {contador}')    #print(matriz)
    #time.sleep(0.05)
    #print(f'linha da matriz atual: {linha_atual + 1}')
    #print('')
    verifycolumn(matriz,lista,n_linhas_listas[linha])

### SEGUIMOS DAQUI ###

def verifycolumn(matriz,lista:list, list_max_size): #verifica se as colunas podem se tornar palavras
    #print('verifycolumn')
    columns = []
    global linha_atual    
    #time.sleep(0)
    
    for i in range(n): #tranforma as colunas numa lista onde cada elemento sao as 'palavras' formadas por cada coluna
        column_str = ''.join(str(row[i]) for row in matriz)
        columns.append(column_str)
    print(f'                                {columns}')#deslocado para facilitar a leitura
    
    if all(any(s.startswith(columns[i])for s in lista[linha_atual])for i in range(n)): #verifica se todos os prefixos podem ser o inicio de
        #print('Todas as colunas formam possiveis palavras')              #alguma palavra na lista (Difici esse conceito) 
        #print(linha_atual)
        #aqui é necessário fazer outro if verificando se existe uma palavra tal que todas as colunas conseguem formar palavras ao mesmo tempo
        #posso tomar a lista de palavras possiveis e testar apenas estas
        
        if linha_atual != n-1:                                                  
            #print('')
            linha_atual = linha_atual + 1
            #print(f'partindo para a proxima linha ({linha_atual+1})')
            func_palavras_possiveis(columns,lista)
        else:
            stop(matriz)
                
    else: 
        if contador[linha_atual] == list_max_size:
            #print(f'nenhuma palavra da lista pequena obedece os requisitos, voltando para a uma lista atras')
            #print('')
            matriz[linha_atual] = ''
            contador[linha_atual] = 0
            #print('tentando getline()...')
            linha_atual = linha_atual - 1
        else:
            #print('tentando novamente na lista pequena')
            pass

def func_palavras_possiveis(columns, lista):
    global linha_atual

    palavras_possiveis = []
    for i in range(n):
        palavras_possiveis_desta_coluna = [s for s in lista[linha_atual-1] if s.startswith(columns[i])]
        for palavra in palavras_possiveis_desta_coluna:
            if palavra not in palavras_possiveis:
                    palavras_possiveis.append(palavra)
    n_linhas_listas[linha_atual] = len(palavras_possiveis)
    lista[linha_atual] = palavras_possiveis
    #print(palavras_possiveis)

#### SEGUIMOS AQUI####
def stop(matriz):
    print('Finalizado.')
    print(f'as posições das palavras são: {contador}')
    print('Matriz final:')
    print(matriz)
    fim = time.perf_counter()
    print(f"\nTempo de execução: {fim - inicio:.2f} segundos")
    quit()



inicio = time.perf_counter()
print(lista)
#print(matriz)
Limpalista(n)

TxtpraLista(lista)

# print('')
# print('começando em 3 segundos...')
# time.sleep(1)
# print('começando em 2 segundos...')
# time.sleep(1)
# print('começando em 1 segundo...')
# time.sleep(1)
# print('')
while True:
    getline(linha_atual,contador[linha_atual], lista,n_linhas_listas[linha_atual])
