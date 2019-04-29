# Altere o script para ao invés de imprimir o resultado na tela, salvar em um
# arquivo no formato CSV (comma separated values).
# Cada linha deverá conter o nome do investimento como primeiro elemento,
# seguido dos resultados para cada ano.
#
# CSV:
# - Tabela
# - Cada do arquivo representa uma linha da tabela
# - Colunas são delimitadas por “,”.
# Exemplo de CSV com duas linhas e quatro colunas:
# 1,2,3,4
# 1,2,4,5
#
# Dicas:
# Ver método join() de string
# Representação de nova linha em string é “\n”. Ex.:
# 'Primeira linha\nSegunda linha’

def compound_interest(amount, interest_rate, time):
  return amount * (1 + interest_rate) ** time

def calculate_return_poupanca(amount, time_year):
  interest_rate_month = 0.469 / 100
  return compound_interest(amount, interest_rate_month, time_year * 12)

def calculate_return_xp(amount, time_year):
  interest_rate_year = (105 / 100) * (7.5 / 100)
  return compound_interest(amount, interest_rate_year, time_year)

def calculate_all_return_poupanca(amount, time_year):
  return [calculate_return_poupanca(amount, year) for year in range(time_year + 1)]

def calculate_all_return_xp(amount, time_year):
  return [calculate_return_xp(amount, year) for year in range(time_year + 1)]

def calculate_all_investment_returns(amount, time_year):
  roi_poupanca = calculate_all_return_poupanca(amount, time_year)
  roi_xp = calculate_all_return_xp(amount, time_year)
  return [['POUP'] + roi_poupanca, ['XP'] + roi_xp]

def ask_name():
  name = None
  while name is None or name.isnumeric():
    name = input('Qual é o seu nome? ')
  return name

def ask_amount():
  amount = None
  while amount is None or not amount.isnumeric():
    amount = input('Quanto deseja investir? R$')
  return float(amount)

def ask_time_year():
  time_year = None
  while time_year is None or not time_year.isnumeric():
    time_year = input('Em quantos _anos_ deseja resgatar seu dinheiro? ')
  return int(time_year)

def to_formatted_list(float_list):
  element_template = '{0:.2f}'
  return [element_template.format(element) for element in float_list]

def to_csv_str(values):
  return ','.join(values)

def to_csv(results):
  lines = ['{name},{values}\n'.format(
    name=result[0],
    values=to_csv_str(to_formatted_list(result[1:]))
  ) for result in results]
  return ''.join(lines)

def write_file(filename, content):
  result_file = open(filename, 'w')
  result_file.write(content)
  result_file.close()

def save_results(results):
  content = to_csv(results)
  write_file('result.csv', content)

name = ask_name()
amount = ask_amount()
time_year = ask_time_year()

results = calculate_all_investment_returns(amount, time_year)
save_results(results)
print("{0}, o resultado foi salvo em 'result.csv'".format(name))
