from hamming_code import *


def _test_hamming_code(bits, expected):
    print(f'\n\tTest Hamming Code - {bits}')

    result = hamming_code(bits)
    if result == expected:
        print(f'\t{result}\t✔')
    else:
        print(f'\t{result}')


def _test_hamming_decode(bits, expected):
    print(f'\n\tTest Hamming Decode - {bits}')
    counter = 0

    for index in range(len(bits)):
        corrupted_bits = bits.copy()
        corrupted_bits[index] = 1 if corrupted_bits[index] == 0 else 0

        result = hamming_decode(corrupted_bits.copy())
        if result == expected:
            print(f'{index:>2}: {corrupted_bits} -> {result}\t✔')
            counter += 1
        else:
            print(f'{index:>2}: {corrupted_bits} -> {result}')

    print(f'\t{counter}/{len(bits)} expected results')


hamming_test_dict = {
    '0101': '0100101',
    '0100': '1001100',
    '0011': '1000011',
    '11001111': '011010001111'
}


print('\n\t-- Hamming Code --')
for data, expected_result in hamming_test_dict.items():
    data = [int(bit) for bit in data]
    expected_result = [int(bit) for bit in expected_result]

    _test_hamming_code(data, expected_result)


print('\n\n\t-- Hamming Decode --')
for expected_result, data in hamming_test_dict.items():
    data = [int(bit) for bit in data]
    expected_result = [int(bit) for bit in expected_result]

    _test_hamming_decode(data, expected_result)
