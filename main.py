from operadores import Operadores
from gatc import GATC

# op = Operadores()

# binario = op.grayToBinary('100101010100010001010')
# print(binario)

# decimal = op.binarioToDecimal(binario)
# print(decimal)

gatc = GATC(100)
gatc.imprimirPopulacao()

for i in (0,50):
    gatc.execucao()

gatc.imprimirPopulacao()



