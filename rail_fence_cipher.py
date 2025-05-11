# File 1: rail_fence_cipher.py

def encryption(text, key):
    if key <= 1:
        return text

    # Create a list of empty strings for each rail
    rail = ['' for _ in range(key)]
    direction_down = False
    row = 0

    # Traverse through the input text and assign characters to rails
    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    # Join the characters from all rails to form the encrypted text
    return ''.join(rail)


def decryption(cipher, key):
    if key <= 1:
        return cipher

    # Create the rail structure
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    # Fill the rail matrix with '*' to mark the zigzag pattern
    direction_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    # Now, fill the '*' positions with cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Reconstruct the original text from the rail matrix
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        result.append(rail[row][col])
        col += 1
        row += 1 if direction_down else -1

    return ''.join(result)
