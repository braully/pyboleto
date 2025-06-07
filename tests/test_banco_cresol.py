# -*- coding: utf-8 -*-
import unittest
import datetime

from pyboleto.bank.cresol import BoletoCresol
from tests.testutils import BoletoTestCase


class TestBancoCresol(BoletoTestCase):
    def setUp(self):
        self.dados = []
        for i in range(3):
            d = BoletoCresol()
            d.carteira = '09'
            d.agencia_cedente = '1000-0'
            d.conta_cedente = '10000-8'
            d.data_vencimento = datetime.date(2025, 6, 17)
            d.data_documento = datetime.date(2025, 5, 26)
            d.data_processamento = datetime.date(2025, 5, 26)
            d.valor_documento = 145.00
            d.nosso_numero = str(100409 + i)
            d.numero_documento = str(626012431 + i)
            self.dados.append(d)

    def test_linha_digitavel(self):
        print(self.dados[0].linha_digitavel)


suite = unittest.TestLoader().loadTestsFromTestCase(BoletoCresol)


if __name__ == '__main__':
    unittest.main()
