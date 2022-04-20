from hamming_code import *

print('-- Hamming Code --')
bits = input('Enter the data bits: ')
bits = [int(bit) for bit in bits]

result = hamming_code(bits)
result = ''.join(str(bit) for bit in result)

print(f'Generated Hamming Code: {result}')

print('\n-- Hamming Decode --')
bits = input('Enter the data bits: ')
bits = [int(bit) for bit in bits]

result = hamming_decode(bits)
result = ''.join(str(bit) for bit in result)
print(f'Decoded Data: {result}')
