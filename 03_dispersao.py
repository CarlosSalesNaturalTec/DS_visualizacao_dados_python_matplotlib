# Importa Biblioteca MatplotLib para geração de gráficos
import matplotlib.pyplot as plt

# Dados para formação do gráfico
x = [1,2,3,4,5]
y = [2,3,2,1,1.5]

# Titulos e Legendas
plt.title ("Gráfico de Dispersão")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# monta gráfico de Pontos/Dispersão
plt.scatter(x,y)
# exibe o gráfico na tela
plt.show()          