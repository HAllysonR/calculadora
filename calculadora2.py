class Calculadora:
    def soma(self, valor_a, valor_b):
         return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def divisao(self, valor_a, valor_b):
         return valor_a / valor_b

    def multiplica(self, valor_a, valor_b):
        return valor_a * valor_b

calculadora = Calculadora()

print(calculadora.soma(10,2))
print(calculadora.divisao(10,2))
print(calculadora.multiplica(10,2))
print(calculadora.subtracao(10,2))

