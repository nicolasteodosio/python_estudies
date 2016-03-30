# -*- coding: utf-8 -*-


class CaixaEletronico(object):

    def __init__(self, saldo, qtdsaques):
        self.saldo = saldo
        self.qtdsaques = qtdsaques

    def sacar(self, valor):
        self.qtdsaques += 1
        self.saldo -= valor

    def add_saldo(self, notas):
        for nota in notas:
            valor = nota.multiplica_valor_quantidade()
            self.saldo += valor

