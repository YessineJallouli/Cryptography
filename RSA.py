# Created by Yessine Jallouli on 04/06/2021

import sys
sys.setrecursionlimit(30000)

def modpow(x,y,mod):
    res = 1 
    while (y > 0): 
        if ((y & 1) == 1) :
            res = (res * x)%mod
        y = y >> 1
        x = (x*x)%mod
    return res

def encrypt(message,e,p,q):
    N = p*q
    return modpow(message,e,N)

def totient(p,q):
    if (q == 1):
        return p-1
    if (p == 1):
        return q-1
    if (p != q):
        return (p-1)*(q-1)
    return p*(q-1)

def egcd(a, b):
    if a > b:
        (d,u,v)=egcd(b,a)
        return (d,v,u)
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, b):
    g, x, y = egcd(a, b)
    if g != 1:
        raise Exception('modular inverse does not exist HAHA')
    else:
        return x % b

def D(e,p,q):
    t = totient(p,q)
    return modinv(e,t)

def getflag(p,q,e,c):
    d = D(e,p,q)
    return modpow(c,d,p*q)

# Use this website to factorize n : https://www.alpertron.com.ar/ECM.HTM  
# n = 7752877946543889667452302816935592041521406241414271580931166592905268802228007384229404499407368534620247986055680055619254524154753257932445198009253639  
p = 109636408366051089507726074917187620871951271410941442600902714861162203610229                                                                  
q = 70714446615751853524975059928936129095522509001149987806362427997074833313291
e = 65537
c = 6322844174478556595176378455164506094747408112775417089534651683708493287375345348695673641350391222150589722977130055528309584536384504193600369023182500

flag = getflag(p,q,e,c)

flag = str(hex(flag))

print(flag)
