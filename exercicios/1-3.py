# Qual seria o valor acumulado em 7, 8 e 9 anos? E se eu investir R$2.000,
# R$10.000 e R$100.000? Qual a diferença entre poupança e o investimento
# atrelado ao CDI?
# Lembrete:
# - Poupança: rendimento de 0,469% ao mês
# - CDI: retorno de 105% do CDI, que rende 7,5% ao ano
# Sugestão: use funções para cada investimento

def compound_interest(amount, interest_rate, time):
  return amount * (1 + interest_rate) ** time

def calculate_return_poupanca(amount, time_year):
  interest_rate_month = 0.469 / 100
  return compound_interest(amount, interest_rate_month, time_year * 12)

def calculate_return_xp(amount, time_year):
  interest_rate_year = (105 / 100) * (7.5 / 100)
  return compound_interest(amount, interest_rate_year, time_year)

print(calculate_return_poupanca(1000, 7))
print(calculate_return_xp(1000, 7))
print(calculate_return_poupanca(1000, 8))
print(calculate_return_xp(1000, 8))
print(calculate_return_poupanca(1000, 9))
print(calculate_return_xp(1000, 9))
print(calculate_return_poupanca(2000, 9))
print(calculate_return_xp(2000, 9))
print(calculate_return_poupanca(10000, 9))
print(calculate_return_xp(10000, 9))
print(calculate_return_poupanca(100000, 9))
print(calculate_return_xp(100000, 9))
