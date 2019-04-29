
# String Methods
# Strings and tuples are immutable sequence types
# https://docs.python.org/2.7/library/stdtypes.html#string-methods

stringval = "print"

# Capitalize
print stringval.capitalize()

# Center
print stringval.center(25)
print stringval.center(25, "*")

# Count
print stringval.count("i")
print stringval.count("p", 0, len(stringval))
print stringval.count("p", 1, len(stringval))

# Decode
# print stringval.decode()

# Encode
# print stringval.encode()

# Ends With
print stringval.endswith("nt")
print stringval.endswith("kt")

# Expand Tabs
print '01\t012\t0123\t01234'.expandtabs()
print '01\t012\t0123\t01234'.expandtabs(1)
print '01\t012\t0123\t01234'.expandtabs(2)
print '01\t012\t0123\t01234'.expandtabs(3)
print '01\t012\t0123\t01234'.expandtabs(4)
print '01\t012\t0123\t01234'.expandtabs(5)

# Find
print "pr" in stringval
print "pi" in stringval

# Format
print "Hello Programmer {}".format("Boo!")
print "Hello Programmer {0}".format("Boo!")
print "Hello {1} Programmer {0}".format("Boo!", "New")
print "Hello {prg} Programmer {0}".format("Boo!", prg="Buddy")
print "Hello {prg!r} Programmer {0!s}".format(25.5, prg="Buddy")
# "Weight in tons {0.weight}"       # 'weight' attribute of first positional arg

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print 'Coordinates: {latitude}, {longitude}'.format(**coord)

# **Alignment**
print '{:<30}'.format('left aligned')
print '{:>30}'.format('right aligned')
print '{:^30}'.format('centered')
print '{:*^30}'.format('centered')

print "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
print "int: {0:#d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
print '{:,}'.format(1234567890)


points = 19.5
total = 22
print 'Correct answers: {:.2%}'.format(points/total)
print 'Correct answers: {:.4%}'.format(points/total)
print 'Correct answers: {:.10%}'.format(points/total)
print 'Correct answers: {:.30%}'.format(points/total)

# Index
print stringval.index("i")

# is's
print stringval.isalnum()
print stringval.isalpha()
print stringval.isdigit()
print stringval.islower()
new_stringval = "   "
print new_stringval.isspace()
print stringval.istitle()
print stringval.capitalize().istitle()
print stringval.isupper()

# Join
print "-".join("NewWorld")
print str(range(5))
print "-".join(str(range(5)))

# ljust & rjust
print stringval.ljust(50, "*")
print stringval.rjust(50, "*")

# lstrip & rstrip
print stringval.lstrip("rip")
print stringval.lstrip("pri")
print '   spacious   '.lstrip()
print '   spacious   '.rstrip()
print 'www.example.com'.lstrip('cmowz.')
print 'www.example.com'.rstrip('cmowz.')

# Lower & Upper
print stringval.lower()
print stringval.upper()

# Partition & rpartition
print stringval.partition(",")
print "1,2,3".partition(",")
print "1,2,3".rpartition(",")

# Replace
print stringval.replace("pr", "h")
song = 'Let it be, let it be, let it be, let it be'
print song.replace("let", "don't let", 2)

# rfind & rindex
quote = 'Do small things with great things love'
print quote.find("things")
print quote.rfind("things")
print quote.rindex("things")
# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))
# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2))
# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))
# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))

# rsplit & split
# Ref: https://stackoverflow.com/questions/27493703/typeerror-split-takes-no-keyword-arguments-in-python-2-x
print song.split()
print song.split(",")
print song.split(",", 2)
print song.rsplit(",", 2)

# splitlines
print 'ab c\n\nde fg\rkl\r\n'.splitlines()
print 'ab c\n\nde fg\rkl\r\n'.splitlines(True)
print 'Two lines\n'.split('\n')

# Startswith
print song.startswith("Let")
print song.startswith("let")

# swap case
print song.swapcase()
print song.upper().swapcase()

# title
print stringval.title()
print song.title()
print "they're bill's friends from the UK".title()

'''
import re
def titlecase(s):
     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)

titlecase("they're bill's friends.")
"They're Bill's Friends."
'''

# translate
from string import maketrans
firstString = "abc"
secondString = "ghi"
thirdString = "ab"
string = "abcdef"
print("Original string:", string)
translation = maketrans(firstString, secondString)
print translation
translation = maketrans(secondString, firstString)
print translation
print 'read this short text'.translate(None, 'aeiou')
print 'read this short text'.translate(translation, 'aeiou')

# zfill
print stringval.zfill(3)
print stringval.zfill(30)

