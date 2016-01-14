import binascii

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def build_binary(string):
    b = ''
    for c in string:
        a = ''.join('{:08b}'.format(ord(c)))
        b += a
    return b


def build_list(string):
    b_list = []
    for c in string:
        b_list.append(ord(c))
    return b_list


def KSA(key):
    #bkey = build_binary(key)
    b_list = build_list(key)
    keylength = len(b_list)

    s = []
    j = 0

    print('\nKey is: %s' % key)
    #print('Binary is: %s' % bkey)
    print('B_list is: %s' % str(b_list))
    print('Key length is: %s' % str(keylength))

    # Initialize a sorted table from numbers 0 to 255
    for i in range(0,256):
        s.append(i)
    #print("\nSorted table is: \n%s" % str(s))

    # Mess up the sorted table, based on the secret key
    for i in range(0,256):
        j = (j + s[i] + int(b_list[i % keylength])) % 256
        s[i], s[j] = s[j], s[i]

    #print('\nTable should be rearranged: \n%s\n' % str(s))
    return s


def PRGA(table, text):
    i = 0
    j = 0
    s = table
    newtext = ''

    if is_hex(text): # Check to see if string is already encrypted, and if true
                     # decrypt it.
        h = binascii.unhexlify(text)
        print("Hex string is: %s" % h)
        for c in h:
            print("Working with: %s" % str(c))
            numerical = int(c)


            i = i + 1
            print('S[i] is: %s' % str(s[i]))
            j = (j + int(s[i])) % 256
            print('S[j] is: %s' % str(s[j]))
            s[i], s[j] = s[j], s[i]


            index = (s[i] + s[j]) % 256
            print('Index is: %s' % str(index))

            element = s[index]
            print('Element is: %s' % str(element))

            b = bin(numerical ^ element)
            print('Binary XOR is: %s' % str(b))

            character = chr(int(b, 2))
            print('Character is: %s\n' % character)

            newtext += character

        print(newtext)


    else:

        for c in text:
            print('C is: %s' % c)

            unic = ord(c)
            print('Unicode is: %s' % str(unic))

            i = i + 1
            j = (j + int(s[i])) % 256
            s[i], s[j] = s[j], s[i]

            index = (s[i] + s[j]) % 256
            print('Index is: %s' % str(index))

            element = s[index]
            print('Element is: %s' % str(element))

            bu = bin(unic)
            print('Binary of unicode is: %s' % str(bu))

            be = bin(element)
            print('Binary of element is: %s' % str(be))

            b = bin(unic ^ element)
            print('Binary XOR is: %s' % str(b))

            d = int(b, 2)
            print('Int of XOR is: %s' % str(d))

            a = chr(d)
            print('ASCII of int is: %s' % a.encode('utf-8'))

            h = hex(int(b,2))
            print('Hex of ASCII is: %s' % str(h))
            print("Without 'b': %s" % str(h)[2:])

            pretty = str(h)[2:]

            newtext += pretty

        print('Plaintext: %s' % text)
        print('Encrypted: %s' % newtext)



def RC4():
    key = 'Nicholas' # input("Enter a secret key: ")
    text = "9df8b166" # 9df8b166
    table = KSA(key)
    PRGA(table, text)

RC4()
