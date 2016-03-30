# -*- coding: utf-8 -*-
from nota import Nota

VALORES_NOTAS = [100, 50, 20, 10, 5]


class Saldo(object):
    notas = [Nota(valor) for valor in VALORES_NOTAS]

    def retorna_saldo_notas(self):
        return sum([nota.calcular_total() for nota in self.notas])

    def retorna_nota_pelo_valor(self, valor):
        return list(filter(lambda x: x.valor == valor, self.notas))[0]

    def retorna_quantidade_pelo_valor(self, valor):
        nota = self.retorna_nota_pelo_valor(valor)
        return nota.quantidade

    def retorna_notas(self):
        return self.notas

    def adicionar_notas(self, relacao_notas):
        for valor, quantidade in relacao_notas.items():
            nota = self.retorna_nota_pelo_valor(valor)
            nota.adicionar(quantidade)

    def remover_notas(self, relacao_notas):
        for valor, quantidade in relacao_notas.items():
            nota = self.retorna_nota_pelo_valor(valor)
            nota.remover(quantidade)
