import numpy as np
import os
import time
os.chdir(os.path.join("Python", "wordblock"))

############################################################################################################
#ESTE CODIGO ACHA TODAS AS COMBINAÇÕES POSSIVEIS, NAO SO A PRIMEIRA, NOTE QUE ESTE PROCESSO É MAIS DEMORADO#
############################################################################################################

n = int(input('Por favor, digite o tamanho da matriz: '))
matriz = np.empty((n,n),dtype='U1')
f = open('listalimpa.txt','r', encoding='utf-8')
resp = open('cartao_resposta.txt','w', encoding='utf-8')

global  n_linhas_listas
global  linhavar
contador = [0]*n
lista  = []
n_linhas_listas = []
linhavar = 0

for i in range(n):
    lista.append([]) #criam-se as variaveis que vao carregar as listas e a variavel que guarda o tamanho de tais listas
    n_linhas_listas.append(0)

def Limpalista(size): #pega a lista geral (um dicionario normal) e separa apenas as palavras com numero n de letras
    f = open('lista0.txt', 'r', encoding='utf-8')
    r = open('listalimpa.txt', 'w', encoding='utf-8')
    for line in f:
        p = f.readline()
        if len(p)-1 == size:
            r.write(f'{p}')

def TxtpraLista(listaselecionada:list,): #Transforma o doc txt feito na função Limpalista numa lista 
    print('TxtpraLista')
    with open('listalimpa.txt', 'r', encoding='utf-8') as f:
        listaselecionada[0] = [line.strip() for line in f if line.strip()]
        n_linhas_listas[0] = len(listaselecionada[0])
        #print(listaselecionada)
        print(n_linhas_listas)
    
def getline(linha:int, pos_lista:int, lista):      #pega um elemento da lista e coloca numa linha da matriz
    #print(f'getline',{linha},{pos_lista})
    if linha == n-1:
        if all((contador[i] == n_linhas_listas[i]) for i in range(n)):
            stop()
    matriz[linha] = list(lista[linha][contador[linha]]) 
    print(f'posições das listas:        {contador}')
    contador[linha] = contador[linha] + 1   
    print(matriz)
    #time.sleep(0.05)
    #print(f'linha da matriz atual: {linha_atual + 1}')
    #print('')
    verifycolumn(matriz,lista, linha)

### SEGUIMOS DAQUI ###

def verifycolumn(matriz,lista:list, linha): #verifica se as colunas podem se tornar palavras
    #print('verifycolumn')
    global linhavar
    columns = []
    #time.sleep(0)
    
    for i in range(n): #tranforma as colunas numa lista onde cada elemento sao as 'palavras' formadas por cada coluna
        column_str = ''.join(str(row[i]) for row in matriz)
        columns.append(column_str)
    print(f'                                {columns}')#deslocado para facilitar a leitura
    
    if all(any(s.startswith(columns[i])for s in lista[linha])for i in range(n)): #verifica se todos os prefixos podem ser o inicio de
        print('Todas as colunas formam possiveis palavras')              #alguma palavra na lista (Difici esse conceito) 
        #print(linha_atual)
        #aqui é necessário fazer outro if verificando se existe uma palavra tal que todas as colunas conseguem formar palavras ao mesmo tempo
        #posso tomar a lista de palavras possiveis e testar apenas estas
        
        if linha != n-1:                                                  
            #print('')
            linha = linha + 1
            linhavar = linha 
            print(f'partindo para a proxima linha ({linha + 1})')
            contador[linha] = 0
            func_palavras_possiveis(columns,lista,linha)
        else:
            with open('cartao_resposta.txt', 'a') as f:
                f.write('\n')
                np.savetxt(f, matriz, fmt='%s', encoding='utf-8')
            

                
    if contador[linha] == n_linhas_listas[linha]:
        for i in range(n-1, -1, -1):
            if contador[i] >= n_linhas_listas[i]:
                matriz[i] = ''
                contador[i] = 0
                print(f'linha {i+1} removida')
                linha = linha - 1
                linhavar = linha
            else:
                contador[linha] = contador[linha] + 1



def func_palavras_possiveis(columns, lista, linha):
    palavras_possiveis = []
    for i in range(n):
        palavras_possiveis_desta_coluna = [s for s in lista[linha-1] if s.startswith(columns[i])]
        for palavra in palavras_possiveis_desta_coluna:
            if palavra not in palavras_possiveis:
                    palavras_possiveis.append(palavra)
    n_linhas_listas[linha] = len(palavras_possiveis)
    lista[linha] = palavras_possiveis
    print(palavras_possiveis)

#### SEGUIMOS AQUI####
def stop():
    print('Finalizado. Matriz no documento de texto "cartao_resposta.txt".')
    print(f'as posições das palavras são: {contador}')
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
    getline(linhavar,contador[linhavar], lista)
