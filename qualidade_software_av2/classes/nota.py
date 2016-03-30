# -*- coding: utf-8 -*-


class Nota(object):
    quantidade = 0

    def __init__(self, valor):
        self.valor = valor

    def adicionar(self, quantidade):
        self.quantidade += quantidade

    def remover(self, quantidade):
        self.quantidade -= quantidade

    def calcular_total(self):
        return self.quantidade * self.valor
