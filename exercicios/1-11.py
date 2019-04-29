# Altere o novo script para pedir o nome do investimento que o usuário
# desejar plotar e plote apenas este.
#
# Sugestão:
# - Use dicionários para guardar as linhas do CSV

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

  # dict comprehension
  return { line[0]: [float(value) for value in line[1:]] for line in csv }

def plot(label, values):
  xvalues = [year for year in range(2019, 2019 + len(values))]
  plt.plot(xvalues, values, label=label, marker='o')
  plt.title('Rendimentos')
  plt.xlabel('Anos')
  plt.ylabel('R$')
  plt.legend()
  plt.show()

investment = input('Qual investimento exibir? ')
series = load_series('result.csv')
if investment in series:
  plot(investment, series[investment])
else:
  print("Investimento não existe em 'result.csv'")
