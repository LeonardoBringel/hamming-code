def parity_index(bits):
    bit_index = 2
    parity_location = [0]

    while bit_index <= len(bits):
        parity_location.append(bit_index - 1)
        bit_index = bit_index * 2
    return parity_location


def parity_range(bits, interator):
    result = []
    next_bit = interator - 1
    cicle = interator

    for index, bit in enumerate(bits):
        if index == next_bit:
            result.append(index)
            cicle -= 1

            if cicle == 0:
                next_bit += interator + 1
                cicle = interator
            else:
                next_bit += 1
    return result


def parity(bits, interator):
    result = 0
    for index in parity_range(bits, interator):
        result += bits[index]
    return 0 if result % 2 == 0 else 1


def insert_parity(bits):
    for bit_index in parity_index(bits):
        bits.insert(bit_index, 0)
    return bits


def reset_parity(bits):
    for bit_index in parity_index(bits):
        bits[bit_index] = 0
    return bits


def calculate_parity(bits):
    for bit_index in parity_index(bits):
        bits[bit_index] = parity(bits, bit_index + 1)
    return bits
