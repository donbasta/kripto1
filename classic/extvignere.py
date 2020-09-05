def parse_path(text):
    text = text[1:]
    name = len(text)-1
    ext = len(text)-1

    if '.' in text:
        while text[ext] != '.':
            ext -= 1
        text = text[:ext]

    while text[name] != '/' and text[name] != '\\':
        name -= 1
    
    return '.' + text[:name], text[name:]


def encrypt(text, key, is_file=False):
    '''
    For encrypting text/file with Extended Vignere Cipher
    '''
    if is_file:
        # Get path, filename, and extension
        path, filename = parse_path(text)
        
        # Open file to get byte data
        in_file = open(text, 'rb')
        data = in_file.read()
        in_file.close()

        enc_bytes = bytearray()
        for i in range(len(data)):
            proc_byte = (data[i] + ord(key[i % len(key)])) % 256
            enc_bytes.append(proc_byte)

        # Save the encrypted byte data    
        enc_file_path = path + filename + "_enc"
        enc_file = open(enc_file_path, 'wb')
        enc_file.write(enc_bytes)
        enc_file.close()

        # Return path
        return enc_file_path

    else:
        ciphertext = ""
        for i in range(len(text)):
            c_val = chr(
                (ord(text[i]) + ord(key[i % len(key)])) % 256
            )
            ciphertext += c_val

        return ciphertext


def decrypt(text, key, is_file=False):
    '''
    For decrypting text with Extended Vignere Cipher
    '''

    if is_file:
        # Get path, filename, and extension
        path, filename = parse_path(text)
        
        # Open file to get byte data
        in_file = open(text, 'rb')
        data = in_file.read()
        in_file.close()

        dec_bytes = bytearray()
        for i in range(len(data)):
            proc_byte = (data[i] - ord(key[i % len(key)])) % 256
            dec_bytes.append(proc_byte)

        # Save the decrypted byte data    
        dec_file_path = path + filename + "_dec"
        dec_file = open(dec_file_path, 'wb')
        dec_file.write(dec_bytes)
        dec_file.close()

        # Return path
        return dec_file_path

    else:
        text = text.replace(" ", "")
        plaintext = ""
        for i in range(len(text)):
            c_val = chr(
                (ord(text[i]) - ord(key[i % len(key)])) % 256
            )
            plaintext += c_val

        return plaintext
