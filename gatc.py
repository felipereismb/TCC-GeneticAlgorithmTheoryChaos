import random
from cromossomo import Cromossomo

class GATC():
    cromossomos = []

    def __init__(self,tamanhoPopulacaoInicial):
        self.inicializarVariaveis(tamanhoPopulacaoInicial)

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
        