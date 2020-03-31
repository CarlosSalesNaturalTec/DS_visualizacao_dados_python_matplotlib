# Importa Biblioteca MatplotLib para geração de gráficos
import matplotlib.pyplot as plt

# Dados para formação do gráfico
x = [2,3,4]
y = [1,2,3]

# Titulos e Legendas
plt.title ("Gráfico de Linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# monta gráfico de Linha
plt.plot(x,y)
# exibe o gráfico na tela
plt.show()      