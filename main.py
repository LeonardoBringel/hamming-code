from hamming_code import *

bits = input('Enter the data bits: ')
bits = [int(bit) for bit in bits]

result = hamming_code(bits)

result = ''.join(str(bit) for bit in result)
print(f'Generated Hamming Code: {result}')
