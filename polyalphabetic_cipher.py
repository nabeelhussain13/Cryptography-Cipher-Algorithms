def generate_key(text, key):
    key = list(key)
    key_extended = []
    key_index = 0

    for char in text:
        if char.isalpha():
            key_extended.append(key[key_index % len(key)])
            key_index += 1
        else:
            key_extended.append(' ')  # preserve spacing for non-alphabet characters
    return "".join(key_extended)

def encryption(plain_text, key):
    cipher_text = []
    key = generate_key(plain_text, key)

    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            is_upper = plain_text[i].isupper()
            base = ord('A') if is_upper else ord('a')
            k = ord(key[i].lower()) - ord('a')
            shift = (ord(plain_text[i]) - base + k) % 26
            cipher_char = chr(base + shift)
            cipher_text.append(cipher_char)
        else:
            cipher_text.append(plain_text[i])

    return "".join(cipher_text)

def decryption(cipher_text, key):
    plain_text = []
    key = generate_key(cipher_text, key)

    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            is_upper = cipher_text[i].isupper()
            base = ord('A') if is_upper else ord('a')
            k = ord(key[i].lower()) - ord('a')
            shift = (ord(cipher_text[i]) - base - k + 26) % 26
            plain_char = chr(base + shift)
            plain_text.append(plain_char)
        else:
            plain_text.append(cipher_text[i])

    return "".join(plain_text)
