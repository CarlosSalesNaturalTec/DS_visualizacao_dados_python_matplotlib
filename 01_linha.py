# ===============================================================================
# gráfico de linha (line)
# ===============================================================================

import matplotlib.pyplot as plt

x = [2,3,4]
y = [1,2,3]

plt.title ("Gráfico de Linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x,y)
plt.show()      # exibe o gráfico na tela