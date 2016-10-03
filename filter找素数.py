
#定义一个3开始的序列
def odd_iter():
    n=1
    while True:
        n=n+2
        yield n

#筛选函数，删掉n的整数倍
def filters(n):
    return lambda x:x % n > 0

#定义生成器，返回素数
def primes():
    yield 2
    it = odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(filters(n),it)

#prime没有停止条件
for n in primes():
    if n < 100:
        print(n)
    else:
        break
