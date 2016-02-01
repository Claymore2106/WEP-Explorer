from libwep64 import gen_iv


i = 0
while i < 10:
    IV = gen_iv()
    hex_IV = hex(IV)
    shex_IV = (hex_IV[2:]).zfill(6)
    # hex_IV = hex_IV.zfill(6)
    print('0x' + shex_IV)
    i += 1
