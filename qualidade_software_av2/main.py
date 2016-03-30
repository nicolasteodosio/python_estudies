# -*- coding: utf-8 -*-
from classes.caixa_eletronico import CaixaEletronico
from classes.saldo import VALORES_NOTAS

OPCOES_MENU = {
    1: 'repor',
    2: 'sacar',
    3: 'consultar_saldo',
    4: 'sair',
}


class Main(object):

    def executar(self):
        caixa = CaixaEletronico()
        while True:
            opcao = mostrar_menu()
            try:
                if OPCOES_MENU[opcao] == 'repor':
                    caixa = repor_caixa(caixa)

                elif OPCOES_MENU[opcao] == 'sacar':
                    efetuar_saque(caixa)

                elif OPCOES_MENU[opcao] == 'consultar_saldo':
                    consultar_saldo(caixa)

                elif OPCOES_MENU[opcao] == 'sair':
                    break

            except KeyError:
                print(u'\n Opção inválida')


def consultar_saldo(caixa):
    print '\nSaldo atual: {}\n'.format(caixa.saldo.retorna_saldo_notas())
    for nota in VALORES_NOTAS:
        print 'Quantidade de notas de {}: {}'.format(nota, caixa.saldo.retorna_quantidade_pelo_valor(nota))


def efetuar_saque(caixa):
    mostrar_cabecalho(msg=u"Caixa Eletrônico - Saque")
    quantia = input("Quantia: ")
    print caixa.sacar(quantia)


def repor_caixa(caixa):

    mostrar_cabecalho(msg=u"Caixa Eletrônico - Reposição de notas")

    qtdnota100 = input("Informa quantidade de notas de 100 reais: ")
    qtdnota50 = input("Informa quantidade de notas de 50 reais: ")
    qtdnota20 = input("Informa quantidade de notas de 20 reais: ")
    qtdnota10 = input("Informa quantidade de notas de 10 reais: ")
    qtdnota5 = input("Informa quantidade de notas de 5 reais: ")

    qtdnotas = [qtdnota100, qtdnota50, qtdnota20, qtdnota10, qtdnota5]

    nota_valor = {}
    for indice, nota in enumerate(caixa.saldo.notas):
        nota_valor[nota.valor] = qtdnotas[indice]

    caixa.depositar(nota_valor)

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


if __name__ == '__main__':
    Main().executar()
