import numpy as np


def ap(start, diff, count):
  return np.cumsum(np.zeros(count) + diff) + start - diff

def gp(start, ratio, count):
  return (np.cumprod(np.ones(count) * ratio) * start) / ratio

# Usando NumPy, calcule os 10 primeiros elementos e a soma da progressão
# artimética cujo primeiro elemento é 10 e a razão é 3.
progression = ap(10, 3, 10)
print('PA: {0}'.format(', '.join(['{0:.0f}'.format(value) for value in progression])))
print('Soma da PA: {0:.0f}\n'.format(progression.sum()))

# Usando NumPy, calcule os 10 primeiros elementos e a soma da progressão
# geométrica cujo primeiro elemento é 10 e a razão é 3.
progression = gp(10, 3, 10)
print('PG: {0}'.format(', '.join(['{0:.0f}'.format(value) for value in progression])))
print('Soma da PG: {0:.0f}\n'.format(progression.sum()))

# Calcule o rendimento do CDI como nos exercícios anteriores do primeiro
# ao décimo ano usando NumPy.
returns = gp(1000, 1 + (7.5/100) * (105/100), 11)
print('Rendimentos do XP: {0}'.format(', '.join(['R${0:.2f}'.format(value) for value in returns])))