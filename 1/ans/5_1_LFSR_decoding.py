import string
def binary(num,length=5):
    return bin(num).replace("0b","").zfill(length)
def str_map_initialization():
    lower = zip(string.ascii_lowercase, range(26))
    upper = zip(string.ascii_uppercase, range(26))
    digit = zip(string.digits, range(26, 32))
    return  {**dict(lower) , **dict(upper),  **dict(digit)}
def num_map_initialization():
    upper = zip(range(26), string.ascii_uppercase)
    digit = zip(range(26, 32), string.digits)
    return {**dict(upper), **dict(digit)}
def test_equations(coef,key_stream,LFSR_size):
    #print("coefficient :",coef)
    #print("key stream :",key_stream)
    for i in range(LFSR_size):
        sum=0
        #print(key_stream[i+LFSR_size],":")
        for j in range(LFSR_size):
            #print(key_stream[j+i]*coef[j],end="+")
            sum ^= key_stream[j+i]*coef[j]
        #print("=",sum)
        if sum != key_stream[i+LFSR_size]:
            return False
    return True
def solve_equation(key_stream, LFSR_size):
    #this function solves N equation N unknowns by bruteforce
    for i in range(64):
        bit_mask=list(map(int,binary(i,6)))
        if test_equations(bit_mask,key_stream,LFSR_size)== True:
            ans=bit_mask
    #print(ans)
    return ans

def find_coef(ciphered_text, sample_text,LFSR_size):
    a_stream=[]
    b_stream=[]
    for i in ciphered_text:
        a_stream.extend(list(map(int,binary(str_map[i]))))
    for i in sample_text:
        b_stream.extend(list(map(int,binary(str_map[i]))))
    # print(a_stream)
    # print(b_stream)
    key_stream=[a_stream[i] ^ b_stream[i] for i in range(2*LFSR_size+1)]
    # print(key_stream)
    return [solve_equation(key_stream, LFSR_size), key_stream]
def decode_LFSR(ciphered_text, LFSR_coef, initial_key):
    key_len=len(ciphered_text)*5
    #print(initial_key)
    key=list(map(int,initial_key))
    for i in range(key_len):
        sum=0
        for j in range(len(LFSR_coef)):
            sum^=LFSR_coef[j]*key[j+i]
        key.append(sum)
    #print(key)
    deciphered_text=[]
    for c in range(len(ciphered_text)):
        bin_form=list(map(int,binary(str_map[ciphered_text[c]])))

        sum=[]
        bit_len=len(bin_form)
        #print(bin_form)
        for j in range(bit_len):
            sum.append(bin_form[j]^key[c*bit_len+j])
        #print(int(''.join(list(map(str, sum))), 2))
        #print(num_map[int(''.join(list(map(str, sum))), 2)])
        deciphered_text.append(num_map[int(''.join(map(str,sum)),2)])
    #print(deciphered_text)
    return ''.join(deciphered_text)
ciphered_text = "j5a0edj2b"
sample_prefix = "WPI"
LFSR_size = 6

str_map = str_map_initialization()
num_map = num_map_initialization()
[LFSR_coef, key] = find_coef(ciphered_text, sample_prefix, LFSR_size)

deciphered_text = decode_LFSR(ciphered_text, LFSR_coef, key[:LFSR_size])
print(f"ciphered text : {ciphered_text}")
print(f"deciphered text : {deciphered_text}")
print(f"initialization vector : {key[:LFSR_size]}")
print(f"feedback coefficients of LFSR : {LFSR_coef}")






