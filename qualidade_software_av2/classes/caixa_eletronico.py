# -*- coding: utf-8 -*-
from saldo import Saldo


class CaixaEletronico(object):
    saldo = Saldo()
    qtdsaques = 0
    valor_total_saques = 0

    def retorna_valor_total_saques(self):
        return self.valor_total_saques

    def depositar(self, relacao_notas):
        self.saldo.adiciona_notas(relacao_notas)

    def sacar(self, valor_saque):
        valor_original = valor_saque
        msg = 'Saque realizado com sucesso'
        if valor_saque > self.saldo.retorna_saldo():
            msg = u"\nQuantia inválida ou saldo insuficiente"

        for nota in self.saldo.retorna_notas():

            if not valor_saque >= nota.valor:
                continue

            quantidade_notas = valor_saque / nota.valor
            quantidade_notas_no_caixa = nota.quantidade

            if quantidade_notas_no_caixa < quantidade_notas:
                quantidade_notas = quantidade_notas_no_caixa
                msg = u"\nNão há cédulas para efetuar o saque, por favor reponha"

            valor_saque -= quantidade_notas * nota.valor
            nota.remover(quantidade_notas)

        if valor_original != valor_saque:
            self.qtdsaques += 1
            self.valor_total_saques += valor_original
        return msg

