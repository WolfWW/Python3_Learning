from numpy import *
#用到了矩阵

#读取数据
def loadData(fileName):
    dataMat = []        #创建一个空列表
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        #strip去掉空白符，用制表符分隔数据
        fltLine = list(map(float,curLine))
        #map将每一个行转变成float，加个list后才能打印出来
        dataMat.append(fltLine)
    return dataMat

#感知器算法过程
def perceptron(dataInput,W,c):
    iter_number = 0   #迭代轮数
    rowCount = shape(dataInput)[0]  #模式矩阵的行数
    flag = 0        #旗子，用它标记计算结果>0的次数
    while flag < rowCount:
        flag = 0
        for i in range(rowCount):
            temp = vdot(W,dataInput[i,:])   #计算两个向量的点积
            if temp > 0:
                flag += 1
            else:
                W = W + c*dataInput[i,:]
        iter_number += 1
        print('第%d轮迭代结束,此轮有%d个小于等于0的情况。' % (iter_number,8-flag))
    print('代入全部样本计算结果均大于0，迭代结束。')
    return W,iter_number

#main
data = array(loadData('perceptData.txt'))
initW = array([-1,-2,-2,0])     #此处可以更改初始的权向量
c = 1                           #修正系数
W,iter_number = perceptron(data,initW,c)
print('权向量W =',W)
print('共迭代了 %d 轮' % iter_number)
#以下两步将方程中多余的符号去掉
s=str('判别函数为d(X) = %dx + %dy + %dz + %d'%(W[0],W[1],W[2],W[3]))
s=s.replace('+ -','- ')
print(s)