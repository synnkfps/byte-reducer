import re#laxing

# input2hexbytes
text = input(f'Digite um texto: ').encode('utf-8')
converted = bytes.hex(text)
final = ' '.join(re.findall('..', converted))

# hexbytes2text
letras = 'abcdef'
def diminuir_letra(s): return letras[letras.index(s)-1]

print(diminuir_letra('f'))
x = final

bytes_array = x.split(' ')
bytes_finais = []

byte_atual = ''
for i in bytes_array:
    tmp = []
    for j in i: 
        if j.isdigit():
            tmp.append(str(int(j)-1 if int(j)!=0 else 'f'))
        else:
            tmp.append(diminuir_letra(j))

        if len(tmp) == 2:
            byte_atual += ''.join(tmp) + ' '
        
decoded = bytes.fromhex(byte_atual).decode("utf-8").encode('utf-8')
decoded = decoded.decode('unicode_escape').replace('\x1f', ' ').encode('utf-8').decode('utf-8')
print(f'Original: {x} '.ljust(20),          f'| Text: {bytes.fromhex(x).decode("utf-8")}')
print(f'Bytes: {byte_atual} '.ljust(20),    f'| Text: {str(decoded)}')
