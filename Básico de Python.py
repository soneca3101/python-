'''print("hello world!")

docString - não é comentário mas é usado com um

# comentário


# AULA 02

separadores
\r\n - quebra a linha qlqr windows
\n - quebra a linha qlqr windows 11
sep='' - escolhe qual separador entre o texto na mesma linha
end='' - escolhe qual separador entre o texto em linhas diferentes

print(12, 34, 1011, sep=' ', end='##')
print(56, 78, sep='-', end='\n')
print(9, 10,sep='-', end='\r\n')
print('quebra de linha')



#AULA 3

# Aspas
print('gleydson martins')
print(1, '"gleydson martins"')

# Aspas duplas
print("gleydson martins")


# Escape
print('gleydson \'martins\'')

# r
print(r'gleydson \'martins\'')
'''

nome = 'Gleydson'
'''sobrenome = 'Martins Raimundo'
idade = 27
ano_de_nascimento = 1997
maior_de_idade = idade >= 18
altura_em_metros = 1.89
print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de Nascimento: ', ano_de_nascimento)
print('É maior? ', maior_de_idade)
'''

'''
OPERADORES MATEMÁTICOS

adição: +
subtração: -
multiplicação: *
divisão: / >>> float
divisão inteira: // >>> trava as casas decimais em 0
exponenciação: **
resto da divisão(módulo): %
'''

h = 1.89
peso = 80
imc = peso / h**2

#print('Imc: ', imc)

#Fstrings
linha1 = f'{nome} tem {h:.2f} de altura'
linha2 = f'pesa {peso} kg e seu IMC é {imc:.2f}'
print(linha1)
print(linha2)

#Format
string = 'h={}, peso={}, imc={:.2f}'
formato = string.format(h, peso, imc)
print(formato)

#input
nome = input('Digite seu nome? ')
print(f'O seu nome é {nome}')

#if/elif/else
entrada = input('voce quer entrar ou sair?')

if entrada == 'entrar':
    print('voce entrou no sistema')
elif entrada == 'sair':
    print('voce saiu do sistemagleyds')
else:
    print('voce não digitou nem "entrar" e nem "sair".')

#operadores de comparação
'''
maior >
maior ou igual >=
menor <
menor ou igual <=
igual ==
diferente !=
'''

#and
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel1 = 'ABC'
print(f'{variavel1}')
print(f'{variavel1: >10}')
print(f'{variavel1: <10}.')
print(f'{variavel1: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel1!r}')

"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel2 = 'Olá mundo'
print(variavel2[::-1])

"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')
