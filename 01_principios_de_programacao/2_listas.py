#definição de lista no python
#<lista>=[]  - criação de uma lista vazia

#criação de uma lista com o valores atribuídos
lista=[10,5,1,1,2,2,3,5,10,2,2,1,3,4,4,6] 
#imprimir uma lista
print(lista)
#imprimir o tamanho da lista
print(len(lista))
#imprimir um elemento específico pelo índice
print(lista[0])
#retornar o index de um elemento dentro de uma lista
print("posição: ",lista.index(6))
index_procurado=lista.index(6) #guardar o index localizado em uma variável
#utilizar essa variável para imprimir o registro
print(lista[index_procurado])
#para acessar o último elemento
print(lista[-1])
#para acessar o penúltimo elemento
print(lista[-2])

mercado=['ações', 'opções', 'futuro', 'dolar', 'ouro', 'criptomoedas']
print (mercado)

#vamos fatiar a lista (slice)
print("print(mercado[0:3])",mercado[0:3])
print("print(mercado[2:5])",mercado[2:5])
print("print(mercado[-4:-1])",mercado[-4:-1])
print("print(mercado[-4:])",mercado[-4:]) #imprimir de -4 até o final da lista
print("print(mercado[3:])",mercado[3:]) #imprimir da posição 3 até o final
print("print(mercado[:4])",mercado[:4]) #imprimir do início até a posição 4

#VERIFICAR SE HÁ ALGUM ELEMENTO DENTRO DE UMA LISTA

print('ouro' in mercado) # retorna True se encontrar ou False caso não encontre
print('ro' in mercado) # essa função não fatia os elementos

print(mercado)
#substituindo valor em uma lista, utilizando o indice
mercado[2]='commodity'
print(mercado)
#substituindo valores em uma lista
mercado[0:2]=['tesouro', 'títulos']
print(mercado)

#adicionando elemento a uma lista com append 

mercado.append('elemento adicionado') #elemento é adicionado ao final da lista
print(mercado)

#contar repetições com count
mercado=mercado*2
print(mercado)
mercado.append('dolar')
print(mercado)
print(mercado.count('dolar'))

# adicionando uma lista a outra lista com extend

lista_compra1=['macarrao', 'arroz', 'feijao', 'batata']
lista_compra2=['beterraba', 'pimetao', 'abobrinha', 'ovo']
print("lista_compra1: ", lista_compra1)
print("lista_compra2: ", lista_compra2)
lista_compra_geral=lista_compra1+lista_compra2
print ("lista_compra_geral (lista_compra1+lista_compra2): ", lista_compra_geral)
# agora utilizando extend
lista_compra1.extend(lista_compra2)
print("lista_compra1.extend(lista_compra2):", lista_compra1)

#para ordenar uma lista usaremos o sort

print("lista",lista)
lista.sort()
print("lista.sort(): ", lista)
print("lista_compra_geral: ", lista_compra_geral)
lista_compra_geral.sort()
print("lista_compra_geral.sort(): ", lista_compra_geral)
lista_compra_geral.append('Leite')
lista_compra_geral.append('Presunto')
print(lista_compra_geral)
lista_compra_geral.sort()
print("lista_compra_geral.sort(): ", lista_compra_geral)
#as letras maiúsculas são colocadas com prioridade na frente das letras minúsculas
#para resolver esse problema, vamos adicionar um parâmetro na função sort()
lista_compra_geral.sort(key=str.casefold)
print("lista_compra_geral.sort(key=str.casefold): ", lista_compra_geral)
lista_compra_geral.reverse()
print("lista_compra_geral.reverse(): ", lista_compra_geral)
lista_compra_geral.append('ovo')
print(lista_compra_geral)
print(lista_compra_geral.count('ovo'))
lista_compra_geral.remove('ovo')

print("lista_compra_geral.remove('ovo') remove o primeiro item que encontrar")
print(lista_compra_geral)
print(lista_compra_geral.count('ovo'))

#vamos inserir um elemento em uma posição desejada
lista1=['a','e','i','o','u']
print(lista1)
print("<lista>.insert(<posicao index>, <valor a ser adicionado>)")
lista1.insert(0, 'A')
print("lista1.insert(0, 'A')")
print(lista1)

#limpando a lista inteira
print(mercado)
mercado.clear()
print("mercado=",mercado)

#--------RESUMO DAS OPERAÇÕES COM LISTA--------#
'''
nome.append(x) Adiciona o elemento x à lista “nome”.
nome.clear() Remove todos os elementos da lista “nome”.
nome.count(x) Conta o número de ocorrências de x na lista “nome”.
nome.extend(y) Insere a lista y no final da lista “nome”.
nome.index(x) Retorna o valor do índice do elemento x da lista “nome”.
nome.insert(pos,x) Insere um elemento x na posição “pos” da lista “nome”.
nome.remove(x) Remove um elemento x da lista “nome”.
nome.reverse( ) Ordena inversamente a lista “nome”.
nome.sort( ) Ordena em ordem crescente ou alfabética a lista “nome”
'''