def blockify(text):
    '''
    Mengembalikan teks yang diblok menjadi 5 huruf
    '''
    blocked_text = ""
    for i in range(len(text)):
        blocked_text += text[i]

        if i % 5 == 4:
            blocked_text += ' '
    
    return blocked_text

def alphabetify(text):
    '''
    Mengembalikan teks dengan semua tandabaca dan spasi dihilangkan, hanya 26 huruf alfabet saja
    '''
    return ''.join(c for c in text if c.isalpha()).upper()