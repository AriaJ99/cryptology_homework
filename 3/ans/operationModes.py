from AES import AES


IV = 0x3243f6a8885a308d313198a2
master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
AES = AES(master_key)


def processMessage(string):
    blocks = [string[i:i + (16 if (i+16) <= len(string) else len(string)-i)] for i in range(0, len(string), 16)]
    for i in range(len(blocks)):
        blocks[i] = int('0x'+''.join(hex(ord(c))[2:] for c in blocks[i]),16)
    return blocks


def processBlocks(blocks):
    plaintext = ''
    for decrypted in blocks:
        decrypted = hex(decrypted)
        decrypted = [decrypted[i:i+2] for i in range(2,len(decrypted),2)]
        decrypted = [chr(int(c,16)) for c in decrypted]
        plaintext += ''.join(decrypted)
    return plaintext


def encryptECB(message):
    encrypted = []
    for block in message:
        encrypted.append(AES.encrypt(block))
    return encrypted


def decryptECB(message):
    decrypted = []
    for block in message:
        decrypted.append(AES.decrypt(block))
    return decrypted


def encryptCBC(message):
    encrypted = [AES.encrypt(message[0] ^ IV)]
    for i in range(1,len(message)):
        encrypted.append(AES.encrypt(message[i] ^ encrypted[i-1]))
    return encrypted


def decryptCBC(message):
    decrypted = [AES.decrypt(message[0]) ^ IV]
    for i in range(1,len(message)):
        decrypted.append(AES.decrypt(message[i]) ^ message[i-1])
    return decrypted


def encryptOFB(message):
    s = [AES.encrypt(IV)]
    encrypted = []
    for i in range(len(message)):
        encrypted.append(s[i] ^ message[i])
        s.append(AES.encrypt(s[i]))
    return encrypted


def decryptOFB(message):
    s = [AES.encrypt(IV)]
    decrypted = []
    for i in range(len(message)):
        decrypted.append(s[i] ^ message[i])
        s.append(AES.encrypt(s[i]))
    return decrypted



def encryptCFB(message):
    encrypted = [AES.encrypt(IV) ^ message[0]]
    for i in range(1,len(message)):
        encrypted.append(AES.encrypt(encrypted[i-1]) ^ message[i])
    return encrypted


def decryptCFB(message):
    decrypted = [AES.encrypt(IV) ^ message[0]]
    for i in range(1,len(message)):
        decrypted.append(AES.encrypt(message[i-1]) ^ message[i])
    return decrypted


def encryptCTR(message):
    encrypted = []
    for i in range(len(message)):
        encrypted.append(AES.encrypt(int(hex(IV)+hex(i)[2:],16)) ^ message[i])
    return encrypted


def decryptCTR(message):
    decrypted = []
    for i in range(len(message)):
        decrypted.append(AES.encrypt(int(hex(IV)+hex(i)[2:],16)) ^ message[i])
    return decrypted


string = input("please enter a text: ")

blocks = processMessage(string)

encrypted = encryptCFB(blocks)
decrypted = decryptCFB(encrypted)

plaintext = processBlocks(decrypted)

print(plaintext)
