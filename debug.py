import ipdb
from lib import *

#code here
c1 = Company("name", 1980)
d1 = Dev("Adam")
f1 = Freebie(d1, c1, 1, 1)
f2 = Freebie(d1, c1, 2, 1)
f3 = Freebie(d1, c1, 3, 1)
f4 = Freebie(d1, c1, 4, 1)
f4 = Freebie(d1, c1, 4, 1)


# print(c1.freebies())
#print(c1.devs())



ipdb.set_trace()