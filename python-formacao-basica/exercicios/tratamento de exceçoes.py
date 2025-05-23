#protege o programa contra erros, trata os erros do programa
try:
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    r = a / b
    print('o resultado é:', r)
except ZeroDivisionError:
    print('O valor de B não pode ser zero')
except ValueError:
    print('Digíte números inteiros para A e B')
except:
    print('Erro ao receber o número')
print('Fim do programa!')