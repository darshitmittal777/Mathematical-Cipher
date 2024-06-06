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

def print_possibilities(s):
    i = 0
    while i<26:
        print(enc(s,i))
        i = i + 1

word = "bm ptl wtfg xtlr tztbg"
print(print_possibilities(word))
#it was damn easy again

word = "rc fjb mjvw njbh"
print(print_possibilities(word))
#it was damn easy