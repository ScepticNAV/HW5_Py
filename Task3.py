with open('Task3_file1_code.txt', 'r') as file:                     
    file1 = file.read()

def encode(file):                                                   # Метод кодировки
    encode = '' 
    prev_char = ''
    count = 1 
    if not file:
        return ''
    for char in file: 
        if char != prev_char:
            if prev_char: 
                encode += str(count) + prev_char 
            count = 1 
            prev_char = char
        else:
            count += 1
    else:
        encode += str(count) + prev_char 
        return encode
        
print()
encoding = encode(file1)
print(f'{encoding}\n')

with open('Task3_file2_decoding.txt', 'r') as file:                 # Метод декодировки
    file2 = file.read()

def rle_decode(data): 
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char 
        else:
            decode += char * int(count)
            count = '' 
    return decode

decoding = rle_decode(file2)
print(f'{decoding}\n')