import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib
from matplotlib import font_manager
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model
from sklearn import linear_model,model_selection,cross_validation
from sklearn import learning_curve

data_train = pd.read_csv("./train.csv")

data_train.info()
# 设置中文字体
font = {
    'family' : 'SimHei',
    'weight' : 'bold'
}
matplotlib.rc("font",**font)

fig = plt.figure()
fig.set(alpha = 0.2)
# # 在一张大图中分几个小图
# plt.subplot2grid((2,3),(0,0)) # 将图片分为2行3列，在1行1列的位置作图
# # 柱状图：幸存人数自动生成x轴，纵坐标为人数
# data_train.Survived.value_counts().plot(kind = 'bar')
# plt.title(u"获救情况（1为获救）")
# plt.ylabel(u"人数")
#
# plt.subplot2grid((2,3),(0,1)) # 将图片分为2行3列，在1行2列的位置作图
# # 柱状图：幸存人数自动生成x轴，纵坐标为人数
# data_train.Pclass.value_counts().plot(kind = 'bar')
# plt.title("乘客等级分布")
# plt.ylabel("人数")
#
# plt.subplot2grid((2,3),(0,2))
# # 散点图：幸存人数为x轴，年龄为y轴
# plt.scatter(data_train.Survived,data_train.Age)
# plt.title("按年龄获救分布（1为获救）")
# plt.ylabel("年龄")
# # 网格设置：b=True显示网格，axis-y显示y轴的网格
# plt.grid(b = True,which='major',axis = 'y')
#
# plt.subplot2grid((2,3),(1,0),colspan=2) # 将图片分为2行3列，在2行1列的位置作图，并且占用2列
# # 密度图
# data_train.Age[data_train.Pclass == 1].plot(kind = 'kde')
# data_train.Age[data_train.Pclass == 2].plot(kind = 'kde')
# data_train.Age[data_train.Pclass == 3].plot(kind = 'kde')
# plt.title("各等级的乘客年龄分布")
# plt.xlabel("年龄")
# plt.ylabel("密度")
# # 图例
# plt.legend(('头等舱','二等舱','三等舱'),loc = 'best')
#
# plt.subplot2grid((2,3),(1,2)) # 将图片分为2行3列，在2行3列的位置作图
# # 柱状图
# data_train.Embarked.value_counts().plot(kind = 'bar')
# plt.title("各登船口岸上船人数")
# plt.ylabel("人数")
#
# Survived_0 = data_train.Pclass[data_train.Survived == 0].value_counts()
# Survived_1 = data_train.Pclass[data_train.Survived == 1].value_counts()
# df_P = pd.DataFrame({'获救':Survived_1,'未获救':Survived_0})
# # print(df)
# # 柱状图，stacked = True是叠图绘制（默认为False）
# df_P.plot(kind = 'bar',stacked = True)
# plt.title("各乘客等级的获救情况")
# plt.xlabel("乘客等级")
# plt.ylabel("人数")
#
# Survived_m = data_train.Survived[data_train.Sex == 'male'].value_counts()
# Survived_f = data_train.Survived[data_train.Sex == 'female'].value_counts()
# df_S = pd.DataFrame({'男性':Survived_m,'女性':Survived_f})
# df_S.plot(kind = 'bar',stacked = True)
# plt.title("按性别对照获救情况")
# plt.ylabel("性别")
# plt.xlabel("人数")


# plt.title("根据船舱等级和性别的获救情况")
# Female_S = fig.add_subplot(141)
# data_train.Survived[data_train.Sex == 'female'][data_train.Pclass != 3].value_counts().plot(kind = 'bar',label = 'Female/Highclass',color = 'pink')
# Female_S.set_xticklabels(["未获救","获救"])
# plt.legend(["女性/高等舱"],loc = 'best')
#
# Female_L = fig.add_subplot(142,sharey = Female_S)
# data_train.Survived[data_train.Sex == 'female'][data_train.Pclass == 3].value_counts().plot(kind = 'bar',label = '女性/低等舱',color = 'Green')
# Female_L.set_xticklabels(["未获救","获救"])
# plt.legend(loc = 'best')
#
# Male_S = fig.add_subplot(143,sharey = Female_S)
# data_train.Survived[data_train.Sex == 'male'][data_train.Pclass != 3].value_counts().plot(kind = 'bar',label = 'Male/Highclass',color = 'red')
# Male_S.set_xticklabels(["未获救","获救"])
# plt.legend(["男性/高等舱"],loc = 'best')
#
# Male_L = fig.add_subplot(144,sharey = Female_S)
# data_train.Survived[data_train.Sex == 'male'][data_train.Pclass == 3].value_counts().plot(kind = 'bar',label = 'Male/Lowclass',color = 'orange')
# Male_L.set_xticklabels(["未获救","获救"])
# plt.legend(["男性/低等舱"],loc = 'best')

