'''
K-近邻算法（KNN）
定义：如果一个样本在特征空间中的k个最相似（即特征空间中最近邻）的样本中的大多数属于某一个类别，则该样本也属于这个类别
距离计算：欧氏距离
knn中的API：sklearn.neighbors.KNeighborsClassifier(n_neighbors = 5)  -- 参数：n_neighbors是选定参考几个邻居
'''

import sklearn
from sklearn.neighbors import KNeighborsClassifier
'''
sklearn优势：1.文档多，且规范  2.包含的算法多  3. 实现起来容易
sklearn中包含的内容：分类、聚类、回归   特征工程   模型选择、调优
'''

#获取数据
x = [[1], [2], [0], [0]]
y = [1, 1, 0, 0]
#机器学习
#实例化一个估计器
estimator = KNeighborsClassifier(n_neighbors=2)
#使用fit方法进行训练
estimator.fit(x, y)
#模型预测
print(estimator.predict([[100]]))

'''

欧氏距离  d = sqrt{(x1-x2)^2+(y1-y2)^2}
曼哈顿距离  d = |x1-x2|+|y1-y2|
切比雪夫距离 d = max(|x1-x2|,|y1-y2|)
标准欧氏距离： 
    标准化变量：x* = (x-m)/s   m为样本集x的均值 s为标准差
    标准化欧氏距离公式：d = aqrt{[(x1-x2)/Sx]^2 + [(y1-y2)/Sy]^2}
余弦距离  d = (x1*x2+y1*y2)/(sqrt(x1^2+y1^2) + sqrt(x2^2+y2^2))
'''