# Assigning Roman Numeral Values
def roman_char_values(char):
    if char == "I":
        return 1
    elif char == "V":
        return 5
    elif char == "X":
        return 10
    elif char == "L":
        return 50
    elif char == "C":
        return 100
    elif char == "D":
        return 500
    elif char == "M":
        return 1000
    else:
        return -1

# Sample Input
roman = 'XXXIV'

def parse_roman(roman):
    total = 0
    for left_index, left_char in enumerate(roman):
        right_index = left_index + 1
        if right_index < len(roman):
            right_char = roman[left_index + 1]
            left_value = roman_char_values(left_char)
            right_value = roman_char_values(right_char)
            if left_value < right_value:
                left_value *= -1
            total += left_value
        else:
            total += roman_char_values(left_char)
    return total

# Tests
assert parse_roman('I') == 1
assert parse_roman('IX') == 9
assert parse_roman('X') == 10
assert parse_roman('XI') == 11
assert parse_roman('XX') == 20
assert parse_roman('XXIV') == 24
assert parse_roman('XXV') == 25
assert parse_roman('XXVI') == 26
assert parse_roman('CDXLVII') == 447