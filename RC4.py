# Please be aware that while functional, this script is intended for educational
# use as a visual aid, and is not designed for further implementation.


import string
import binascii


def KSA(key):
    table = []
    j = 0

    for i in range(256):  # Initialize a sorted table from numbers 0 to 255
        table.append(i)
    # Mess up the sorted table, based on the secret key
    for i in range(256):
        j = (j + table[i] + ord(key[i % len(key)])) % 256
        table[i], table[j] = table[j], table[i]
    return table


def PRGA(table):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + table[i]) % 256
        table[i], table[j] = table[j], table[i]
        yield table[(table[i] + table[j]) % 256]


def encode(key, text):
    newtext = []
    randomized = KSA(key)
    keystream = PRGA(randomized)
    encrypted = ''

    for c in text:
        unic = ord(c)  # Get an int value
        h = hex(unic ^ next(keystream)) # Get a hex value: \0x5d
        s = str(h[2:])  # Remove the \0x: 5d
        s = s.zfill(2)  # Ensure there are always two digits, nothing like '6'
        newtext.append(s)
    for i in newtext:
        encrypted += str(i)
    return encrypted


def decode(key, text):
    h = binascii.unhexlify(text)
    randomized = KSA(key)
    keystream = PRGA(randomized)
    decrypted = ''
    for i in h:
        n = int(i)  # Get the numerical value for the hex character
        a = n ^ next(keystream)  # Get the unencrypted numerical value from table
        c = chr(a)  # Get the ASCII value for that number
        decrypted += c
    return decrypted


def RC4(key, text):
    if all(c in string.hexdigits for c in text):
        return decode(key, text)
    else:
        return encode(key, text)
