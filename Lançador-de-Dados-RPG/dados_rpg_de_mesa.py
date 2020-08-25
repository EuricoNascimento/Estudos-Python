"""
Codigo que simula o lançamento de dados em um jogo de rpg de mesa, onde o numero de lados do dado,
quantiadade de dados e modificadores são fornecidos pelo usuario
"""
import random


def dices(sd, rl, md):
    """
    Função que recebe os lados do dado (sd), quantas rolagens deve ser feitas (rl)
     e o modificador a ser somado(md).
    """
    try:
        if int(rl) > 0:
            dc = list(random.randint(1, int(sd) + 1) for x in range(int(rl)))
            print(f'{dc} + {md} = {sum(dc) + int(md)}')
    except ValueError:
        print(f'Dados inseridos incorretamente')


option = 's'
while option != '2':
    option = input('Deseja rolar os dados?\n1-Sim\n2-Não\n')
    if option == '1':
        side = input('Digite o numero de lados do dado: ')
        roll = input('Digite quantas vezes o dado será lançado: ')
        mod = input('Digite o modificador (0 se não tiver): ')
        dices(side, roll, mod)
    elif option != '2':
        print('Opção invalida')
