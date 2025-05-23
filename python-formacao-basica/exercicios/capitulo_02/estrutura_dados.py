lVazia = [] #aqui cria-se uma lista vazia
print(lVazia)

lNumeros = [1, 2, 3]
print(lNumeros)

valor = True
lDados = [77, 'ovo', valor, lNumeros] #lista mista com varios tipos de dados
print(lDados)

print (len(lDados)) #conta a quantidade de dados da lista

lDados.append(965) #acrescenta um ítem à lista
print(lDados)

print (len(lDados)) #conta novamente a quantidade de dados da lista

tupla = (2, 3, 4) #parece com a lista mas não aceita acrescimo de dados, nem deletar dados, ela não pode
print( tupla)     #ser modificada dps de criada, é útil para aumentar o processamento do pc, pois ele vai saber exatamente a memória utilizada

conjunto_num = {1, 2, 3, 1, 2}#set --> os elementos não se repetem
print(conjunto_num) #os números repetidos não aparecem
print(len(conjunto_num))

dicionario = {'gato': 'felino domesticado', 'banana': 'fruta amarela', 
              'legenda':'829', 'cidade': 'San Andreas', 'residente': True}
print(dicionario['gato'])
print(dicionario['banana'],'\n',dicionario['cidade']) #o dicionario armazena informações em variaveis

A = []
A.append(12) #acrescenta o número ao final da lista
A.append(11)
A.append(90)
print(A)

print(A[1])
del A[1] #remove o número de indice 1 da lista
print(A)
A[0] = 999 #modifica o primeiro valor da lista
print (A)

#Recurso do fatiamento
Origem = [36, 25, 21, 48, 17, 38, 43, 62, 89, 10]
Destino1 = Origem[3:6] #primeiro parametro é o indice de inicio
print(Destino1)        #o segundo paramentro é o indice de final, começa na posição 3 e termina na 5

Destino2 = Origem[1:7:2] #o terceiro parametro é o passo, indice: 1-3-5 
print(Destino2)

Destino3 = Origem[:4] #o fatiamento parte da posição 0
print(Destino3) #4 primeiros elementos da lista

Destino4 = Origem[6:] #a partir da posição 6, até o fim da lista
print(Destino4)

A = [10, 12, 14, 16]
B = A #B aponta para o mesmo de id de A, ambos apontam para o mesmo lugar da memória
print(id(A))
print(id(B))
B = A[:] #usamos o fatiamento para copiar a lista inteira
print(B)
print(id(A))
print(id(B))
B[0] = 89
print(A)
print(B)

A.clear() #limpa a lista
print(A)

B = A.copy () #produz uma lista nova, copia a lisat com novo id
print(id(A))
print(id(B))

A = [10, 12, 14, 16]
n = A.count (10) #conta quantas occorencias de um valor existem dentro da lista
print(n)

B = [1, 2, 3, 4, 10]
A.extend(B) #extende a lista A, acrescentando a ela todos os elementos de B
print(A)

print(A.index(10)) #retorna a posição do item mensionado
print(A.index(10, 1)) #retorna a posição do 10 a partir do indice 1

A.insert(5, 568) #coloca na posição 5 o valor 568
print(A)

A.insert(0, 58) #coloca na posição 0 o valor 58
print(A)

print(len(A))

R = A.pop(0) #remove o elemento da posição 0 da lista e carrega R com o elemento
print(A)
print(R)

R = A.pop(-1) #remove o ultimo elemento da lista e carrega R com o elemento
print(A)
print(R)

A.remove(12) #remove todos os valores 12 da lista
print(A)

A.reverse() #inverte a lista, o ultimo se torna o primeiro
print(A)

A.sort() #classifica a lista, a torna ordenada de forma crescente
print(A)

A.sort(reverse=True) #classifica a lista, a torna ordenada de forma decrescente
print(A)

L = [21, 45, 17, 28]
for valor in L: #aceita todos os objetos compostos, executa 1 vez para cada item
    print(valor) #'valor' a cada repetição recebe um item da lista
    valor = 0 #alterar o objeto de controle não altera a lista
    print(valor)
print(L)
print('Fim do Programa')

L = [23, 12, 54, 43, 54]
pos = 0
for valor in L:
    print(f'A posição {pos} da lista L, contém {valor}')
    pos += 1
print('Fim do Programa')

