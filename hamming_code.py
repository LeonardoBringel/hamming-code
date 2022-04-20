from parity import *


def integrity_check(bits):
    check_bits = reset_parity(bits)
    check_bits = calculate_parity(check_bits)
    return check_bits == bits


def hamming_code(bits):
    bits = insert_parity(bits)
    bits = calculate_parity(bits)
    return bits


def hamming_decode(bits):
    result = []

    if integrity_check(bits):
        for index, bit in enumerate(bits):
            if index not in parity_index(bits):
                result.append(bit)
    else:
        return [0]
    return result
