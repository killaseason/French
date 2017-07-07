import re

cik='1452922'


a='000094787117000444xxxxkjjx000094787117000096'

#fileName1=re.compile(r'[0-9]{10}-[0-9]{2}-[0-9]{6}')
fileName1=re.compile(r'([0-9]{10})([0-9]{2})([0-9]{6})')
b=fileName1.findall(a)

for name in b[0:1]:
    print name[0]+'-'+name[1]+'-'+name[2]
print b
