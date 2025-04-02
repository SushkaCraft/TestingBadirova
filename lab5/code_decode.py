def encoding_dict():
    encoding = {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24',
        'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34',
        'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44',
        'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54',
        'Z': '55', ' ': '00'
    }
    return encoding

def create_decoding_dict():
    decoding = {}
    
    for char, code in encoding_dict().items():
        if code not in decoding:
            decoding[code] = char
    
    return decoding

def encode_text(text):
    encoded = []
    encoding = encoding_dict()
    for char in text.upper():
        if char in encoding:
            encoded.append(encoding[char])
    return ''.join(encoded)
    
def decode_text(text):
    decoded = []
    decoding = create_decoding_dict()
    for i in range(0, len(text), 2):
        code = text[i:i+2]
        if code in decoding:
            decoded.append(decoding[code])
    return ''.join(decoded)

code_str = 'Hello World'

# print(create_decoding_dict())

print(encode_text(code_str))

encode_str = encode_text(code_str) # '2315313134005234423114'

print(decode_text(encode_str))
