#!/usr/bin/python

str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str2=""
for i in str:
    if i == 'z':
        shift = 'b'
    elif i == 'y':
        shift = 'a'
    elif i == ' ':
        shift = ' '
    else:
        shift=chr(ord(i) + 2)
    str2 = str2+shift
print str2

