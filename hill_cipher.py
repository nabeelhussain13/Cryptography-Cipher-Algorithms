import numpy as np
from numpy.linalg import LinAlgError

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists")

def create_matrix(key, n):
    key = key.lower().replace(" ", "")
    if len(key) != n * n:
        raise ValueError("Invalid key length for the matrix")
    return [[ord(char) - ord('a') for char in key[i:i + n]] for i in range(0, len(key), n)]

def process_text(text, n):
    text = text.lower().replace(" ", "")
    while len(text) % n != 0:
        text += 'x'
    return text

def text_to_matrix(text, n):
    return [[ord(text[i + j]) - ord('a') for j in range(n)] for i in range(0, len(text), n)]

def matrix_to_text(matrix):
    text = ""
    for row in matrix:
        for num in row:
            text += chr((num % 26) + ord('a'))
    return text

def encryption(plain_text, key_str):
    n = int(len(key_str) ** 0.5)
    key_matrix = create_matrix(key_str, n)
    plain_text = process_text(plain_text, n)
    text_matrix = text_to_matrix(plain_text, n)

    result = []
    for block in text_matrix:
        encrypted = [(sum(block[k] * key_matrix[i][k] for k in range(n)) % 26) for i in range(n)]
        result.append(encrypted)
    return matrix_to_text(result)

def decryption(cipher_text, key_str):
    n = int(len(key_str) ** 0.5)
    key_matrix = np.array(create_matrix(key_str, n))
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = mod_inverse(det, 26)

    try:
        inv_matrix = (det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int)) % 26
    except LinAlgError:
        raise ValueError("Key matrix is not invertible")

    cipher_text = process_text(cipher_text, n)
    text_matrix = text_to_matrix(cipher_text, n)

    result = []
    for block in text_matrix:
        decrypted = [(sum(block[k] * inv_matrix[i][k] for k in range(n)) % 26) for i in range(n)]
        result.append(decrypted)
    return matrix_to_text(result)
