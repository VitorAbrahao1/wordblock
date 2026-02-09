import numpy as np
import os
import time
os.chdir(os.path.join("Python", "wordblock"))

n = int(input('Por favor, digite o tamanho da matriz: '))
matriz = np.empty ((n,n),dtype='U1')

f = open('listalimpa.txt','r', encoding='utf-8')

lista = []
posições = [''] * n
pos_lista_max = 0 #posição maxima da lista
linha_atual = 0
last_line_number = 0
stop = False

def Limpalista(size):
    f = open('lista0.txt', 'r', encoding='utf-8')
    r = open('listalimpa.txt', 'w', encoding='utf-8')
    for line in f:
        p = f.readline()
        if len(p)-1 == size:
            r.write(f'{p}')
    

def TxtpraLista(listaselecionada:list): #Transforma o doc txt numa lista 
    print('TxtpraLista')
    global lista
    global last_line_number
    with open('listalimpa.txt', 'r', encoding='utf-8') as f:
        listaselecionada = [line.strip() for line in f if line.strip()]
        lista = listaselecionada
        last_line_number = len(lista)
    print(f'ultima linha: {last_line_number}')
    return False
    # print(lista)
    # print(lista[100])
    
def getline(linha:int, pos_lista:int):      #pega um elemento da lista e coloca numa coluna da matriz
    #print(f'getline',{linha},{pos_lista})
    global pos_lista_max
    global linha_atual
    global posições
    matriz[linha] = list(lista[pos_lista])
    posições[linha] = int(pos_lista) # type: ignore
    print(matriz)
    #time.sleep(0.05)
    linha_atual = linha_atual + 1
    if pos_lista == pos_lista_max:
        pos_lista_max = pos_lista_max + 1
        print(f'linhas da lista visitadas: {pos_lista_max}')
    print(f'linha da matriz atual: {linha_atual}')
    print('')
    verifycolumn(matriz,lista)

def verifycolumn(matriz,lista): #verifica se a coluna pode ou nao se tornar palavra
    print('verifycolumn')
    columns = []
    global linha_atual
    global pos_lista_max
    global last_line_number
    global stop
    global posições
    looped = 0

    time.sleep(0)
    
    for i in range(n): #tranforma as colunas numa lista onde cada elemento sao as 'palavras' formadas por cada coluna
        column_str = ''.join(str(row[i]) for row in matriz)
        columns.append(column_str)
    print(columns)
    
    if all(any(s.startswith(columns[i])for s in lista)for i in range(n)): #verifica se todos os prefixos podem ser o inicio de
        print('Todas as colunas formam possiveis palavras')              #alguma palavra na lista (Difici esse conceito) 
        print(linha_atual)
        if linha_atual != n:                                               
                print(f'partindo para a proxima linha ({linha_atual+1})')     
                print('')
                pos_lista_max = 0
        else:
                print('Finalizado. Matriz final:')
                print(f'as posições das palavras são: {posições}')
                print(matriz)
                stop = True
                
    else: 
        linha_atual = linha_atual - 1
        print(f'alguma coluna nao pode formar palavras')
        print(f'linha da matriz atual: {linha_atual + 1}')
        print('')
        if pos_lista_max == last_line_number: #verifica se a palavra utilizada é a ultima palavra da lista
            #print('não existem combinações com estas palavras, retomando de 1 linha antes')
            looped = looped + 1
            for i in range(looped):
                matriz[linha_atual] = ''
                linha_atual = linha_atual - 1
                pos_lista_max = int(posições[linha_atual]) + 1                

        try:
            print('tentando getline()...')
            getline(linha_atual,pos_lista_max)
        except:
            pass
        return False


inicio = time.perf_counter()   

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
    if stop == False:
        getline(linha_atual,pos_lista_max)
    if stop == True:
        fim = time.perf_counter()
        print(f"\nTempo de execução: {fim - inicio:.2f} segundos")

        quit()