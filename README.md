# Implementação realizada para Trabalho de Conclusão de Curso em Ciência da Computação - [UFT](https://ww2.uft.edu.br//)

## Resumo
Alguns algoritmos em aprendizado de máquina são parametrizáveis, ou seja, permitem a configuração de parâmetros de maneira a aumentar o desempenho na tarefa utilizada. Na maioria dos casos, estes parâmetros são encontrados empiricamente pelo desenvolvedor. Outra abordagem é utilizar alguma técnica de otimização para encontrar um conjunto otimizado de parâmetros. Este projeto tem por objetivo a aplicação dos algoritmos evolutivos, Algoritmo Genético (AG), Fluid Genetic Algorithm (FGA) e Genetic Algorithm using Theory of Chaos (GATC) para otimizar a busca de hiperparâmetros em algoritmos de árvores de decisão. Este trabalho apresenta alguns resultados  satisfatórios dentro do conjunto de dados testados, onde o algoritmo Classification and Regression Trees (CART) foi utilizado como algoritmo classificador para os testes. Nestes, as árvores de decisão geradas a partir dos valores padrão dos hiperparâmetros são comparados com os otimizados pela abordagem proposta. Buscou-se otimizar a acurácia e o tamanho final da árvore gerada, o que foram otimizadas com sucesso pelos algoritmos propostos.

## Problema
O problema de configuração automática de hiperparâmetros tem relação com vários campos que excedem a computação, onde todas essas áreas compartilham de um critério de qualidade específico comparando diferentes objetos, tendo como objetivo selecionar o objeto que melhor representa o conjunto de dados. Assim, modelos estatísticos e metodologia de otimização são implementados em ML com foco de selecionar os valores dos hiperparâmetros.   

Uma grande gama dos problemas necessitam de uma configuração dos parâmetros para obtenção de um resultado mais satisfatório, com isso, é consumido muito tempo e em alguns casos é necessário que um especialista estude a base de dados e o algoritmo utilizado, para assim, realizar a melhor configuração possível dos parâmetros do algoritmo.

## Algoritmo Classification and Regression Trees (CART)
O algoritmo CART é uma árvore de decisão, e tem como entrada um objeto ou um conjunto de atributos e como saída uma resposta, essa é dada a partir de uma sequência de testes.

Basicamente uma Árvore de Decisão permite dividir recursivamente um conjunto de dados de treino até que cada divisão forneça uma classificação para a instância.
As Árvores de Decisão consistem em "nós" que formam uma árvore, o que significa que, existe um nó-raiz que não tem ramos de entrada, ao contrário dos restantes nós. Cada nó intermédio específica um teste para o atributo, e cada ramo descendente desse nó corresponde ao valor possível desse atributo. Este conjunto de regras é seguido até ser atingido o nó-terminal ou folha

![image](https://user-images.githubusercontent.com/17303936/156013600-da25f627-c08a-4649-9bb1-d4fdfcf86715.png)

A árvore de decisão resultante a partir do a algoritmo CART sempre é binária, o critério utilizado para calcular a impureza de um nó é o índice Gini, o qual mede a heterogeneidade dos dados.

Optou-se por manipular os seguintes parâmetros do algoritmo CART:

![image](https://user-images.githubusercontent.com/17303936/156027741-ab12e3b9-1849-43be-8ba7-f0217e082649.png)

## Base de dados
### Steel Plates
Esta base de dados contém dados de falhas na produção de placas de aço, sendo 1941 exemplos descritos por 27 atributos e classificados em 7 classes. Esses atributos descrevem as propriedades físicas das placas de aço, como tamanho do defeito, posição da falha, refletância da luz da superfície, tipo de material, etc. Todos os atributos são numéricos.

### Breast Cancer
Nesta base de dados relata-se sobre a ocorrência ou não do câncer de mama, estão incluídos 201 instâncias de uma classe e 85 instâncias de outra classe. As instâncias são descritas por 9 atributos, alguns dos quais são lineares e alguns são nominais.

### Wine
Está base de dados mostram os resultados de uma análise química de vinhos mas derivados de três diferentes cultivares. A análise determinou as quantidades de 13 constituintes encontrados em cada um dos três tipos de vinhos. Foram registadas 178 instancias.

### Iris
Este é talvez o banco de dados mais conhecido encontrado na literatura sobre reconhecimento de padrões. O conjunto de dados contém 3 classes de 50 instâncias cada, onde cada classe se refere a um tipo de planta da íris. 

### Isolet
Este conjunto de dados foi gerado da seguinte forma. 150 voluntários falaram o nome de cada letra do alfabeto duas vezes

### Madelon
Este conjunto de dados contém pontos de dados agrupados em 32 agrupamentos colocados nos vértices de um hipercubo de cinco dimensões e rotulados aleatoriamente com +1 ou -1. As cinco dimensões constituem 5 características informativas, assim, 15 combinações lineares desses recursos foram adicionadas para formar um conjunto de 20 recursos informativos.

## Genetic Algorithm using Theory of Chaos
As principais diferenças do GATC para um AG padrão são, o processo de cruzamento que é aplicado pelo uso da função caótica, e a representação cromossomial que também sofre alteração na nova metodologia, utilizando a função da teoria do caos para conduzir a evolução do algoritmo.

![image](https://user-images.githubusercontent.com/17303936/156026939-8d6cd1a9-5665-43e0-b7f4-c2761d9d99a5.png)

O cromossomo é divido em três partes: a solução do problema representada de forma binária, o valor da λ e a máscara de cruzamento uniforme.

![image](https://user-images.githubusercontent.com/17303936/156027076-cb8a41c9-9d84-4cf1-a728-2ce1dde48073.png)

O algoritmo GATC trabalha com problemas multimodais, sendo assim, a primeira parte do cromossomo compõe a solução do problema. A segunda parte é o valor de λ no intervalo de 0 a 4.  Sua representação binária é a proporção do valor real de acordo com quantidade de bits definidas pelo programador para λ. Os cromossomo podem ser considerados como: convergente, periódico e caótico. Quando λ é menor que 3, o cromossomo é classificado como convergente, ou seja, o cromossomo tende a convergir para valores constantes nos processos de iteração do GATC. Caso o valor seja entre 3 e 3,56, o cromossomo é classificado como periódico, neste caso, o cromossomo tende a se tornar neutro para o algoritmo, ou seja, durante as iterações, seu valor pode convergir ou variar. E, por fim, se λ está entre 3,56 e 4, o cromossomo é caótico, assim, o cromossomo tem um comportamento evolutivo completamente variável durante as iterações.

