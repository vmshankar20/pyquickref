
# Sequence Types : str, unicode, list, tuple, bytearray, buffer, xrange
# https://docs.python.org/2.7/library/stdtypes.html#typesseq

from sys import getsizeof
l = "Hello"
print getsizeof(l)
bk = bytearray(l)
print getsizeof(bk)
bk = buffer(l)
print getsizeof(bk)


'''
Result:
26
30
32
'''