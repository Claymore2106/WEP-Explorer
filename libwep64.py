import KDF
import RC4
import random


def set_passphrase():
    passphrase = input('Enter a 5 charcter passphrase: ')
    while len(passphrase) != 5:
        passphrase = input('Passphrase must be 5 characters! ')

    keys = KDF.wepkey64(passphrase)
    return passphrase, keys


def get_index(keys):
    i = 1
    print('Keys are: ')
    for key in keys:
        print('%i: %s' % (i, key))
        i += 1

    key_index = int(input('Index to use (1-4): '))
    key_index = keys[key_index - 1]
    return key_index


def gen_iv():
    IV = int(random.uniform(0, 16777215))
    return IV


def WEP64():
    passphrase, keys = set_passphrase()
    index = get_index(keys)
    IV = 'a03177'.upper()
    # IV = gen_iv()
    #hex_IV = hex(IV)
    #shex_IV = (hex_IV[2:]).zfill(6)
    shex_IV = IV
    key = (shex_IV + index).upper()
    text = ''
    print('Hex IV is: 0x%s' % shex_IV)
    print('Working key is: %s' % key)

    text = input('Text to encrypt or decrypt: ')
    choice = input('Should text be encrypted? (y/n): ')
    if choice == 'y':
        text = RC4.encode(key, text)
    elif choice == 'n':
        text = RC4.decode(key, text)

    print('Changed text:\n%s' % text)
