# Importa Biblioteca MatplotLib para geração de gráficos
import matplotlib.pyplot as plt

# Dados para formação do gráfico
x = [1,2,3,4,5]
y = [4,3,2,1,1]

# Titulos e Legendas
plt.title ("Gráfico de Barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# monta gráfico de Barras
plt.bar(x,y)
# exibe o gráfico na tela
plt.show()          