class Operadores():

    def binaryToGray(self, binario):
        gray = ''
        gray += binario[0]
        for i in range(0, len(binario)-1):
            v1 = binario[i]
            v2 = binario[i+1]
            print(v1, ' = ', v2)
            if(v1 == v2):
                gray += '0'
            else:
                gray += '1'

        return gray

    def grayToBinary(self, gray):
        binario = ''
        binario += gray[0]
        for i in range(0, len(gray)-1):
            v1 = binario[i]
            v2 = gray[i+1]
            print(v1, ' = ', v2)
            if(v1 == v2):
                binario += '0'
            else:
                binario += '1'

        return binario

    def binarioToDecimal(self, binario):
        decimal = 0
        expoente = len(binario)
        for i in range(0, len(binario)):
            expoente = expoente - 1
            if(binario[i] == '1'):
                decimal += 2 ** expoente

        return decimal

    def decimalToBinary(self,decimal):
        if decimal == 0:
            return ''
        else:
            return self.decimalToBinary(decimal//2) + str(decimal % 2)
