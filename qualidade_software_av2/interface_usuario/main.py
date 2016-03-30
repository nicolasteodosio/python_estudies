# -*- coding: utf-8 -*-
from qualidade_software_av2.classes import CaixaEletronico, Nota

OPCOES_MENU = {
    1: 'repor',
    2: 'sacar',
    3: 'consultar_saldo',
    4: 'sair',
}

NOTA5_VALOR = 5
NOTA10_VALOR = 10
NOTA20_VALOR = 20
NOTA50_VALOR = 50
NOTA100_VALOR = 100

NOTA5 = Nota(NOTA5_VALOR, 0)
NOTA10 = Nota(NOTA10_VALOR, 0)
NOTA20 = Nota(NOTA20_VALOR, 0)
NOTA50 = Nota(NOTA50_VALOR, 0)
NOTA100 = Nota(NOTA100_VALOR, 0)


NOTAS = []

def main():
    while True:
        opcao = mostrar_menu()

        try:
            if OPCOES_MENU[opcao] == 'repor':
                caixa = repor_caixa()

            elif OPCOES_MENU[opcao] == 'sacar':
                efetuar_saque(caixa)

            elif OPCOES_MENU[opcao] == 'consultar_saldo':
                print '\n Saldo atual: {}'.format(caixa.saldo)

            elif OPCOES_MENU[opcao] == 'sair':
                break

        except KeyError:
            print(u'\n Opção inválida')


def efetuar_saque(caixa):
    mostrar_cabecalho(msg=u"Caixa Eletrônico - Saque")
    quantia = input("Quantia: ")
    if quantia % 100 == 0:
        NOTA100.quantidade -= 1
        caixa.sacar(quantia)
        quantia -= NOTA100_VALOR
    elif quantia % 50 == 0:
        NOTA50.quantidade -= 1
        caixa.sacar(quantia)
        quantia -= NOTA50_VALOR
    elif quantia % 20 == 0:
        NOTA20.quantidade -= 1
        caixa.sacar(quantia)
        quantia -= NOTA20_VALOR
    elif quantia % 10 == 0:
        NOTA10.quantidade -= 1
        caixa.sacar(quantia)
        quantia -= NOTA10_VALOR
    elif quantia % 5 == 0:
        NOTA5.quantidade -= 1
        caixa.sacar(quantia)
        quantia -= NOTA5_VALOR
    if quantia == 0:
        print u'Quantidade de saques: {} \n' \
              u'Novo valor após o saque: {}'.format(caixa.qtdsaques, caixa.saldo)
    else:
        print u"\nQuantidade de células não é múltiplo do valor solicitado"




def repor_caixa():
    
    mostrar_cabecalho(msg=u"Caixa Eletrônico - Reposição de notas")

    qtdnota5 = input("Informa quantidade de notas de 5 reais: ")
    NOTA5.quantidade = qtdnota5
    qtdnota10 = input("Informa quantidade de notas de 10 reais: ")
    NOTA10.quantidade = qtdnota10
    qtdnota20 = input("Informa quantidade de notas de 20 reais: ")
    NOTA20.quantidade = qtdnota20
    qtdnota50 = input("Informa quantidade de notas de 50 reais: ")
    NOTA50.quantidade = qtdnota50
    qtdnota100 = input("Informa quantidade de notas de 100 reais: ")
    NOTA100.quantidade = qtdnota100

    NOTAS = [NOTA5, NOTA10, NOTA20, NOTA50, NOTA100]
    
    caixa = CaixaEletronico(0, qtdsaques=0)

    caixa.add_saldo(NOTAS)

    return caixa


def mostrar_menu():
    mostrar_cabecalho(msg=u"Caixa Eletrônico - Menu de Opções")
    print("1- Repor")
    print("2- Sacar")
    print("3- Consultar saldo")
    print("4- Fim")
    opcao = input("Opção: ")
    return opcao


def mostrar_cabecalho(msg):
    print("\n---------------------------------------")
    print(msg)
    print("---------------------------------------")
