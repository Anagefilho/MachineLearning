# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:02:10 2019

@author: anage
"""
import numpy as np
import csv
from classe import Conjuntos

suporte_min = 0.10 #float(input("Qual o suporte mínimo?"))
conf_min = 0.30 #float(input("Qual a confiança mínima?"))

def suporte(conjunto):
    for p in conjunto:
        for chave,valor in p.dict.items():
            if(valor/int(len(chave)) < suporte_min):
                p.setPoda()
                #print("Podado");
            else:
                p.poda=0
                #print("n podado")
def confianca(conjunto):
    for p in conjunto:
        for key,valor in p.dict.items():
            print("")

def retorna_apv(conjunto):
    lista_aprovado = [];
    for i in conjunto:
        if i.poda == 0: #se a poda é 0 quer dizer que passou no teste do suporte.
            print("Passaram no sup 1:", i.dict)
            for p in i.dict:
                lista_aprovado.append(p)#pegamos e salvamos numa lista auxiliar os valores que foram aprovados
    return lista_aprovado

produtos, list = {
"Arroz":0, "Azeitona":0, "Suco":0, "Abacaxi":0, "Açúcar":0,
"Hambúrguer":0,"Biscoito":0,"Bombom":0,"Café":0,"Caldo":0,
"Cereal":0,"Chocolate":0,"Chá":0,"Coco ralado":0,"Creme de leite":0,
"Geleia":0,"Leite":0,"Fermento":0,"Café":0,"Farinha":0,
"Cerveja":0,"Refrigerante":0,"Vinho":0,"Feijão":0,"Gelatina":0,

"Salame":0,"Licor":0,"Champanhe":0,"Rum":0,"Água":0,
"Ricota":0,"Patê":0,"Queijo":0,"Nata":0,"Presunto":0,
"Linguiça":0,"Mortadela":0,"Bacon":0,"Chester":0,"Gordura vegetal":0,
"Pimentão":0,"Repolho":0,"Ovos":0,"Melancia":0,"Maçã":0,
"Vagem":0,"Uva":0,"Tomate":0,"Espinafre":0,"Cenoura":0,
},[]

dados = np.genfromtxt("teste.csv", delimiter=',', usecols=(1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,30 ,31 ,32 ,33 ,34 ,35 ,36 ,37 ,38 ,39 ,40 ,41 ,42 ,43 ,44 ,45 ,46 ,47 ,48 ,49))
p = dados.sum(axis=0) #pega a soma de cada coluna
#Guardando a frequencia de cada item
j=0
for i in produtos: #Coloca os produtos numa lista de classes do tipo Conjuntos.
    produtos[i]=int(p[j])
    j+=1
for x, y in produtos.items():
    list.append(Conjuntos({x: y}, 0))

suporte(list)#verifica o suporte de C1 e F1, se forem menor que o sup minimo a flag podado é ativada.
lista_aprovado = []
print(list)
lista_aprovado.append(retorna_apv(list))
print(lista_aprovado)
aux, array=[],[]
ic, jc = 0,0
#print(lista_aprovado)
for i in range(len(lista_aprovado)):
    for j in range(len(lista_aprovado)):
        if lista_aprovado[0][ic] is lista_aprovado[0][jc]:
            print("a")
        else:
            aux.append(lista_aprovado[0][ic])
            aux.append(lista_aprovado[0][jc])
            print(lista_aprovado)
            array = np.array(aux)
        jc += 1
    print(array)
    ic += 1
    break
