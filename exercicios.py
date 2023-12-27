# print('Python na Escola de Programação da Alura')

# douglas_nome = 'Douglas'
# douglas_idade = 30

# print(f'Meu nome é {douglas_nome} e tenho {douglas_idade} anos')

# print('A','L','U','R','A', sep='\n')


# pi = 3.14159
# print(f'O valor arredondado de pi é: {pi:.2f}')


# ## PAR OU IMPAR:
# numero_escolhido = int(input('Informe seu número: '))
# if numero_escolhido % 2 == 0:
#     print('Seu número é par')
# else:
#     print('Seu número é ímpar')

# ## IDADE:
# idade_escolhida = int(input('Informe a idade: '))
# if 0 < idade_escolhida <= 12:
#     print("Criança")
# elif 12 < idade_escolhida <= 18:
#     print("Adolescente")
# elif idade_escolhida > 18:
#     print("Adulto")
# else: 
#     print("Valor inválido!")

# ## VERIFICADOR DE USUARIO E SENHA
# usuario = 'douglas'
# senha = 'teste'

# usuario_escolhido = input('Informe o usuario: ')
# senha_escolhida = input('Informe a senha: ')

# if senha_escolhida == senha and usuario_escolhido == usuario:
#     print('login efetuado')
# else:
#     print('usuario ou senha inválido')

# ## COORDENADAS PLANO CARTESIANO
# x = int(input('Informe o valor de X: '))
# y = int(input('Informe o valor de Y: '))

# if x > 0 and y > 0:
#     print('Primeiro quadrante')
# elif x < 0 and y > 0:
#     print('Segundo quadrante')
# elif x < 0 and y < 0:
#     print('Terceiro quadrante')
# elif x > 0 and y < 0:
#     print('Quarto quadrante')
# else: 
#     print('O ponto está localizado no eixo ou origem')

# ## ALGUMAS LISTAS
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nomes = ['douglas', 'tamara', 'daniel', 'fernando']
# anos = [1993, 2023]

# ## EXIBIÇÃO DOS ITENS DA LISTA
# for numero in numeros:
#     print(numero)
# print()

# ## SOMA DOS IMPARES
# soma_impares = 0
# for i in range(1, 11, 2):
#     soma_impares += i
# print(soma_impares)
# print()

# ## EXIBIÇÃO AO CONTRÁRIO
# for i in range(10, 0, -1):
#     print(i)
# print()

# ## TABUADA
# numero_tabuada = int(input('Digite um numero para a tabuada: '))
# for i in range(1, 11):
#     resultado = numero_tabuada * i
#     print(f'{numero_tabuada} x {i} = {resultado}')
# print()

# ## SOMA DE NUMEROS DA LISTA
# lista_numeros = [10, 5, 8, 3, 7]
# soma = 0
# try:
#     for numero in lista_numeros:
#         soma += numero
#     print(f"Soma dos elementos: {soma}")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# ## MÉDIA DE VALORES DA LISTA
# lista_valores = [15, 20, 25, 30]
# soma_valores = 0
# try:
#     for valor in lista_valores:
#         soma_valores += valor
#     media = soma_valores // len(lista_valores)
#     print(f"Média dos valores: {media}")
# except ZeroDivisionError:
#     print("A lista está vazia, não é possível calcular a média.")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# ## CRIAÇÃO DE DICIONÁRIO
# pessoa = {'nome':'Douglas', 'idade':30, 'cidade':'Rio de Janeiro'}

# ## ALTERAÇÃO DE UM VALOR
# pessoa['idade'] = 31

# ## CRIAÇÃO DE NOVO VALOR
# pessoa['profissão'] = ['estudante']

# ## EXCLUSÃO DE VALOR
# del pessoa['cidade']

# ## DICIONÁRIO COM NÚMEROS QUADRADOS
# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

# ## VERIFICAÇÃO DE EXISTÊNCIA DENTRO DO DICIONÁRIO
# pessoa = {'nome':'Douglas', 'idade':30, 'cidade':'Rio de Janeiro'}
# if 'nome' in pessoa:
#     print("a chave 'nome' já existe")
# else:
#     print("a chave 'nome' não existe")

# ## CONTADOR DE PALAVRAS
# frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos"
# contagem_palavras = {}
# palavras = frase.split()
# for palavra in palavras:
#     contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
# print(contagem_palavras)
