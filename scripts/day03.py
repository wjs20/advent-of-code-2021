from math import prod
from utils import get_input
from collections import Counter

def parse_report(report):
    return [[int(bit) for bit in bitstring if bit.isdigit()] for bitstring in report.splitlines()]

def transpose(array):
    return list(zip(*array))

def mode(array):
    c = Counter(array)
    if c[1] >= c[0]:
        return 1
    else:
        return 0

def get_modes(array, axis = 1):
    if axis == 1:
        array = transpose(array)
    return [mode(a) for a in array]

def bit_to_dec(bitarray): 
    bitstring = ''.join([str(bit) for bit in bitarray])
    return int(bitstring, 2)

def extract_power_consumption_rates(report):
    bitarrays = parse_report(report)
    gamma = get_modes(bitarrays)
    epsilon = [0 if bit == 1 else 1 for bit in gamma]
    return [bit_to_dec(rate) for rate in [gamma, epsilon]]

def compute_power_consumption(report):
    rates = extract_power_consumption_rates(report)
    return prod(rates)

def extract_oxygen_rating(report):
    bitarrays = parse_report(report)
    position = 0
    while len(bitarrays) > 1:
        modes = get_modes(bitarrays)
        bitarrays = [line for line in bitarrays if line[position] == modes[position]]
        position += 1
    return bitarrays[0]

def extract_carbon_rating(report):
    bitarrays = parse_report(report)
    position = 0
    while len(bitarrays) > 1:
        modes = get_modes(bitarrays)
        bitarrays = [line for line in bitarrays if not line[position] == modes[position]]
        position += 1
    return bitarrays[0]

def compute_life_support_rating(report):
    oxygen = extract_oxygen_rating(report)
    carbon = extract_carbon_rating(report)
    return prod([bit_to_dec(rate) for rate in [oxygen, carbon]])

if __name__ == '__main__':
    example = """00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010"""

    assert compute_power_consumption(example) == 198, 'power consumption example failed'
    assert compute_life_support_rating(example) == 230, 'life support example failed'
    report = get_input('day03.txt')
    print(compute_power_consumption(report))
    print(compute_life_support_rating(report))