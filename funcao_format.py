#exemplo1:

num1 = 10
num2 = 3

divisao = num1/num2
print(divisao)
print('{:.2f}'.format(divisao))
print( f'{divisao:.4f}' )

#exemplo2:

nome = "Paola da Silva"
print(f'{nome:#^20}')

#exemplo3:
num = 25
num_formatado = '{n:*<10} {n:#>10}'. format(n=num)
print(num_formatado)