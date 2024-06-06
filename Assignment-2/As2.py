text = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"
def octa(a):
    if(a>='0'and a<='9'):
        return int(a)
    else:
        return ord(a)-55


List = [0] * 256
List2 =[]
for i in range(0, len(text) - 1, 2):
    letter = octa(text[i]) * 16 + octa(text[i + 1])
    List[letter] = List[letter] + 1
    List2.append(letter)

prob = []
for i in range(1, 15):
    k = 0
    p = 0
    c = 0
    while k < 256:
        p += List[k] * List[k]
        k += i
        c += 1
    p = p / (c * c)
    prob.append(p)

print(prob)

#possible -> 7,9
List_poss = []
z = 7
for i in range(0,z):
    List_temp = []
    k=i
    for j in range(0,256):
        f=1
        k=i
        while k < len(List2):
            if (List2[k]^j)<32 or (List2[k]^j)>127:
                f=0
                break
            k = k +z;
        if f>0:
            List_temp.append(j)
    List_poss.append(List_temp)

#confirm 7

eprob = [0.082,0.015,0.028,0.043,0.127,0.022,0.02,0.061,0.07,0.002,0.008,0.04,0.024,0.067,0.015,0.019,0.001,0.06,0.063,0.091,0.028,0.01,0.024,0.002,0.02,0.001]
prob_max =[]
prob_m =[]
for j in range(len(List_poss)):
    prob_max.append(0)
    prob_m.append(0)
    for i in range(0,len(List_poss[j])):
        lct=0
        prob=[0]*26
        y=j
        while(y<len(List2)):
            if(List_poss[j][i]^List2[y]>=97 and List_poss[j][i]^List2[y]<=122):
                lct = lct+1;
                prob[(List_poss[j][i]^List2[y])-97] = prob[(List_poss[j][i]^List2[y])-97] + 1
            y = y + z;
        prob_cur=0
        for k in range (0,26):
            prob_cur = prob[k]*eprob[k] + prob_cur
        if(prob_max[j]<prob_cur):
            prob_max[j] = prob_cur
            prob_m[j] = List_poss[j][i]

print(prob_m)
for i in range(0, len(List2)):
    print(chr(prob_m[i%7]^List2[i]),end="")