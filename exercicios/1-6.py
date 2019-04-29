# Altere o script para validar que o usuário está digitando valores válidos:
# - nome deve ser não numérico
# - montante inicial deve ser número
# - tempo de investimento deve ser número
# Mantenha o script perguntando enquanto o usuário não digita o valor correto
# Dica: há métodos de string para verificar se o conteúdo é numérico

def compound_interest(amount, interest_rate, time):
  return amount * (1 + interest_rate) ** time

def calculate_return_poupanca(amount, time_year):
  interest_rate_month = 0.469 / 100
  return compound_interest(amount, interest_rate_month, time_year * 12)

def calculate_return_xp(amount, time_year):
  interest_rate_year = (105 / 100) * (7.5 / 100)
  return compound_interest(amount, interest_rate_year, time_year)

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

def print_result(name, amount, time_year, roi_poupanca, roi_xp):
  message_header_template = '{name}, o retorno de investir R${amount} durante {time_year} anos é:'
  message_roi_template = '- {investiment_name}: R${roi:.2f}'

  message_header = message_header_template.format(name=name, amount=amount, time_year=time_year)
  message_roi_poupanca = message_roi_template.format(
    roi=roi_poupanca,
    investiment_name='Poupança')
  message_roi_xp = message_roi_template.format(
    roi=roi_xp,
    investiment_name='XP')

  print(message_header)
  print(message_roi_poupanca)
  print(message_roi_xp)

name = ask_name()
amount = ask_amount()
time_year = ask_time_year()

roi_poupanca = calculate_return_poupanca(amount, time_year)
roi_xp = calculate_return_xp(amount, time_year)

print_result(name, amount, time_year, roi_poupanca, roi_xp)
