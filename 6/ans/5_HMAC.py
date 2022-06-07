from os import TMP_MAX

def Hash(text,IV):
    #the function which takes a text and IV in string form as input
    #and returns output of SHA256 algorithm in string form
    pass
def key_adjust(key,b):
    
    if len(key)>b:
        key=key[:b]
    elif len(key)<b:
        key=(b-len(key))*'0'+key
    return key
#print(key_adjust(key,b))
def XOR(a,b):
    ans=''
    print(len(a))
    for i in range(len(a)):
        tmp=''
        if a[i]==b[i]:
            tmp='0'
        else:
            tmp='1'
        ans+=tmp 
    print(ans)
    return ans
b=32#blocks lenght
IV=""
ipad='00110110'
opad='01011100'
key=input("pleas enter the key(preferably 32-bit) : ")
text=input("please enter the input text : ")
#padding the test
while len(text)%b>0:
    text+='0'
k_ipad=''
k_opad=''
key=key_adjust(key,b)
for i in range(b//8):
    k_ipad+=XOR(key[i:i+8],ipad)
for i in range(b//8):
    k_opad+=XOR(key[i:i+8],opad)
#print(k_ipad,k_opad)
H_s_x=Hash(k_ipad,IV)#h(s||x)
for i in range(len(text)//b):
    H_s_x+=Hash(text[i:i+b],IV)
output=Hash(k_opad,IV)
for i in range(len(text)//b):
    output+=Hash(H_s_x[i:i+b],IV)
print(output)