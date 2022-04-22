from parity import *


def find_error(bits):
    error_index = []
    check_bits = calculate_parity(bits.copy())

    for index in range(len(bits)):
        if bits[index] != check_bits[index]:
            error_index.append(index)
    return error_index


def correct_error(bits, error_index):
    error_position = 0

    for index in error_index:
        error_position += index + 1
    bits[error_position - 1] = 0 if bits[error_position - 1] == 1 else 1
    return bits


def hamming_code(bits):
    bits = insert_parity(bits)
    bits = calculate_parity(bits)
    return bits


def hamming_decode(bits):
    error_index = find_error(bits)

    if len(error_index) != 0:
        bits = correct_error(bits, error_index)

    bits = remove_parity(bits)
    return bits