# Survived_0 = data_train.Embarked[data_train.Survived == 0].value_counts()
# Survived_1 = data_train.Embarked[data_train.Survived == 1].value_counts()
# df_E = DataFrame({"未获就":Survived_0,"获救":Survived_1})
# df_E.plot(kind = 'bar',stacked = True)
# plt.title("各登陆港口的获救情况")
# plt.xlabel("登录港口")
# plt.ylabel("人数")

# g = data_train.groupby(['SibSp','Survived'])
# df = pd.DataFrame(g.count()['PassengerId'])
# print(df)
#
# g = data_train.groupby(['Parch','Survived'])
# df = pd.DataFrame(g.count()['PassengerId'])
# print(df)
#
# print(data_train.Cabin.value_counts())
#
# Survived_Cabin = data_train.Survived[pd.notnull(data_train.Cabin)].value_counts()
# Survived_NoCabin = data_train.Survived[pd.isnull(data_train.Cabin)].value_counts()
# df_C = DataFrame({'有Cabin':Survived_Cabin,'无Cabin':Survived_NoCabin})
# df_C.plot(kind = 'bar',stacked = True)
# plt.title("按Cabin有无看获救情况")
# plt.xlabel("Cabin有无")
# plt.ylabel("人数")
#
# plt.show()

# 数据预处理
# 使用RandomForestClassifier填补确实的年龄属性
def set_missing_ages(df):
    # 把已有的数值型特征取出来丢进 Random Forest Regressor 中
    age_df = df[['Age','Fare','Parch','SibSp','Pclass']]

    # 乘客分成已知年龄和未知年龄两部分,.values 将DataFrame格式转换成数组形式
    known_age = age_df[age_df.Age.notnull()].values
    unknown_age = age_df[age_df.Age.isnull()].values

    # y是目标年龄
    y = known_age[:,0]

    # x是特征值属性
    x = known_age[:,1:]

    rfr = RandomForestRegressor(random_state=0,n_estimators=2000,n_jobs=-1)
    rfr.fit(x,y)

    predictedAges = rfr.predict(unknown_age[:,1::])

    df.loc[(df.Age.isnull()),'Age'] = predictedAges

    return df,rfr

def set_Cabin_type(df):
    # loc 定位符合条件的数据
    df.loc[(df.Cabin.notnull()),'Cabin'] = "Yes"
    df.loc[(df.Cabin.isnull()),'Cabin'] = "No"
    return df

data_train, rfr = set_missing_ages(data_train)
data_train = set_Cabin_type(data_train)

# get_dummies（数据列，prefix = 'XXX'）对数据列进行one-hot编码，使用XXX对分类进行命名
dummies_Cabin = pd.get_dummies(data_train['Cabin'],prefix = 'Cabin')
dummies_Embarked = pd.get_dummies(data_train['Embarked'],prefix='Embarked')
dummies_Sex = pd.get_dummies(data_train['Sex'],prefix='Sex')
dummies_Pclass = pd.get_dummies(data_train['Pclass'],prefix='Pclass')

df = pd.concat([data_train,dummies_Cabin,dummies_Embarked,dummies_Sex,dummies_Pclass],axis=1)

# 删除原表中的这些列，用刚刚生成的 dummies_X 代替
# inplace=False，默认该删除操作不改变原数据，而是返回一个执行删除操作后的新dataframe；
# inplace=True，则会直接在原数据上进行删除操作，删除后无法返回。
df.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

# 标准化数据，通过对原始数据进行变换把数据变换到均值为0，标准差为1范围内
scaler = preprocessing.StandardScaler()
# age_scale_param = scaler.fit(df['Age'])
df['Age_scaled'] = scaler.fit_transform(df[['Age']])
# fare_scale_param = scaler.fit(df['Fare'])
df['Fare_scaled'] = scaler.fit_transform(df[['Fare']])

# print(df)

# 逻辑回归建模
# regex 利用后面的正则表达式进行筛选
train_df = df.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.values

# y即Survival结果
y = train_np[:, 0]

# X即特征属性值
X = train_np[:, 1:]

# C 和 tol 都是计算参数，penalty是用于选择惩罚项中的使用规范
clf = linear_model.LogisticRegression(C=1.0,penalty='l1',tol = 1e-6)
clf.fit(X,y)

print(clf)

# 对 test_data 进行数据预处理
data_test = pd.read_csv("./test.csv")
# 定位符合条件的数据
data_test.loc[(data_test.Fare.isnull()),'Fare'] = 0
tmp_df = data_test[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]
# 取出年龄数据丢失的数据项组成数组
null_age = tmp_df[data_test.Age.isnull()].values

# 根据特征属性x预测年龄并补上
X = null_age[:,1:]
predictedAge = rfr.predict(X)
# 补充预测数据
data_test.loc[(data_test.Age.isnull()),'Age'] = predictedAge

