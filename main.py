from operadores import Operadores

op = Operadores()

binario = op.grayToBinary('10110011')
print(binario)

decimal = op.binarioToDecimal(binario)
print(decimal)

normalizado = decimal / 255
print(normalizado)




