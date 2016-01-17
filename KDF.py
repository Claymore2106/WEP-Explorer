def wepkey64(val):
    pseed = [0, 0, 0, 0]
    randNumber = 0
    k64 = ["", "", "", ""]
    i = 0
    j = 0
    tmp = 0
    while i < len(val):
        pseed[i % 4] ^= ord(val[i])
        i += 1

    randNumber = pseed[0] | (pseed[1] << 8) | (pseed[2] << 16) | (pseed[3] << 32)

    i = 0
    while i < 4:
        j = 0
        while j < 5:
            randNumber = (randNumber * 0x343fd + 0x269ec3) & 0xffffffff
            tmp = (randNumber >> 16) & 0xff
            s = str(hex(tmp)[2:])  # Remove the \0x: 5d
            s = s.zfill(2)
            k64[i] += s.upper()
            j += 1
        i += 1

    return k64
