import os

Continuar = 1

while(Continuar):

 diretorio = input("Digite o nome do diretorio q deseja criar")
 diretorio = '/'+diretorio+'/'

 personagem = input("Digite o nome do baralho para pegar as cartas")
 file = open(personagem,'r')


 for number in file:
  os.link(number,diretorio+number)
  os.remove(number)

 Continuar = int(input("Deseja Continuar? 1 / 0"))
