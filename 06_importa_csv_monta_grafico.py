# Importa Biblioteca MatplotLib para geração de gráficos
import matplotlib.pyplot as plt

# abre arquivo csv e coloca seu conteúdo em uma váriavel
dados = open("arquivos/populacao.csv").readlines()

# inicializa variáveis/matrizes que receberão dados
x = []
y = []

# iteração em todo o arquivo, uma linha por vez
for i in range(len(dados)):
    if i !=0:                       #desconsidera linha 0 (cabeçalho)
        linha = dados[i].split(";") #define separador de colunas ";"
        x.append(int(linha[0]))     #adiciona na matriz X, o valor contido na coluna 0
        y.append(int(linha[1]))     #adiciona na matriz Y, o valor contido na coluna 1

# Título e legendas
plt.title("Crescimento populacional Brasileiro no período de 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x 100.000.000")

# Plota dados
plt.bar(x, y, color="#e4e4e4" )             #grafico de barras
plt.plot(x, y, color="k", linestyle="--")   #gráfico de linha

# Exibe o gráfico
plt.show()