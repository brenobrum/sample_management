import csv

list_of_samples = []

# retorna se o ponto é valido ou não
def validate_points(point):
  if not (point.isdigit()): # valida se o ponto é um digito
    return False
  points = [37, 38, 39, 62]
  return int(point) in points # retorna verdadeiro se o ponto estiver na lista [37, 38, 39, 62]

# retorna se a concentração é valida ou não
def validate_concentration(concentration):
  if not (concentration.isdigit()): # valida se o ponto é um digito
    return False
  return int(concentration) >= 0 # retorna verdadeiro se a concentração não for negativa

# exibe a média de concentração por ponto
def show_concentration_avarege(point, dict_of_points):
  if point in dict_of_points: # verifica se o ponto passado se encontra no dict_of_points
    print("Ponto", point,":", (dict_of_points[point]['concentration_sum'] / dict_of_points[point]['count']))
  else: 
    print("Ponto", point, ": Não houveram amostras para o ponto")

def option1():
  valid = False
  while not valid: # enquanto a opção inserida não for valida o ponto será solicitado infinitamente
    point = input('Informe o número do ponto: ')
    valid = validate_points(point) # chamada da função validate_points para identificar se o ponto é valido
    if not valid:
      print('número do ponto invalido, deve selecione um entre 37, 38, 39 ou 62') # caso o ponto não seja valido a mensagem é exibida

  valid = False
  while not valid:
    concentration = input('Informe a concentração de E. coli: ')
    valid = validate_concentration(concentration) # chamada da função validate_concentration para identificar se a concentração é valida
    if not valid:
      print('concentração deve ser maior que 0') # caso a concentração não seja valida a mensagem é exibida

  list_of_samples.append({'point': int(point), 'concentration': int(concentration)})

def option2():
  more_inputs = True
  while more_inputs:
    option1() # chama a opção 1 até que o usuário não queira mais adicionar registros
    more_inputs = not (input('Pressione qualquer tecla para inserir mais um registro ou OK para retornar: ').upper() == 'OK')

def option3():
  dict_of_points = {}
  higher_concentration_point = {'point': 0, 'concentration': 0} # instancia o ponto com maior concentração
  higher_concentration_sample = {'point': 0, 'concentration': 0} # instancia a amostra com maior concentração

  for i in list_of_samples:
    if i['point'] in dict_of_points: # caso já exista a chave do ponto no dicionario
      dict_of_points[i['point']]['count'] += 1 # soma 1 ao contador de vezes que o ponto aparece em amostras
      dict_of_points[i['point']]['concentration_sum'] += i['concentration'] # soma o valor da concentração da amostra ao somatorio do valor de concentração do dicionario para o ponto
    else: # caso a chave do ponto ainda não exista no dicionario
      dict_of_points[i['point']] = { 'count': 1, 'concentration_sum': i['concentration']} # cria a chave com o contador de vezes que o ponto aparece igual a 1 e o valor da concentração igual ao valor de concetração da amostra
    
    if dict_of_points[i['point']]['concentration_sum'] > higher_concentration_point['concentration']: # atualiza o valor do ponto de maior concentração
      higher_concentration_point = {'point': i['point'], 'concentration': dict_of_points[i['point']]['concentration_sum'] }
    if i['concentration'] > higher_concentration_sample['concentration']: # atualiza o valor da amostra de maior concentração
      higher_concentration_sample = {'point': i['point'], 'concentration': i['concentration']}

  if not higher_concentration_point == {'point': 0, 'concentration': 0}: # verifica se o ponto de maior concentração não é vazio
    print("Ponto com maior concentração é o", higher_concentration_point['point'], "com a soma de concentração igual a", higher_concentration_point['concentration']) # exibe a concentração do ponto de maior concentração
  else:
    print("Não foi possivel calcular o ponto com maior concentração por não haver amostras") 
  
  if not higher_concentration_sample == {'point': 0, 'concentration': 0}: # verifica se a amostra de maior concentração não é vazio
    print("A amostra com maior concentração é do ponto", higher_concentration_sample['point'], "com uma concentração igual a", higher_concentration_sample['concentration']) # exibe a amostra do ponto de maior concentração
  else:
    print("Não foi possivel calcular a amostra com maior concentração por não haver amostras") 
  
  print("Média de concentração dos pontos: ")
  show_concentration_avarege(37, dict_of_points) # exibe média do ponto 37
  show_concentration_avarege(38, dict_of_points) # exibe média do ponto 38
  show_concentration_avarege(39, dict_of_points) # exibe média do ponto 39
  show_concentration_avarege(62, dict_of_points) # exibe média do ponto 62

# salva arquivo csv com os valores de list_of_samples
def option4():
  fields = ['PONTO', 'CONCENTRAÇÃO']
  rows = [] 
  for i in list_of_samples:
    rows.append([i['point'], i['concentration']]) # transforma objeto em lista

  # escreve no arquivo "gravar_amostras.csv"
  with open('gravar_amostras.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)
  print("Todas as amostras foram salvas no arquivo \"gravar_amostras.csv\"")

def option5():
  with open('carregar_amostras.csv', mode ='r')as file:
    # le arquivo "carregar_amostras.csv"
    csvFile = csv.reader(file)
  
    count = 0
    for lines in csvFile:
      if count > 0:
        list_of_samples.append({'point': int(lines[0]), 'concentration': int(lines[1])}) # transforma valor lido em objeto
      else:
        count = 1
  print("As amostras foram carregadas do arquivo \"carregar_amostras.csv\"")

def option6():
  if list_of_samples: # verifica se a lista está vazia
    print('Ponto Concentração')
    for i in list_of_samples: # exibe todas as amostras de list_of_samples
      print(i['point'], i['concentration'])
  else:
    print('Não existem amostras na lista de amostras.')
 
while True:
  print('1 - Novo registro')
  print('2 - N novos registros')                                                                                     
  print('3 - Calcular propriedades ')                                                                                     
  print('4 - Gravar em arquivo  ')                                                                                     
  print('5 - Carregar de arquivo   ')                                                                                     
  print('6 - Visualizar registros  ')
  option = input('Digite uma opção ou FIM para sair: ')

  # ifs de 1-6 para chamar as funções solicitadas
  if option == '1':
    print('-------------------')
    option1()
    print('-------------------')
  elif option == '2':
    print('-------------------')
    option2()
    print('-------------------')
  elif option == '3':
    print('-------------------')
    option3()
    print('-------------------')
  elif option == '4':
    print('-------------------')
    option4()
    print('-------------------')
  elif option == '5':
    print('-------------------')
    option5()
    print('-------------------')
  elif option == '6':
    print('-------------------')
    option6()
    print('-------------------')
  elif option.upper() == 'FIM':  # caso o usuário digite 'fim', a execução termina
    exit()
  else: # verifica se o usuário digitou um comando correto.
    print('Opção invalida, tente novamente.')