# 处理 test.csv 中的 Cabin 数据
# Cabin数据处理为 '有->Yes' '无->No'
data_test = set_Cabin_type(data_test)
dummies_Cabin = pd.get_dummies(data_test['Cabin'],prefix='Cabin')
dummies_Embarked = pd.get_dummies(data_test['Embarked'],prefix='Embarked')
dummies_Sex = pd.get_dummies(data_test['Sex'],prefix='Sex')
dummies_Pclass = pd.get_dummies(data_test['Pclass'],prefix='Pclass')

# concat 联合各种表格,axis = 1 为按列为轴合并，默认为按行合并
df_test = pd.concat([data_test,dummies_Cabin,dummies_Embarked,dummies_Sex,dummies_Pclass],axis=1)

# 删除原表中的这些列，用刚刚生成的 dummies_X 代替
# inplace=False，默认该删除操作不改变原数据，而是返回一个执行删除操作后的新dataframe；
# inplace=True，则会直接在原数据上进行删除操作，删除后无法返回。
df_test.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

# 标准化数据，通过对原始数据进行变换把数据变换到均值为0，标准差为1范围内
# 因为 Age 和 Fare 两个列的参数内部差距过大，数据杂乱，影响数据的收敛，影响预测
df_test['Age_scaled'] = scaler.fit_transform(df_test[['Age']])
df_test['Fare_scaled'] = scaler.fit_transform(df_test[['Fare']])

print(df_test)
# TODO 至此就可以提交了，以上是未经过优化之前的版本
'''**************************************'''
# TODO 开始进行优化

# 关联 model系数 和 feature
pd.DataFrame({"columns":list(train_df.columns)[1:],"coef":list(clf.coef_.T)})

clf = linear_model.LogisticRegression(C = 1.0,penalty='l1',tol= 1e-6)
all_data = df.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
X = all_data.values
y = all_data.values
# print(cross_validation.cross_val_score(clf,X,y,cv = 5))

# 进行数据分割：按照 训练数据：CV数据 = 7：3的比例
split_train,split_cv = model_selection.train_test_split(df,test_size=0.3,random_state=0)
train_df = split_train.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')

# # 生成模型
# clf = linear_model.LogisticRegression(C = 1.0,penalty = 'l1',tol=1e-6)
# clf.fit(train_df.values[:,1:],train_df.values[:,0])
#
# # 对 cross validation 数据进行预测
# cv_df = split_cv.filter(regex = 'Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
# predictions = clf.predict(cv_df.values)
#
# origin_data_train = pd.read_csv("./train.csv")
# bad_cases = origin_data_train.loc[origin_data_train['PassengerId'].isin(split_cv[predictions != cv_df.values[:,0]]['PassengerId'].values)]
# print(bad_cases)

# 用 sklearn 的 learning_curve 得到 training_score 和 cv_score，使用 plt 画出 learning_curve
# 也就是用训练和测试的数据画出当前数据过拟合状态还是欠拟合状态
def plot_learning_curve(estimator,title,X,y,ylim = None,cv = None,n_jobs = 1,
                        train_size = np.linspace(.05,1.,20),verbose = 0,plot = True):
    """
     画出data在某模型上的learning curve.
     参数解释
     ----------
     estimator : 你用的分类器。
     title : 表格的标题。
     X : 输入的feature，numpy类型
     y : 输入的target vector
     ylim : tuple格式的(ymin, ymax), 设定图像中纵坐标的最低点和最高点
     cv : 做cross-validation的时候，数据分成的份数，其中一份作为cv集，其余n-1份作为training(默认为3份)
     n_jobs : 并行的的任务数(默认1)
     """
    train_sizes,train_scores,test_scores = model_selection.learning_curve(estimator,X,y,cv=cv,n_jobs=n_jobs,train_sizes=train_size,verbose=verbose)
    # 训练集取平均值，按列计算
    train_scores_mean = np.mean(train_scores,axis=1)
    # 训练集取标准差，按列计算
    train_scores_std = np.std(train_scores,axis=1)
    # 测试集同上处理
    test_scores_mean = np.mean(test_scores,axis=1)
    test_scores_std = np.std(test_scores,axis=1)

    if plot:
        plt.figure()
        plt.title(title)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.xlabel(u"训练样本数")
        plt.ylabel(u"得分")
        # gca-->get current axes
        plt.gca().invert_yaxis()
        # 设置网格
        plt.grid()

        # 在规定区域生成高亮
        plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,
                         alpha=0.1, color="b")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std,
                         alpha=0.1, color="r")
        # ‘o-’是图表线型
        plt.plot(train_sizes, train_scores_mean, 'o-', color="b", label=u"训练集上得分")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="r", label=u"交叉验证集上得分")

        plt.legend(loc="best")

        plt.draw()
        plt.show()
        plt.gca().invert_yaxis()

        midpoint = ((train_scores_mean[-1] + train_scores_std[-1]) + (test_scores_mean[-1] - test_scores_std[-1])) / 2
        diff = (train_scores_mean[-1] + train_scores_std[-1]) - (test_scores_mean[-1] - test_scores_std[-1])
        return midpoint, diff

plot_learning_curve(clf,"学习曲线",X,y)
















