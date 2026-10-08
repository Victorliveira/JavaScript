import time

vermelho = '\033[31m'
verde = '\033[32m'
limpar = '\033[m'

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')
print('0 - Sair')

opcao = int(input('Escolha uma opção: '))

while opcao <0 or opcao > 4:
    print(f'{vermelho}Operação inválida. Digite novamente{limpar}')
    opcao = int(input('Escolha uma opção: '))

while True:
    if opcao == 1:
        print(f'A soma entre {a} e {b} é igual a {a + b}')
    elif opcao == 2:
        print(f'A subtração entre {a} e {b} é igual a {a - b}')
    elif opcao == 3:
        print(f'A multiplicação entre {a} e {b} é igual a {a * b}')
    elif opcao == 4:
        print(f'A divisão entre {a} e {b} é igual a {a / b:.2f}')
    time.sleep(0.5)

    mudar = str(input('Deseja mudar os números? S/N ')).upper()
    if mudar[0] not in 'S or N':
        print(f'{vermelho}Operação inválida. Digite novamente{limpar}')
        mudar = str(input('Deseja mudar os números? S/N ')).upper()
    elif mudar[0] == 'S':
        a = float(input('Digite um número: '))
        b = float(input('Digite outro número: '))


    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('0 - Sair')
    time.sleep(0.5)
    opcao = int(input('Escolha uma opção: '))
    while opcao <0 or opcao > 4:
        print('Operação inválida. Digite novamente')
        opcao = int(input('Escolha uma opção: '))
    time.sleep(0.5)
    if opcao == 0:
        break    


print(f'{verde}Obrigado por usar a calculadora!')
print(f'Volte sempre!{limpar}')

