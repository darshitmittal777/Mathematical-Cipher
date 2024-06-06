def convert_char(c,k):
    k = k % 26
    if(c>='A' and c<='Z'):
        if ord(c)+k>ord('Z'):
            c = chr(ord(c) - 26)
        c = chr(ord(c) + k)  
    if(c>='a' and c<='z'):
        if ord(c)+k>ord('z'):
            c = chr(ord(c) - 26)
        c = chr(ord(c) + k)  
    return c    

def enc(m,k):
    s=""
    for i in m:
        s = s + convert_char(i,k)
    return s

word = "iitk is better than iitd and iitb"
key = 9
print(enc(word,key))

word = "lets learn cryptography"
key = 25
print(enc(word,key))