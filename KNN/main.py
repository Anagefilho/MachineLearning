# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:26:46 2019

@author: anage
"""
import numpy as np

def binariza_classe(array): #Passa classe para 0 e 1
    for i in range(len(array)):
        for j in range(9):
            if array[i][j] == "tested_negative":
                array[i][j] = '0'
            elif array[i][j] == "tested_positive":
                array[i][j] = '1'


def pega_menor(ar, coluna): #Pega o menor valor de uma coluna
    y = 0
    menor = float(1000)
    while(y < len(ar)):
        if menor > float(ar[y][coluna]):
            menor = float(ar[y][coluna])
        y+=1
    return menor

def pega_maior(ar, coluna): #Pega maior valor de uma coluna
    y = 0
    maior = float(0)
    while(y < len(ar)):
        if maior < float(ar[y][coluna]):
            maior = float(ar[y][coluna])
        y+=1
    return maior

def min_max(array): #Transforma toda a array em min-max
    x = 0
    coluna = 0
    while(x < 8):
        p = 0
        menor = pega_menor(array, coluna)
        maior = pega_maior(array, coluna)

        while(p < len(array)):
            z = round((float(array[p][coluna]) - menor)/(maior - menor), 5)
            array[p][coluna] = z
            p += 1

        x += 1
        if coluna < 8:
            coluna += 1
        else:
            coluna = 0

def pega_classe_knn(treino,teste, sort): #Pega a classe do numero de menor valor da ordenação
    for i in range(len(teste)):
        for t in range(len(treino)):
           if(sort == round(dist_euclidiana(treino[t], teste[i]),5)):
               return treino[t][8]


def acuracia_e_erros(acertos, erros, k): #Tira a acuracia total
    ac = acertos/(acertos+erros)
    if(k == 1):
        return ac
    else:
        return 1 - ac

def knn(treino, teste, k): #Execução do KNN
    print("Executando o KNN")
    distancia_obj = [] #Cria a lista para receber as distâncias dos objetos
    cont0, cont1, acerto, erro = 0, 0, 0, 0

    for i in range(len(teste)):
        for t in range(len(treino)):
            distancia_obj.append(round(dist_euclidiana(treino[t], teste[i]),5))
        print("Caso de teste sendo analisado: ", i+1)
        dist = np.array(distancia_obj)
        sorted_d = np.sort(dist)
        cont0 = 0
        cont1 = 0
        b = 0
        for z in range(k):
            b = pega_classe_knn(treino, teste, sorted_d[z])
            if b == '0':
               cont0 += 1
               if cont0 > int(k/2):#Pega sempre acima da metade do k.
                   if teste[i][8] == b:
                       acerto +=1
                       #print("Acertou tested_negative")
                       break
                   else:
                       erro += 1
                       #print("Errou tested_positive")
                       break

            else:
               cont1 += 1
               if cont1 > int(k/2):#Pega sempre acima da metade do k.
                   if teste[i][8] == b:
                       acerto +=1
                       #print("Acertou tested_positive")
                       break
                   else:
                       erro += 1
                       #print("Errou tested_negative")
                       break
        distancia_obj.clear() #limpa a lista de objetos

    print("Total de acertos:",acerto)
    print("Total de erros:",erro)

    print("A Acuracia total foi: ", acuracia_e_erros(acerto, erro, 1)*100, "%")
    print("O total de erro foi de: ",acuracia_e_erros(acerto, erro, 2)*100, "%")
    print("Testes classificados:",len(teste))
    print("Quantidade de tuplas de treino: ",len(treino))
       # print(teste[i])
       # print(teste_acuracia)

def dist_euclidiana(treino, teste):
	tamanho, soma = len(treino), 0

	for i in range(tamanho):
    		soma += np.square(float(treino[i]) - float(teste[i]))

	return np.sqrt(soma)


arq = open('Diabetes-data.txt', 'r')
print("Arquivo de dados carregado")
dados = arq.readlines() #Lendo linha por linha do arquivo

x = 0

train_ids = np.loadtxt("train-data.txt").astype(int)  #Carrega os vetores de treino
test_ids = np.loadtxt("test-data.txt").astype(int)    #Carrega os vetores de teste

print("Vetores de dados de teste e treino lidos ")

while x < len(dados): #Pega os dados do arquivo e coloca numa lista.
    if dados[x] == "\n":
        local = dados.index(dados[x])
        dados.pop(local)
    else:
        dados[x] = dados[x].split(',')
        x += 1

for linha in dados: #Tira o \n
    local = dados.index(linha) # Local do i em dados
    for b in linha:
        local2 = dados[local].index(b) # Local2 do b em i ( local )
        if "\n" in b:
            dados[local][local2] = b.replace("\n",'')#Substitui o valor de acordo com "local" e "local2"

x = 0
dados_treino = []
dados_teste = []

while(x < len(train_ids)):
    dados_treino.append(dados[int(train_ids[x])])#Carregando a lista de treino
    x+=1

x = 0

while(x < len(test_ids)):
    dados_teste.append(dados[int(test_ids[x])]) #Carregando a lista de teste
    x+=1


teste = np.array(dados_teste) #Normaliza os dados de teste
treino = np.array(dados_treino) #Normaliza os dados de treino

binariza_classe(treino)
binariza_classe(teste)

min_max(treino)
min_max(teste)

print("Dados de teste e treino foram normalizados com min-max")

k = int(input("Qual o valor do K desejado? "))
knn(treino, teste, k)

print("Concluído")
