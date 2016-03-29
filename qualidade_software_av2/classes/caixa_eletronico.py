# -*- coding: utf-8 -*-


class CaixaEletronico(object):

    def __init__(self, saldo, qtdsaques):
        self.saldo = saldo
        self.qtdsaques = qtdsaques

    def sacar(self, valor):
        if valor > self.saldo:
            return u'Não é possível retirar esse valor'
        self.qtdsaques += 1
        return u'QUantidade de saques: {} \n' \
               u'Novo valor após o saque: {}'.format(self.qtdsaques, self.saldo - valor)
