# File 1: one_time_pad_cipher.py
import random
import string

def generate_random_key(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def encryption(plain_text, key):
    if len(key) < len(plain_text):
        raise ValueError("Key must be at least as long as the plaintext")

    cipher_text = []
    for p, k in zip(plain_text, key):
        if p.isalpha():
            base = ord('A') if p.isupper() else ord('a')
            p_offset = ord(p) - base
            k_offset = ord(k.lower()) - ord('a')
            c = chr((p_offset + k_offset) % 26 + base)
            cipher_text.append(c)
        else:
            cipher_text.append(p)
    return "".join(cipher_text)

def decryption(cipher_text, key):
    if len(key) < len(cipher_text):
        raise ValueError("Key must be at least as long as the ciphertext")

    plain_text = []
    for c, k in zip(cipher_text, key):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            c_offset = ord(c) - base
            k_offset = ord(k.lower()) - ord('a')
            p = chr((c_offset - k_offset + 26) % 26 + base)
            plain_text.append(p)
        else:
            plain_text.append(c)
    return "".join(plain_text)
