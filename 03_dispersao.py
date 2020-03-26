# ===============================================================================
# gráfico de dispersão (scatterplot)
# ===============================================================================

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,2,1,1.5]

plt.title ("Gráfico de Dispersão")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.scatter(x,y)
plt.show()          # exibe o gráfico na tela