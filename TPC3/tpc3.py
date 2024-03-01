import sys
import re

soma = 0
lista = []
state = 'OFF'
for line in sys.stdin:
    lista.extend(re.findall(r'OFF|ON|=|\d+',line,re.IGNORECASE))

for i in lista:
    if i.upper() == 'ON':
        state = 'ON'
    elif i.upper() == 'OFF':
        state = 'OFF'
    elif i == '=':
        print("Soma: ", soma)
    else: #Somar
        if(state == 'ON'):
            soma+=int(i)