print '%(language)s has %(number)03d quote types.' % {"language": "Python", "number": 2}
print '%(language)s has %(number)#3d quote types.' % {"language": "Python", "number": 2}
print '%(language)s has %(number)-3d quote types.' % {"language": "Python", "number": 2}
print '%(language)s has %(number) 3d quote types.' % {"language": "Python", "number": 2}
print '%(language)s has %(number)+3d quote types.' % {"language": "Python", "number": 2}
print '%(language)s has %(number)#5x quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)#5X quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)05e quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)05E quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)#2f quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)04F quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)F quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)03g quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)03G quote types.' % {"language": "Python", "number": 10}
# Refer ASCII Table https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjWqJqYofThAhWHA3IKHdf0Dx
# AQjRx6BAgBEAU&url=https%3A%2F%2Fsimple.wikipedia.org%2Fwiki%2FASCII&psig=AOvVaw2-kYuac2Ayo8eSdZSeTXAr&ust=1556591456736092
print '%(language)s has %(number)03c quote types.' % {"language": "Python", "number": 36}
print '%(language)s has %(number)03i quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)03o quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)03r quote types.' % {"language": "Python", "number": 10}
print '%(language)s has %(number)03s quote types.' % {"language": "Python", "number": 10}

value = xrange(25)
# value[1] = 30 => TypeError: 'xrange' object does not support item assignment
print value


# """
# Result:
#
# C:\Python27\python.exe C:/Work/Python/quickref/stringmethods.py
# Print
#           print
# **********print**********
# 1
# 1
# 0
# True
# False
# 01      012     0123    01234
# 01 012 0123 01234
# 01  012 0123  01234
# 01 012   0123  01234
# 01  012 0123    01234
# 01   012  0123 01234
# True
# False
# Hello Programmer Boo!
# Hello Programmer Boo!
# Hello New Programmer Boo!
# Hello Buddy Programmer Boo!
# Hello 'Buddy' Programmer 25.5
# Coordinates: 37.24N, -115.81W
# left aligned
#                  right aligned
#            centered
# ***********centered***********
# int: 42;  hex: 2a;  oct: 52;  bin: 101010
# int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
# 1,234,567,890
# Correct answers: 88.64%
# Correct answers: 88.6364%
# Correct answers: 88.6363636364%
# Correct answers: 88.636363636363640239324013236910%
# 2
# True
# True
# False
# True
# True
# False
# True
# False
# N-e-w-W-o-r-l-d
# [0, 1, 2, 3, 4]
# [-0-,- -1-,- -2-,- -3-,- -4-]
# print*********************************************
# *********************************************print
# nt
# nt
# spacious
#    spacious
# example.com
# www.example
# print
# PRINT
# ('print', '', '')
# ('1', ',', '2,3')
# ('1,2', ',', '3')
# hint
# Let it be, don't let it be, don't let it be, let it be
# 9
# 27
# 27
# 27
# 27
# -1
# 18
# ['Let', 'it', 'be,', 'let', 'it', 'be,', 'let', 'it', 'be,', 'let', 'it', 'be']
# ['Let it be', ' let it be', ' let it be', ' let it be']
# ['Let it be', ' let it be', ' let it be, let it be']
# ['Let it be, let it be', ' let it be', ' let it be']
# ['ab c', '', 'de fg', 'kl']
# ['ab c\n', '\n', 'de fg\r', 'kl\r\n']
# ['Two lines', '']
# True
# False
# lET IT BE, LET IT BE, LET IT BE, LET IT BE
# let it be, let it be, let it be, let it be
# Print
# Let It Be, Let It Be, Let It Be, Let It Be
# They'Re Bill'S Friends From The Uk
# ('Original string:', 'abcdef')
#  
#  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`ghidefghijklmnopqrstuvwxyz{|}~��������������������������������������������������������������������������������������������������������������������������������
#  
#  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefabcjklmnopqrstuvwxyz{|}~��������������������������������������������������������������������������������������������������������������������������������
# rd ths shrt txt
# rd tbs sbrt txt
# print
# 0000000000000000000000000print
# Python has 002 quote types.
# Python has   2 quote types.
# Python has 2   quote types.
# Python has   2 quote types.
# Python has  +2 quote types.
# Python has   0xa quote types.
# Python has   0XA quote types.
# Python has 1.000000e+01 quote types.
# Python has 1.000000E+01 quote types.
# Python has 10.000000 quote types.
# Python has 10.000000 quote types.
# Python has 10.000000 quote types.
# Python has 010 quote types.
# Python has 010 quote types.
# Python has   $ quote types.
# Python has 010 quote types.
# Python has 012 quote types.
# Python has  10 quote types.
# Python has  10 quote types.
# xrange(25)
#
# Process finished with exit code 0
#
# """