# ===============================================================================
# gráfico de barras (bar)
# ===============================================================================

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [4,3,2,1,1]

plt.title ("Gráfico de Barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x,y)
plt.show()          # exibe o gráfico na tela