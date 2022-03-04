def binary(n, l=8):
    return bin(n).replace('0b','').zfill(8)
def string_to_byte(s):
    ans=[]
    for i in s:
        ascii=ord(i)
        ans.append(binary(ascii))
    print(ans)
    return ans
def byte_to_string(b):
    ans=[]
    for i in b:
        ans.append(chr(int(i,2)))
    return ''.join(ans)
def find_key(plain_byte, cipher_byte, nonce):
    key=[]
    msg_len=len(plain_byte)
    for i in range(msg_len):
        k=int(plain_byte[i],2)^int(cipher_byte[i],2)
        key.append(binary((k%256-nonce)%256))
    return key
def decipher(cipher_byte, key, nonce):
    plain_byte=[]
    msg_len=len(cipher_byte)
    for i in range(msg_len):
        p=int(cipher_byte[i], 2) ^ ((int(key[i], 2)+nonce)%256)
        plain_byte.append(binary(p%256))
    return plain_byte
Alex_plaintext="BARACKOBAMA"
Alex_cipherbyte="0100001100011011000100100011000011111000101001111000111011101001000101000001110101100100"
Alex_cipherbyte=[Alex_cipherbyte[0+i:8+i] for i in range(0,len(Alex_cipherbyte),8)]
Alex_plainbyte=string_to_byte(Alex_plaintext)
Alex_ciphertext=byte_to_string(Alex_cipherbyte)
Blake_cipherbyte="0100011000010100000011110011001111110000101010011001011011111110000000110001110001110110"
Blake_cipherbyte=[Blake_cipherbyte[0+i:8+i] for i in range(0,len(Blake_cipherbyte),8)]
key=find_key(Alex_plainbyte,Alex_cipherbyte,1)
Blake_ciphertext=byte_to_string(Blake_cipherbyte)
Blake_plainbyte=decipher(Blake_cipherbyte, key, 2)
Blake_plaintext=byte_to_string(Blake_plainbyte)
print("Alex messages :")
print(f"\tAlex plain text : {Alex_plaintext} -> {Alex_plainbyte}")
print(f"\tAlex cipher text : {Alex_ciphertext} -> {Alex_cipherbyte}")
print("key :\n\t",f"{byte_to_string(key)} -> {key}")
print("Blake messages :")
print(f"\tBlake cipher text : {Blake_ciphertext} -> {Blake_cipherbyte}")
print(f"\tBlake plain text : {Blake_plaintext} -> {Blake_plainbyte}")
star='*'*10
print(f"FINAL ANSWER :\n\t{star}{Blake_plaintext}{star}")
#Alex_ciphertext=list(map(int,list(Alex_ciphertext)))
#print(Alex_ciphertext)
#print(string_to_byte(Alex_plaintext))