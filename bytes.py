# diminuir bytes
import binascii 


letras = 'abcdef'
def diminuir_letra(s):
    return letras[letras.index(s)-1]

print(diminuir_letra('f'))
x = input(f'Digite seus bytes: ')

bytes_array = x.split(' ')
bytes_finais = []

byte_atual = ''
for i in bytes_array:
    tmp = []
    for j in i: 
        if j.isdigit():
            tmp.append(str(int(j)-1))
        else:
            tmp.append(diminuir_letra(j))

        if len(tmp) == 2:
            byte_atual += ''.join(tmp) + ' '
        
print(f'Original: {x} '.ljust(20),          f'| Text: {bytes.fromhex(x).decode("utf-8")}')
print(f'Bytes: {byte_atual} '.ljust(20),    f'| Text: {bytes.fromhex(byte_atual).decode("utf-8")}')
