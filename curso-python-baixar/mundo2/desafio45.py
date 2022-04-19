from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('''Suas opções
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep (1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 12)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if pc == 0: #pc jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print ('JOGADA INVÁLIDA!')
elif pc == 1: #pc jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
        
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2: #pc jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
