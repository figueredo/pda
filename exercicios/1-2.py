# Qual seria o valor acumulado em 7, 8 e 9 anos? E se eu investir R$2.000,
# R$10.000 e R$100.000?
#
# Lembrete: rendimento de 0,469% ao mês
# Sugestão: use variáveis para os valores que mudam

interest_rate_month = 0.469 / 100
amount = 1000

time_year = 7
print(amount * (1 + interest_rate_month) ** (time_year * 12))

time_year = 8
print(amount * (1 + interest_rate_month) ** (time_year * 12))

time_year = 9
print(amount * (1 + interest_rate_month) ** (time_year * 12))

amount = 2000
print(amount * (1 + interest_rate_month) ** (time_year * 12))

amount = 10000
print(amount * (1 + interest_rate_month) ** (time_year * 12))

amount = 100000
print(amount * (1 + interest_rate_month) ** (time_year * 12))
