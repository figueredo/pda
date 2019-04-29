# Altere o script para imprimir uma mensagem ao usuário dizendo o valor
# acumulado em 10 anos para a poupança?
# Lembrete:
# Poupança: rendimento de 0,469% ao mês
# Sugestão: use formatação de strings para gerar a mensagem

def compound_interest(amount, interest_rate, time):
  return amount * (1 + interest_rate) ** time

def calculate_return_poupanca(amount, time_year):
  interest_rate_month = 0.469 / 100
  return compound_interest(amount, interest_rate_month, time_year * 12)

def calculate_return_xp(amount, time_year):
  interest_rate_year = (105 / 100) * (7.5 / 100)
  return compound_interest(amount, interest_rate_year, time_year)

def print_result(roi):
  result_template = 'O retorno da poupança em 10 anos para um investimento de R$1000 é R${roi:.2f}'
  result = result_template.format(roi=roi)
  print(result)

roi = calculate_return_poupanca(1000, 10)
print_result(roi)
