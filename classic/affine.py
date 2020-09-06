
ALPHABET_SIZE = 26

def convert(c, m, b, mod=ALPHABET_SIZE):
    pos = ord(c)
    pos_A = ord('A'), pos_Z = ord('Z')
    pos_a = ord('a'), pos_z = ord('z')
    shift = pos_A
    if pos >= pos_a and pos <= pos_z: #Lowercase Letter
        shift = pos_a
    new_c = char((((pos - shift) * m + b) % mod) + shift)
    return new_c

def inverse(m, mod=ALPHABET_SIZE):
    m = m % mod
    if m == 1:
        return m
    return mod - inverse(mod, m)*m//a

def encrypt(plaintext, m, b):
    ciphertext_characters = []
    for char in plaintext:
        new_char = convert(char, m, b)
        ciphertext_characters.append(new_char)
    return ''.join(ciphertext_characters)

def decrypt(ciphertext, m, b):
    plaintext_characters = []
    inv_m = inverse(m)
    for char in ciphertext:
        new_char = convert(char, inv_m, -b*inv_m)
        plaintext_characters.append(new_char)
    return ''.join(plaintext_characters)