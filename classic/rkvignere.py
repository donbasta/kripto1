def encrypt(plaintext, word):
    '''
    For encrypting plaintext with Running Key Vignere Cipher
    '''
    key = word + plaintext[:-(len(word))]
    ciphertext = ""
    for i in range(len(plaintext)):
        c_val = chr(
            (ord(plaintext[i]) + ord(key[i % len(key)]) - 2 * ord('A')) % 26 + ord('A')
        )
        ciphertext += c_val

    return ciphertext


def decrypt(ciphertext, word):
    '''
    For decrypting plaintext with Running Key Vignere Cipher
    '''
    ciphertext = ciphertext.replace(" ", "")
    plaintext = ""
    key = word
    for i in range(0, len(ciphertext), len(word)):
        temp = ""
        for j in range(len(key)):
            c_val = chr(
                (ord(ciphertext[i]) - ord(key[i % len(key)])) % 26 + ord('A')
            )
            plaintext += c_val
            temp += c_val
        key = temp

    return plaintext
