# ==================================================================================================================
# gráfico de dispersão e linha + customizações de layout + salvar gráfico
# ==================================================================================================================

import matplotlib.pyplot as plt

# Dados para montagem do gráfico
x = [1,2,3,4,5]
y = [2,3,2,1,1.5]

# Parâmtros diversos
# Mais detalhes sobre customização de layout: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
grafico_titulo = "Gráfico de Dispersão e Linha"
grafico_eixo_x =  "Eixo X"
grafico_eixo_y =  "Eixo Y"
grafico_legenda = "Meus Pontos"

grafico_arquivo_nome = "grafico"
grafico_arquivo_pdf = grafico_arquivo_nome + ".pdf"
grafico_arquivo_png = grafico_arquivo_nome + ".png"
grafico_arquivo_png_dpi = 300

pontos_simbolo = "."
pontos_cor = "red"
pontos_tamanho = 200

linha_cor = "blue"
linha_estilo ="--"

# Monta o gráfico a partir dos Dados e Parâmetros definidas acima
plt.title (grafico_titulo)
plt.xlabel(grafico_eixo_x)
plt.ylabel(grafico_eixo_y)
plt.scatter(x , y , label = grafico_legenda, color = pontos_cor , marker = pontos_simbolo, s=pontos_tamanho)    #dispersão
plt.plot(x , y ,  color = linha_cor, linestyle = linha_estilo)  #linha
plt.legend()   #exibe legendas

# Salva e exibe o gráfico
plt.savefig(grafico_arquivo_pdf)                                    # Salva o gráfico em formato PDF
plt.savefig(grafico_arquivo_png, dpi=grafico_arquivo_png_dpi)       # Salva o gráfico em formato PNG com 300 dpi de resolução
plt.show()                                                          # exibe o gráfico na tela