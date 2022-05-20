class Calculadora:
    def __init__(self, num1, num2):
        self.Valor_a = num1
        self.Valor_b = num2
    def soma(self):
        return self.Valor_a + self.Valor_b

    def subtracao(self):
        return self.Valor_a - self.Valor_b

    def divisao(self):
        return self.Valor_a / self.Valor_b

    def multiplica(self):
        return self.Valor_a * self.Valor_b

calculadora = Calculadora(10,2)
print('Valor de A'.format(calculadora.Valor_a))
print('Valor de B'.format(calculadora.Valor_b))

print(calculadora.soma())
print(calculadora.divisao())
print(calculadora.multiplica())
print(calculadora.subtracao())

