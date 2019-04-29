# Crie um novo script que lê o arquivo CSV e plota um gráfico com todas as
# linhas (cada linha do CSV, será uma linha no gráfico). Use o nome do
# investimento como legenda.
#
# Dicas:
# - plt.plot() pode ser chamado várias vezes
# - Ver método split() de string
# - Relembre conversão de tipos

import matplotlib.pyplot as plt

def load_csv(filename):
  f = open(filename)
  lines = f.read().splitlines()
  f.close()
  return [line.split(',') for line in lines]

def load_series(filename):
  csv = load_csv(filename)
  # Converter para float todas as colunas exceto a primeira
  # que é o identificador do investimento
  return [[line[0]] + [float(value) for value in line[1:]] for line in csv]

def plot(series):
  for serie in series:
    label = serie[0]
    yvalues = serie[1:]
    xvalues = [year for year in range(2019, 2019 + len(yvalues))]
    plt.plot(xvalues, yvalues, label=label, marker='o')
  plt.title('Rendimentos')
  plt.xlabel('Anos')
  plt.ylabel('R$')
  plt.legend()
  plt.show()

series = load_series('result.csv')
plot(series)
