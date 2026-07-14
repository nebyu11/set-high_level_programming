#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    r_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    for i in range(len(roman_string)):
        ch = roman_string[i]
        if ch not in r_dict:
            return 0
        val = r_dict[ch]
        if i > 0 and val > r_dict[roman_string[i - 1]]:
            num += val - 2 * r_dict[roman_string[i - 1]]
        else:
            num += val
    return num
