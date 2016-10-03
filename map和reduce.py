# -*- coding: utf-8 -*-
# 将名字格式规范
def normalize(name):
    return name[0].upper()+name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



# -*- coding: utf-8 -*-
#求积
from functools import reduce

def prod(L):
    def f(x,y):
        return x*y    
    return reduce(f,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
 Run




# -*- coding: utf-8 -*-
#将字符串转换为浮点数
from functools import reduce

def str2float(s):
    left,right = s.split('.')
    right_len = len(right)    
    def str2int(c):
        return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}[c]
    def fn(x,y):
        return x*10+y
    L1=reduce(fn,map(str2int,left))
    L2=reduce(fn,map(str2int,right))/(10**right_len)
    return L1+L2

print('str2float(\'123.456\') =', str2float('123.456'))
