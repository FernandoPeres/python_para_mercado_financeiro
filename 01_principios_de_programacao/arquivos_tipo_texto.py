# -*- coding=utf8 -*-
'''
Usaremos o método open() para ler, criar e editar arquivos
    Parâmetros utilizados:
    r - Leitura
    w - Escrita. Substitui o conteúdo do arquivo existente
    x - Escrita. Retorna um erro caso o arquivo já exista
    a - Escrita. Insere os novos dados no final do arquivo
    b - Modo binário
    t - Modo texto (padrão)
    + - Atualizar. Tanto leitura quanto escrita

'''
# EXEMPLO 01
'''
arquivo = open("contatos.txt", "a") #caso não exista ele criará o arquivo contatos.txt
arquivo.write("Olá, mundo!\n") # sempre que for chamado, este método adicionará o texto
lendo = open("contatos.txt", "r") # lendo recebe a leitura do arquivo
linhas=lendo.readlines() #linhas recebe o arquivo lido e separa em linhas
print(len(linhas))
print(linhas)
for linha in linhas: # um for percorrendo e imprimindo todas as linhas lidas
    print (linha)

'''
arquivo1 = open("texto.txt", "a")
frases=list()
frases.append("Treinamento \n")
frases.append("Python \n")
frases.append("Leitura \n")
frases.append("Arquivos \n")
arquivo1.writelines(frases)
arquivo_lido = open("texto.txt", "r")
linhas=arquivo_lido.readlines()
print(linhas)
arquivo1.close()