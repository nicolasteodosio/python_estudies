# -*- coding: utf-8 -*-


class Nota(object):

    def __init__(self, valor, quantidade):
        self.valor = valor
        self.quantidade = quantidade

    def multiplica_valor_quantidade(self):
        return self.valor * self.quantidade
