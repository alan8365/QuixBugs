

import string
def to_base(num, b):
    result = ''
    alphabet = string.digits + string.ascii_uppercase
    if b <= 0 or b > len(alphabet):
        return 'Invalid base'
    while num > 0:
        i = num % b
        num = num // b
        result = result + alphabet[i]
    return result[::-1]




