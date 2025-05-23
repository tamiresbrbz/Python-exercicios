class Carro:
    def __init__(self, cor='preto', ano=2025):
        self.rodas = 4
        self.volante = 1
        self.bancos = 3
        self.cor = cor
        self.ano = ano
    
    def cordocarro(self):
        print('A cor do carro é ' + self.cor)
    
    def anocarro(self):
        print('O carro é do ano ' + self.ano)

meucarro = Carro('vermelho', '2018')
meucarro.cordocarro()
meucarro.anocarro()