texto = "Estou estudando Python no 'LinkedIn Learning'"
print(texto)
print(texto[0])
print(texto[16:22])
print(texto[26:]) #fatiamente inicio:final
print(texto.lower()) #formata a string para ter apenas letras minusculas
print(texto.upper()) #formata a string para ter apenas letras maiusculas
print(texto.title()) #torna todas as letras iniciais maiusculas
print(texto.capitalize()) #torna apenas a primeira letra da frase maiuscula

from datetime import datetime
print(f'Data e horário atual: {datetime.now()}')
a = 4
b = 3

print('A divisão de {} por {} é {:.3f}'.format(a, b, a/b)) #format define o formato do dado ':.3f' define que havera apenas 3 casas decimais depois da vírugla

a = 'olá mundo'
b = 'Alfred'

print('{0}, me chamo {1}'.format(a, b)) #format define onde as variáveis ficam
print('{1}, me chamo {0}'.format(a, b)) #define onde elas ficam e como aparecem
print('{}, me chamo {}'.format(a, b))
print('{c}, me chamo {d}'.format(c='Olá', d='Bruce'))