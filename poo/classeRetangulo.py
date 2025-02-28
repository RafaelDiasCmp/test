class Retangulo:
    def __init__(self, base, altura):
            self.base = base
            self.altura = altura

    #Propriedade base
    @property # @DECORATOR  getter      -- sinalizador para interpretar o código a seguir de uma maneira especial   GETTER
    def base(self):
        return self._base
    
    #setter
    @base.setter
    def base(self, valor):
        if not isinstance(valor, int | float):
             raise TypeError('Valor numérico esperado')
        if valor < 0:
            raise ValueError('Valor positivo esperado')
        self._base = valor
             
    
    def calc_area(self):
        return self.altura * self.base
    
    def exibe(self):
        print(f'Retângulo ({self.base} x {self.altura})')
        print(f'     Área = {self.calc_area()}')


r1 = Retangulo(12, 5)
print('r1: ', end='')
r1.exibe()

r1 = Retangulo(20, 5)
print('r2: ', end='')
r1.exibe()