from KDF import wepkey64

def callwep():
    passphrase = input('Passphrase: ')
    keys = wepkey64(passphrase)
    i = 0
    while i <= 3:
        print('Key %s is: %s' % (str(i + 1), keys[i]))
        i += 1


callwep()
