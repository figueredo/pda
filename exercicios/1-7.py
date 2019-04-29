# Altere o script para calcular o valor acumulado a cada ano até o ano
# informado pelo usuário.

def compound_interest(amount, interest_rate, time):
  return amount * (1 + interest_rate) ** time

def calculate_return_poupanca(amount, time_year):
  interest_rate_month = 0.469 / 100
  return compound_interest(amount, interest_rate_month, time_year * 12)

def calculate_return_xp(amount, time_year):
  interest_rate_year = (105 / 100) * (7.5 / 100)
  return compound_interest(amount, interest_rate_year, time_year)

def calculate_all_returns_poupanca(amount, time_year):
  roi_poupanca = []
  for year in range(time_year + 1):
    roi = calculate_return_poupanca(amount, year)
    roi_poupanca.append(roi)
  return roi_poupanca

def calculate_all_returns_xp(amount, time_year):
  roi_xp = []
  for year in range(time_year + 1):
    roi = calculate_return_xp(amount, year)
    roi_xp.append(roi)
  return roi_xp

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

def to_formatted_str(float_list):
  element_template = '{0:.2f}'

  str_list = []
  for element in float_list:
    str_element = element_template.format(element)
    str_list.append(str_element)

  return ', '.join(str_list)

def print_result(name, amount, time_year, roi_poupanca, roi_xp):
  message_header_template = '{name}, o retorno de investir R${amount} durante {time_year} anos é:'
  message_roi_template = '- {investiment_name}: {roi_list}'

  message_header = message_header_template.format(name=name, amount=amount, time_year=time_year)
  message_roi_poupanca = message_roi_template.format(
    roi_list=to_formatted_str(roi_poupanca),
    investiment_name='Poupança')
  message_roi_xp = message_roi_template.format(
    roi_list=to_formatted_str(roi_xp),
    investiment_name='XP')

  print(message_header)
  print(message_roi_poupanca)
  print(message_roi_xp)

name = ask_name()
amount = ask_amount()
time_year = ask_time_year()

roi_poupanca = calculate_all_returns_poupanca(amount, time_year)
roi_xp = calculate_all_returns_xp(amount, time_year)

print_result(name, amount, time_year, roi_poupanca, roi_xp)
