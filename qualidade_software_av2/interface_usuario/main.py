# -*- coding: utf-8 -*-
from qualidade_software_av2.classes import CaixaEletronico, Nota

OPCOES_MENU = {
    1: 'repor',
    2: 'sacar',
    3: 'consultar_saldo',
    4: 'sair',
}


def main():
    while True:
        opcao = mostrar_menu()

        if OPCOES_MENU[opcao] == 'repor':
            caixa = repor_caixa()

        elif OPCOES_MENU[opcao] == 'sacar':
            efetuar_saque(caixa)

        elif OPCOES_MENU[opcao] == 'consultar_saldo':
            print 'Saldo atual: {}'.format(caixa.saldo)

        elif OPCOES_MENU[opcao] == 'sair':
            break

        else:
            print(u"Opção inválida!")
            continue


def efetuar_saque(caixa):
    print("\n---------------------------------------")
    print(u"Caixa Eletrônico - Saque")
    print("---------------------------------------")
    quantia = input("Quantia: ")
    print caixa.sacar(quantia)


def repor_caixa():
    print("\n---------------------------------------")
    print(u"Caixa Eletrônico - Reposição de notas")
    print("---------------------------------------")
    qtdNota5 = input("Informa quantidade de notas de 5 reais: ")
    nota5 = Nota(5, qtdNota5)
    qtdNota10 = input("Informa quantidade de notas de 10 reais: ")
    nota10 = Nota(10, qtdNota10)
    qtdNota20 = input("Informa quantidade de notas de 20 reais: ")
    nota20 = Nota(20, qtdNota20)
    qtdNota50 = input("Informa quantidade de notas de 50 reais: ")
    nota50 = Nota(50, qtdNota50)
    qtdNota100 = input("Informa quantidade de notas de 100 reais: ")
    nota100 = Nota(100, qtdNota100)
    notas = [nota5.multiplica_valor_quantidade(), nota10.multiplica_valor_quantidade(),
             nota20.multiplica_valor_quantidade(), nota50.multiplica_valor_quantidade(),
             nota100.multiplica_valor_quantidade()]
    caixa = CaixaEletronico(sum(notas), 0)
    return caixa


def mostrar_menu():
    print("\n---------------------------------------")
    print(u"Caixa Eletrônico - Menu de Opções")
    print("---------------------------------------")
    print("1- Repor")
    print("2- Sacar")
    print("3- Consultar saldo")
    print("4- Fim")
    opcao = input("Opção: ")
    return opcao
