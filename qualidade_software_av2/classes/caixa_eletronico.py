# -*- coding: utf-8 -*-
from saldo import Saldo


class CaixaEletronico(object):
    saldo = Saldo()
    qtdsaques = 0

    def depositar(self, relacao_notas):
        self.saldo.adicionar_notas(relacao_notas)

    def sacar(self, valor_saque):
        valor_original = valor_saque
        msg = 'Saque realizado com sucesso'
        if valor_saque > self.saldo.retorna_saldo_notas():
            msg = u"\nQuantia inválida ou saldo insuficiente"

        msg, valor_saque = self.calcular_nota_saque(msg, valor_saque)

        if valor_original != valor_saque:
            self.qtdsaques += 1
        return msg

    def calcular_nota_saque(self, msg, valor_saque):
        for nota in self.saldo.notas:

            if not valor_saque >= nota.valor:
                continue

            quantidade_notas = valor_saque / nota.valor
            quantidade_notas_no_caixa = nota.quantidade

            if quantidade_notas_no_caixa < quantidade_notas:
                quantidade_notas = quantidade_notas_no_caixa
                msg = u"\nNão há cédulas para efetuar o saque, por favor reponha"

            valor_saque -= quantidade_notas * nota.valor
            nota.remover(quantidade_notas)
        return msg, valor_saque

