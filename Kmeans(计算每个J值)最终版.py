from numpy import *
from math import *
from matplotlib import pyplot as plt

#读取数据点
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        #strip()删除字符串中的空白符，包括空格、‘\t’‘\n’‘\r’
        fltLine = tuple(map(float,curLine))    #每行读取后转换成float型
        dataMat.append(fltLine)         #将转换后的向量添加到矩阵的最后一行
    #print(type(dataMat))
    #print(dataMat)
    return dataMat

#计算模式到中心的欧几里得距离
def distEuclid(vecA,vecB):   #Euclid欧几里得，vector向量
    return sqrt(sum(power(vecA - vecB,2)))

#选择初始聚类中心
def setCent(dataSet,k):   #n是中心向量维数，k是中心个数
    n = shape(dataSet)[1]  #数据集的列数即中心向量列数
    center = zeros((k,n))
    for i in range(k):
        center[i,:] = dataSet[i,:]  #初始中心定为x1和x2
    return center


#kmeans算法过程
def kMeans(dataSet,k,distCompute=distEuclid,createCent=setCent):
    m = shape(dataSet)[0]   #m表示行数
    n = shape(dataSet)[1]   #n表示列数
    clusterGroup = mat(zeros((m,2)))    #创建一个矩阵，存放归属和距离
    #选定初始中心
    center = createCent(dataSet,k)
    #当中心改变时
    centerFlag = True   #初始化一个标志，表示中心改变
    while centerFlag == True:
        centerFlag = False
        #计算每个点，并归类
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                dist = distCompute(center[j,:],dataSet[i,:])
                if dist < minDist:
                    minDist = dist
                    minIndex = j
            if clusterGroup[i,0] != minIndex:
                #centerFlag = True
                clusterGroup[i,:] = minIndex,minDist
        #每个类的点求均值，并定为新的中心，直至某次计算与上次计算中心向量值相同
        newCenter = zeros((k,n))
        for j in range(k):
            pointCluster = dataSet[nonzero(clusterGroup[:, 0].A == j)[0]]
            #pointsInClust.append(tuple(map(float,mean(pointCluster,axis=0))))
            newCenter[j,:] = mean(pointCluster,axis=0)
            if center[j,0] != newCenter[j,0]:   #这里取巧了，想办法直接比一行
                centerFlag = True
                center[j,:] = newCenter[j,:]
    return center,clusterGroup

def compuJK(dataSet,k,center,clusterGroup):
    print('3.各聚类集的聚类准则函数值：')
    sumJ = 0
    for j in range(k):
        J=0
        for i in range(shape(dataSet)[0]):
            if clusterGroup[i,0] == j:
                tempJ = sum(power(dataSet[i,:] - center[j,:],2))
                J = J + tempJ
        print('第%d类的准则函数J为%f' % (j+1,J))
        sumJ = sumJ +J
    print('准则函数J的和为%f' % sumJ)

#用matplotlib显示分类结果
def show(dataSet,k,centroids,clusterAssment):
    numSamples, dim = dataSet.shape
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    for i in range(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)
    plt.show()

#主函数
def main():
    data = mat(loadDataSet('kmeansData.txt'))
    k = 5
    theCenter,theCluster = kMeans(data,k)
    print('K=%d时的结果：' % k)
    print('1.最终的聚类中心为：\n',theCenter)
    print('2.各模式分类序号为：\n',theCluster[:,0])
    compuJK(data,k,theCenter,theCluster)
    show(data,k,theCenter,theCluster)

if __name__ == '__main__':
    main()