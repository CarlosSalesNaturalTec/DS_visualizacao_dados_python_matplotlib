# Importa Bibliotecas 
import matplotlib.pyplot as plt     #MatplotLib para geração de gráficos
import random                       #Random para sorteio de números aleatórios/randômicos

# inicializa variável/matriz que receberá os dados
vetor = []

# loop para geração de vários números aleatórios
for i in range(100):
    sorteio = random.randint(0,50)   #sorteia um número
    vetor.append(sorteio)           #adiciona na matriz X, o valor contido na coluna 0

# Titulos e Legendas
plt.title("BoxPlot - Diagrama de Caixa")

# Plota dados
plt.boxplot(vetor)

# Exibe o gráfico
plt.show()
