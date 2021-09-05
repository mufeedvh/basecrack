# THE BEERWARE LICENSE (Revision 42):
# <thenoviceoof> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you
# think this stuff is worth it, you can buy me a beer in return
# - Nathan Hwang (thenoviceoof)
#
# Modified from: https://github.com/thenoviceoof/base92/blob/master/python/base92/base92.py

import math

def base92_ord(val):
    num = ord(val)
    if val == '!':
        return 0
    elif ord('#') <= num and num <= ord('_'):
        return num - ord('#') + 1
    elif ord('a') <= num and num <= ord('}'):
        return num - ord('a') + 62
    else:
        raise ValueError('val is not a base92 character')

def base92_decode(bstr):
    bitstr = ''
    resstr = ''
    if bstr == '~':
        return ''
    # we always have pairs of characters
    for i in range(len(bstr) // 2):
        x = base92_ord(bstr[2*i])*91 + base92_ord(bstr[2*i+1])
        bitstr += '{:013b}'.format(x)
        while 8 <= len(bitstr):
            resstr += chr(int(bitstr[0:8], 2))
            bitstr = bitstr[8:]
    # if we have an extra char, check for extras
    if len(bstr) % 2 == 1:
        x = base92_ord(bstr[-1])
        bitstr += '{:06b}'.format(x)
        while 8 <= len(bitstr):
            resstr += chr(int(bitstr[0:8], 2))
            bitstr = bitstr[8:]
    return resstr

decode = base92_decode
b92decode = base92_decode