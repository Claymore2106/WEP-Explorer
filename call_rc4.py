from RC4 import RC4

def call_RC4():
        key = input("Enter a secret key: ")
        text = input("Text to encrypt or hex to decrypt: ")
        text = RC4(key, text)
        print(text)

call_RC4()
