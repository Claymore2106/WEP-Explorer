import RC4


plain = ""
cipher = ""
IV = ('a03177').upper()
print('IV: %s' % IV)
current = ('02cb768980').upper()
key = '02CB778981'
print('Start: %s' % current)
combo = IV + current
print('Combo: %s' % combo)


with open('plain_simple.txt', 'r') as pfile:
    for line in pfile:
        for c in line:
            if c != '\n':
                plain += c



with open('cipher_simple.txt', 'r') as cfile:
    for line in cfile:
        for c in line:
            if c != ' ' and c != '\n':
                cipher += c


print('\nPlaintext challenge: \n%s\n' % plain)
print(len(plain))
print('\nCiphertext response: \n%s\n' % cipher)
print(len(cipher))

wait = input('Enter to start')

while current != 'FFFFFFFFFF':
    working_text = RC4.decode(combo, cipher)
    #print('Plantext: %s' % plain)
    #print('Working: %s' % working_text)
    if plain in working_text:
        print('PASSWORD FOUND! %s' % combo)
        print('Plaintext: %s' % plain)
        print('Working: %s' % working_text)
        break
    else:
        #print('Incrementing %s ' % current),
        current_int = int(current, 16)
        current_int += 1
        current = ((hex(current_int))[2:]).zfill(10)
        #print('to %s' % current)
        combo = (IV + current).upper()
        print('Incrementing to  %s' % combo)
        #wait = input('Enter to start')
