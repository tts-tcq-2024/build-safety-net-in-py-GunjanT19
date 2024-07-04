def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def remove_consecutive_duplicates(s):
    result = [s[0]]
    for char in s[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)

def encode_characters(name):
    encoded = [get_soundex_code(name[0])]
    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0':
            encoded.append(code)
    return ''.join(encoded)

def generate_soundex(name):
    if not name:
        return ""
    
    # Retain the first letter and encode the rest
    first_letter = name[0].upper()
    encoded = encode_characters(name)

    # Remove consecutive duplicates
    encoded = remove_consecutive_duplicates(encoded)
    
    # Combine the first letter with the encoded characters and pad with zeros
    soundex = first_letter + encoded[1:]
    soundex = soundex[:4].ljust(4, '0')

    return soundex
