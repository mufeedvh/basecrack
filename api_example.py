# import the BaseCrack class from basecrack.py
from basecrack import BaseCrack

# calling the api function decode() with the encoded base
result = BaseCrack().decode('c3BhZ2hldHRp')

# printing the output
"""
result is tuple where:
result[0] = DECODED STRING
result[1] = ENCODING SCHEME
"""
print('Decoded String: {}'.format(result[0]))
print('Encoding Scheme: {}'.format(result[1]))
