import random
from cromossomo import Cromossomo
from operadores import Operadores

class GATC():
    cromossomos = []
    operador = Operadores()

    def __init__(self,tamanhoPopulacaoInicial):
        self.inicializarVariaveis(tamanhoPopulacaoInicial)
        self.ordenarPopulacao()

    def inicializarVariaveis(self,tamanhoPopulacaoInicial):
        self.inicializarPopulacao(tamanhoPopulacaoInicial)

    def inicializarPopulacao(self, tamanhoPopulacaoInicial):
        individuoDefault = '0000000000000000000000000000'
        mascara = self.gerarUmIndividuo()
        lambyda = self.gerarLambyda()

        self.cromossomos.append(Cromossomo(individuoDefault, lambyda, mascara))

        for i in range(0, (tamanhoPopulacaoInicial - 1)):
            individuo = self.gerarUmIndividuo()
            mascara = self.gerarUmIndividuo()
            lambyda = self.gerarLambyda()

            novo = Cromossomo(individuo, lambyda, mascara)
            self.cromossomos.append(novo)

    def imprimirPopulacao(self):
        print("\n\n")
        for i in range(0, len(self.cromossomos)):
            print('Individuo: {} - Size: {} - Acuracia: {}'.format(
                self.cromossomos[i].individuo, self.cromossomos[i].size, self.cromossomos[i].acuracia))

    def ordenarPopulacao(self):
        # Ordena a lista pelo fitness (key = lambda cromossomo: cromossomo.fitness)
        listaOrdenada = sorted(
            self.cromossomos, key=lambda cromossomo: cromossomo.fitness, reverse=True)
        self.cromossomos = listaOrdenada

    def gerarLambyda(self):
        novo = ''

        g1 = random.randint(0, 1)
        g2 = random.randint(0, 1)
        g3 = random.randint(0, 1)
        g4 = random.randint(0, 1)

        novo += str(g1)+str(g2)+str(g3)+str(g4)
        
        return novo
    
    def gerarUmIndividuo(self):
        novo = ''

        criterion = random.randint(0, 1)
        splitter = random.randint(0, 1)

        novo += str(criterion)+str(splitter)

        max_depth_bit1 = random.randint(0, 1)
        max_depth_bit2 = random.randint(0, 1)
        max_depth_bit3 = random.randint(0, 1)
        max_depth_bit4 = random.randint(0, 1)
        max_depth_bit5 = random.randint(0, 1)
        max_depth_bit6 = random.randint(0, 1)

        novo += str(max_depth_bit1) + str(max_depth_bit2) + str(max_depth_bit3) + \
            str(max_depth_bit4) + str(max_depth_bit5) + str(max_depth_bit6)

        min_samples_split_bit1 = random.randint(0, 1)
        min_samples_split_bit2 = random.randint(0, 1)
        min_samples_split_bit3 = random.randint(0, 1)
        min_samples_split_bit4 = random.randint(0, 1)
        min_samples_split_bit5 = random.randint(0, 1)
        min_samples_split_bit6 = random.randint(0, 1)
        min_samples_split_bit7 = random.randint(0, 1)
        min_samples_split_bit8 = random.randint(0, 1)

        novo += str(min_samples_split_bit1) + str(min_samples_split_bit2) + str(min_samples_split_bit3) + str(min_samples_split_bit4) + str(min_samples_split_bit5) + \
            str(min_samples_split_bit6) + \
            str(min_samples_split_bit7) + str(min_samples_split_bit8)

        min_samples_leaf_bit1 = random.randint(0, 1)
        min_samples_leaf_bit2 = random.randint(0, 1)
        min_samples_leaf_bit3 = random.randint(0, 1)
        min_samples_leaf_bit4 = random.randint(0, 1)
        min_samples_leaf_bit5 = random.randint(0, 1)
        min_samples_leaf_bit6 = random.randint(0, 1)
        min_samples_leaf_bit7 = random.randint(0, 1)
        min_samples_leaf_bit8 = random.randint(0, 1)

        novo += str(min_samples_leaf_bit1) + str(min_samples_leaf_bit2) + str(min_samples_leaf_bit3) + str(min_samples_leaf_bit4) + str(min_samples_leaf_bit5) + \
            str(min_samples_leaf_bit6) + \
            str(min_samples_leaf_bit7) + str(min_samples_leaf_bit8)

        min_weight_fraction_leaf_bit1 = random.randint(0, 1)
        min_weight_fraction_leaf_bit2 = random.randint(0, 1)
        min_weight_fraction_leaf_bit3 = random.randint(0, 1)

        novo += str(min_weight_fraction_leaf_bit1) + \
            str(min_weight_fraction_leaf_bit2) + \
            str(min_weight_fraction_leaf_bit3)

        presort = random.randint(0, 1)

        novo += str(presort)

        return novo

    def selecaoPaisRandom(self):
        rand1 = random.randint(0, len(self.cromossomos) - 1)
        rand2 = random.randint(0, len(self.cromossomos) - 1)

        pai1 = self.cromossomos[rand1]
        pai2 = self.cromossomos[rand2]

        return pai1, pai2

    def selecaoPaisElitismo(self):
        pai1 = self.cromossomos[0]
        pai2 = self.cromossomos[1]

        return pai1, pai2

    def cruzamento(self, pai1, pai2):
        mascaraPai1 = pai1.mascara
        lambydaPai1 = pai1.lambyda

        indPai1 = pai1.individuo
        indPai2 = pai2.individuo
        indNovo1 = ''
        indNovo2 = ''
        for i in range(0, len(mascaraPai1)):
            if(mascaraPai1[i] == '1'):
                indNovo1 += indPai1[i]
                indNovo2 += indPai2[i]
            else:
                indNovo1 += indPai2[i]
                indNovo2 += indPai1[i]

        novaMascara = self.operacao(mascaraPai1, lambydaPai1)

        novo1 = Cromossomo(indNovo1,lambydaPai1,novaMascara)
        novo2 = Cromossomo(indNovo2,lambydaPai1,novaMascara)
        return novo1, novo2

    def operacao(self, mascara, lambyda):
        lambBin         = self.operador.grayToBinary(lambyda)
        lambDecimal     = self.operador.binarioToDecimal(lambBin)
        lambNormalizado = lambDecimal * (4/15)
        print("Lamb normalizado: ",lambNormalizado)
        
        novaMascara = ''

        atributo1   = mascara[0]
        atributo2   = mascara[1]

        #-----------------------------------------------------------
        
        atributo3   = mascara[2:8]
        valor3bin   = self.operador.grayToBinary(atributo3)
        valor3dec   = self.operador.binarioToDecimal(valor3bin)
        valor3norm  = valor3dec / 63 
        valorCaotico = self.funcaoCaotica(lambNormalizado,valor3norm)
        valor3dec = int(valorCaotico * 63)

        if(valor3dec > 50):
            valor3bin = '110010'
        else:
            valor3bin = self.operador.decimalToBinary(valor3dec)

        valorBin = valor3bin

        for i in range(0,6-len(valor3bin)):
            valorBin = '0'+valorBin

        valor3gray = self.operador.binaryToGray(valorBin)
        
        #----------------------------------------------------------- 
        atributo4 = mascara[8:16]
        valor4bin   = self.operador.grayToBinary(atributo4)
        valor4dec   = self.operador.binarioToDecimal(valor4bin)
        valor4norm  = valor4dec / 255 
        valorCaotico = self.funcaoCaotica(lambNormalizado,valor4norm)
        valor4dec = int(valorCaotico * 255)

        if(valor4dec < 2):
            valor4bin = '00000010'
        else:
            valor4bin = self.operador.decimalToBinary(valor4dec)

        valorBin = valor4bin
        
        for i in range(0,8-len(valor4bin)):
            valorBin = '0'+valorBin

        valor4gray = self.operador.binaryToGray(valorBin)
        
        #-----------------------------------------------------------
        atributo5 = mascara[16:24]
        valor5bin   = self.operador.grayToBinary(atributo5)
        valor5dec   = self.operador.binarioToDecimal(valor5bin)
        valor5norm  = valor5dec / 255 
        valorCaotico = self.funcaoCaotica(lambNormalizado,valor5norm)
        valor5dec = int(valorCaotico * 255)

        if(valor5dec < 1):
            valor5bin = '00000001'
        else:
            valor5bin = self.operador.decimalToBinary(valor5dec)

        valorBin = valor5bin
        
        for i in range(0,8-len(valor5bin)):
            valorBin = '0'+valorBin

        valor5gray = self.operador.binaryToGray(valorBin)

        #-----------------------------------------------------------
        atributo6 = mascara[24:27]
        valor6bin   = self.operador.grayToBinary(atributo6)
        valor6dec   = self.operador.binarioToDecimal(valor6bin)
        valor6norm  = valor6dec / 7 
        valorCaotico = self.funcaoCaotica(lambNormalizado,valor6norm)
        valor6dec = int(valorCaotico * 7)

        if(valor6dec > 5):
            valor6bin = '101'
        else:
            valor6bin = self.operador.decimalToBinary(valor6dec)

        valorBin = valor6bin
        
        for i in range(0,3-len(valor6bin)):
            valorBin = '0'+valorBin

        valor6gray = self.operador.binaryToGray(valorBin)
       
        #-----------------------------------------------------------
        atributo7 = mascara[27]

        novaMascara = atributo1 + atributo2 + valor3gray + valor4gray + valor5gray + valor6gray + atributo7

        return novaMascara

    def funcaoCaotica(self, lambyda, mascaraValor):
        # zn+1 = λ*zn*(1 − zn)
        return lambyda*mascaraValor * (1-mascaraValor)

    def mutacao(self):
        rand1 = random.randint(0, len(self.cromossomos) - 1)
        rand2 = random.randint(0, len(self.cromossomos[rand1].individuo) - 1)

        ind  = self.cromossomos[rand1].individuo
        masc = self.cromossomos[rand1].mascara
        lamb = self.cromossomos[rand1].lambyda
        if(ind[rand2] == '1'):
            list1 = list(ind)
            list1[rand2] = '0'
            str1 = ''.join(list1)
            ind = str1
        else:
            list1 = list(ind)
            list1[rand2] = '1'
            str1 = ''.join(list1)
            ind = str1

        self.cromossomos.append(Cromossomo(ind,lamb,masc))
        self.ordenarPopulacao()
        self.cromossomos = self.cromossomos[:-1]

    def execucao(self):
        pai1, pai2      = self.selecaoPaisRandom()
        novo1, novo2    = self.cruzamento(pai1,pai2) 

        self.cromossomos.append(novo1)
        self.cromossomos.append(novo2)
        
        self.mutacao()

        self.ordenarPopulacao()
        self.cromossomos = self.cromossomos[:-2]

    ###################################################################33
    # Gets para realizar cruzamento e aplicação da função caótica

    def getCriterion(self, ind):
        return  ind[0]

    def getSplitter(self, ind):
        return ind[1]

    def getMaxDepth(self, ind):
        return 50, ind[2:8]

    def getMinSamplesSplit(self, ind):
        return 255, ind[8:16]
        
    def getMinSamplesLeaf(self, ind):
        return 255, ind[16:24]

    def getMinWeigthFractionLeaf(self, ind):
        return 7, ind[24:27]
        
    def getPresort(self, ind):
        return ind[27]
        