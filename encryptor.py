# !/usr/bin/python
# -*- coding: UTF-8 -*-

import random


print("\nType 'random__' to use a random passcode.\n")
pswF = input('Passcode:')
txt = input('Text:').lower()
if pswF == 'random__':
    def shuffle_str(str_in=''):
        lF = list(str_in)
        random.shuffle(lF)
        return ''.join(lF)
    psw = shuffle_str('abcdefghijklmnopqrstuvwxyz').upper()
else:
    psw = str(pswF.upper())
    pass


a = psw[0:1]
pTxt = txt.replace('a', a)

b = psw[1:2]
pTxt = pTxt.replace('b', b)

c = psw[2:3]
pTxt = pTxt.replace('c', c)

d = psw[3:4]
pTxt = pTxt.replace('d', d)

e = psw[4:5]
pTxt = pTxt.replace('e', e)

f = psw[5:6]
pTxt = pTxt.replace('f', f)

g = psw[6:7]
pTxt = pTxt.replace('g', g)

h = psw[7:8]
pTxt = pTxt.replace('h', h)

i = psw[8:9]
pTxt = pTxt.replace('i', i)

j = psw[9:10]
pTxt = pTxt.replace('j', j)

k = psw[10:11]
pTxt = pTxt.replace('k', k)

l = psw[11:12]
pTxt = pTxt.replace('l', l)

m = psw[12:13]
pTxt = pTxt.replace('m', m)

n = psw[13:14]
pTxt = pTxt.replace('n', n)

o = psw[14:15]
pTxt = pTxt.replace('o', o)

p = psw[15:16]
pTxt = pTxt.replace('p', p)

q = psw[16:17]
pTxt = pTxt.replace('q', q)

r = psw[17:18]
pTxt = pTxt.replace('r', r)

s = psw[18:19]
pTxt = pTxt.replace('s', s)

t = psw[19:20]
pTxt = pTxt.replace('t', t)

u = psw[20:21]
pTxt = pTxt.replace('u', u)

v = psw[21:22]
pTxt = pTxt.replace('v', v)

w = psw[22:23]
pTxt = pTxt.replace('w', w)

x = psw[23:24]
pTxt = pTxt.replace('x', x)

y = psw[24:25]
pTxt = pTxt.replace('y', y)

z = psw[25:26]
pTxt = pTxt.replace('z', z)


print('Text:', pTxt)
print('Passcode:', psw)
