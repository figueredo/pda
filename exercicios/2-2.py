# Considerando o arquivo data.csv:
# A. Leia os dados em um DataFrame e explore-o
# B. Adicione uma nova coluna ratio, sendo a razão entre pontuação e tentativas para cada pessoa.
# C. Imprima as informações das pessoas com o maior e menor ratio.
# D. Ordene decrescentemente pelo ratio.
# E. Salve o novo arquivo CSV.

import pandas as pd

# A. Leia os dados em um DataFrame e explore-o
df = pd.read_csv('./data.csv')

# Possíveis explorações
# Listar colunas: df.columns
# Sumário estatístico: df.describe()
# Listar algumas das primeiras linhas: df.head()
# Plotar histograma:
# df.hist()
# plt.plot() # carregar matplotlib antes

# B. Adicione uma nova coluna ratio, sendo a razão entre pontuação e tentativas para cada pessoa.
df['ratio'] = df.score/df.attempts

# C. Imprima as informações das pessoas com o maior e menor ratio.
max_ratio = df.loc[df.ratio.idxmax()]
min_ratio = df.loc[df.ratio.idxmin()]
print('Maior aproveitamento:')
print(max_ratio)
print('Menor aproveitamento:')
print(min_ratio)

# D. Ordene decrescentemente pelo ratio.
sorted_df = df.sort_values(by='ratio', ascending=False)

# E. Salve o novo arquivo CSV.
sorted_df.to_csv('sorted_data.csv', index=False)