import math

def encryption(plain_text, key):
    key = str(key)
    num_cols = len(key)
    num_rows = math.ceil(len(plain_text) / num_cols)
    padding = num_cols * num_rows - len(plain_text)
    plain_text += '_' * padding  # use underscore as padding

    # Create matrix row-wise
    matrix = [plain_text[i:i+num_cols] for i in range(0, len(plain_text), num_cols)]

    # Determine order of columns by sorted key
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])

    # Read matrix column-wise based on key order
    cipher_text = ''
    for idx, _ in key_order:
        for row in matrix:
            cipher_text += row[idx]

    return cipher_text

def decryption(cipher_text, key):
    key = str(key)
    num_cols = len(key)
    num_rows = math.ceil(len(cipher_text) / num_cols)

    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    col_lengths = [num_rows] * num_cols

    total_chars = len(cipher_text)
    matrix = ['' for _ in range(num_cols)]

    index = 0
    for idx, _ in key_order:
        matrix[idx] = cipher_text[index:index+col_lengths[idx]]
        index += col_lengths[idx]

    # Rebuild the plain text row-wise
    plain_text = ''
    for i in range(num_rows):
        for j in range(num_cols):
            if i < len(matrix[j]):
                plain_text += matrix[j][i]

    return plain_text.rstrip('_')  # remove padding
