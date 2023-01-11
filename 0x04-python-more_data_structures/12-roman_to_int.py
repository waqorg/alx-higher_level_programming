#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(roman_string)):
        curr_val = roman_map[roman_string[i]]
        if i < len(roman_string) - 1:
            next_val = roman_map[roman_string[i + 1]]
            if curr_val < next_val:
                result -= curr_val
            else:
                result += curr_val
        else:
            result += curr_val
    return result
