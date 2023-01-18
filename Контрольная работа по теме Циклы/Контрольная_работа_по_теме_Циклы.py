from random import *
from math import *
from re import U

3
print("1")
print()

try:
    n=int(input("vali 1-9 palju tahad näha kuuske? "))
    if n<1 or n>9:
        print("vale vahemik")
except:
    print("vale andmetüüp")
x=0
for x in range(4):
    for e in range(n):
        if x==0:
            print(" ----- ", end="")
        elif x ==1:
            print("|  O  |", end="")
        elif x==2:
            print("!  -  !", end="")
        elif x==3:
            print(" ----- ", end="")
    print("")


print()
print("2")
print()

try:
    nch=int(input("sista arv> "))
    st=int(input("sisesta arvu aste> "))
    nch1 =stn= 1
    while stn<nch:
        stn=nch1**st
        if stn>nch:
            break
        print(nch1,"^",st,"=",stn)
        nch1 +=1
except:
    print("vale andmetüüp")

print()
print("3")
print()

print("füüsika hinded")
u=randint(1,30)
nomer=1
suma=0
for i in range (u):
    o=randint(2,5)
    print(nomer,"->",o)
    nomer +=1
    suma +=o
nome=nomer-1
kesk=suma/nome
print("keskmine on:", kesk)

print()
print("4")
print()
