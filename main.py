from hamming import *

print('  _   _                                            ____          _      ')
print(' | | | | __ _ _ __ ___  _ __ ___ (_)_ __   __ _   / ___|___   __| | ___ ')
print(' | |_| |/ _` | \'_ ` _ \\| \'_ ` _ \\| | \'_ \\ / _` | | |   / _ \\ / _` |/ _ \\')
print(' |  _  | (_| | | | | | | | | | | | | | | | (_| | | |__| (_) | (_| |  __/')
print(' |_| |_|\\__,_|_| |_| |_|_| |_| |_|_|_| |_|\\__, |  \\____\\___/ \\__,_|\\___|')
print('                                          |___/                         ')

while True:
    answer = input('[1] - Code\t\t[2] - Decode\n[0] - Exit\t\tOption: ')
    match answer:
        case '1':
            print('\n-- Hamming Code --')

            bits = input('Enter the data bits: ')
            bits = [int(bit) for bit in bits]

            result = hamming_code(bits)
            result = ''.join(str(bit) for bit in result)
            print(f'Generated Hamming Code: {result}')

        case '2':
            print('\n-- Hamming Decode --')

            bits = input('Enter the data bits: ')
            bits = [int(bit) for bit in bits]

            result = hamming_decode(bits)
            result = ''.join(str(bit) for bit in result)
            print(f'Decoded Data: {result}')

        case '0':
            exit()
    print('\n')
