# -*- coding: utf-8 -*-
#输出回数
def is_palindrome(n):
    return int(str(n)[::-1])==n
#将输入数字转换字符串并反向，再转换整型和原数比较，相同则返回    

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
