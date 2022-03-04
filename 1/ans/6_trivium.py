key = [0 for i in range(80)]
IV = [0 for i in range(80)]
s1 = [*key[3:], *[0 for i in range(93-78+1)]]
s2 = [*IV, *[0 for i in range((177-94+1)-80)]]
s3 = [0 for i in range(178, 289)]
s3[-3:]=[1, 1, 1]
s = [*s1, *s2, *s3]
# print(s3)
# print(len(s3))
# print(len(s2))
# print(len(s1))
for i in range(288):
    #trivium algorithm warm up phase
    t1 = s[65]+s[92]
    t2 = s[161]+s[176]
    t3 = s[242]+s[287]
    z = t1+t2+t3
    t1 = t1+s[90] & s[91]+s[170]
    t2 = t2+s[174]&s[175]+s[263]
    t3 = t3+s[285]&s[286]+s[68]
    s1 = [t3, *s1[:-1]]
    s2 = [t1, *s2[:-1]]
    s3 = [t2, *s3[:-1]]
    # s1[0]=t3
    # s2[0]=t1
    # s3[0]=t2
    s = [*s1, *s2, *s3]
    print(f"output(z) : {z} (output isn't valid during warm up phase")
    print(f"s[0:70] after {i+1}th rotation :\n{s[:70]}")