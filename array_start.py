from array import *
vals = array('i',[21,22,23])
for i in vals:
    print(i)
print(vals.buffer_info())
vals.reverse()
print(vals)

# copy one array values to other array
vals2 = array(vals.typecode,(a*a for a in vals))
for e in vals2:
    print(e)

value = array('i',[2,4,6,8,10])
i = 0
while i < len(value):
    print(value[i])
    i+=1
    