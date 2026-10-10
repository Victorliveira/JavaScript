import time

vermelho = '\033[31m'
verde = '\033[32m'
limpar = '\033[m'

a = 1
b = 1

a = str(input('Digite o primeiro número: ')).replace(',','.')
b = str(input('Digite o segundo número: ')).replace(',','.')

#Transforma o valor para o tipo flutuante
a = float(a)
b = float(b)

# Opções da calculadora
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')

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
        while True:
            try:
                resultado = a/b
            except ZeroDivisionError:
                print(f'{vermelho}Você não pode dividir por zero!{limpar}')
                a = str(input('Digite o primeiro número: ')).replace(',','.')
                b = str(input('Digite o segundo número: ')).replace(',','.')
                a = float(a)
                b = float(b)
            else:
                break
        print(f'A divisão entre {a} e {b} é igual a {a / b:.2f}')
    time.sleep(0.5)

    mudar = str(input('Deseja mudar os números? S/N ')).upper()
    if mudar[0] not in 'S or N':
        print(f'{vermelho}Operação inválida. Digite novamente{limpar}')
        mudar = str(input('Deseja mudar os números? S/N ')).upper()
    elif mudar[0] == 'S':
        a = str(input('Digite o primeiro número: ')).replace(',','.')
        b = str(input('Digite o segundo número: ')).replace(',','.')
        a = float(a)
        b = float(b)


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

