S=input("Dati un sir de caractere:")
#a
a=S.count('A')
print("S1:",a)
#b
for i in S:
    b=S.replace('A','*')
print("S2:",b)
#c
for i in S:
    c=S.replace('B',' ')
print("S3:",c)
#d
for i in S:
    d=S.count('MA')
print("S4:",d)
#e
for i in S:
    e=S.replace('MA','TA')
print("S5:",e)
#f
for i in S:
    f=S.replace('TO',' ')
print("S6:",f)
#g
print(S[::-1])













