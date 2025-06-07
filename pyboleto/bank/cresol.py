# -*- coding: utf-8 -*-
from pyboleto.data import BoletoData, custom_property


# Referencias: 
# - BoletoBradesco
# - https://pt.scribd.com/document/612682075/especificacoes-tecnicas
# - https://s3.amazonaws.com/site321-prod/documents/files/1b8a6952d02d7aa03ebf389b5599ee38d72955a8/original.pdf?1539624253

class BoletoCresol(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o Banco Cresol
    '''
    agencia_cedente = custom_property('agencia_cedente', 4)
    conta_cedente = custom_property('conta_cedente', 7)
    convenio = custom_property('convenio', 4)
    # Nosso numero sem digito verificador
    carteira = custom_property('carteira', 2)
    nosso_numero = custom_property('nosso_numero', 11)
    #nosso_numero_dv = custom_property('nosso_numero_dv', 1)

    def __init__(self):
        super(BoletoCresol, self).__init__()
        self.codigo_banco = "133"
        self.logo_image = "logo_cresol.jpg"


    def format_nosso_numero(self):            
        # 09/00000100409-6
        # Carteira / Nosso Número - DV do Nosso Número
        nosso_numero_formado = f"{self.carteira:02d}/{self.nosso_numero}-{self.dv_nosso_numero}"
        return nosso_numero_formado


    @property
    def dv_nosso_numero(self):
        resto2 = self.modulo11(self.nosso_numero, 7, 1)
        digito = 11 - resto2
        if digito == 10:
            dv = 'P'
        elif digito == 11:
            dv = 0
        else:
            dv = digito
        return dv

    @property
    def campo_livre(self):
        campo_livre_formatado = f'{self.agencia_cedente.split("-")[0]}' \
                                f'{self.carteira}' \
                                f'{self.nosso_numero}' \
                                f'{self.conta_cedente.split("-")[0]}' \
                                '0'
        return campo_livre_formatado
