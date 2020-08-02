#ACTION1 2+4+6+8+...+100
a=range(2,102,2)
b=sum(a)
print(sum(a))

sum=0
for i in range(2,102,2):
    sum=sum+i
print(sum)
print(i)

import numpy as np
print(sum(np.arange(2,102,2)))


#ACTION2 :统计全班成绩
import numpy as np
persontype = np.dtype({'names':['名字', U'语文', U'数学', U'英语'], \
							'formats':['U32','i', 'i', 'i']})
peoples = np.array([("张飞",68,65,30),("关羽",95,76,98), \
						("刘备",98,86,88),("典韦",90,88,77),("许褚",80,90,90)],dtype=persontype)
   

names = peoples['名字']
chineses = peoples['语文']
maths = peoples['数学']   
englishs = peoples['英语']
sumscore=chineses+maths+englishs
    
print('最小成绩',np.min(maths))
print('平均成绩',np.mean(maths))
print('最高成绩',np.max(maths))   
print('方差成绩',np.var(maths))
print('标准差成绩',np.std(maths))
print(sumscore)  
index=np.argsort(-sumscore)
namesort=names[index]
scoresort=sumscore[index]
print('总成绩从高到低排名',scoresort)
print('排名',namesort)
   
    数学中的平均成绩、最小成绩、最大成绩、方差、标准差
    总成绩排序，得出名次进行成绩输出
    
#ACTION3 :对汽车质量数据进行统计
# 数据集：car_complain.csv
# 600条汽车质量投诉
# Step1，数据加载
# Step2，数据预处理
# 拆分problem类型 => 多个字段
# Step3，数据统计
# 对数据进行探索：品牌投诉总数，车型投诉总数
# 哪个品牌的平均车型投诉最多
 
import pandas as pd
# 数据加载
result = pd.read_csv('car_complain.csv')
print(result)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print(result.columns)
tags = result.columns[7:]
print(tags)

df= result.groupby(['brand'])['id'].agg(['count'])
df2= result.groupby(['brand'])[tags].agg(['sum'])
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
df2.reset_index(inplace=True)
#df2.to_csv('temp.csv')
df2= df2.sort_values('count', ascending=False)
print(df2)
#print(df2.columns)
#df2.to_csv('temp.csv', index=False)
query = ('A11', 'sum')
print(df2.sort_values(query, ascending=False))
    