import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_train = pd.read_excel("./LG_data_test.xlsx")

data_train.info()

# 设置中文字体
font = {
    'family' : 'SimHei',
    'weight' : 'bold'
}
matplotlib.rc("font",**font)

fig = plt.figure()
fig.set(alpha = 0.2)
#
# # plt.subplot2grid((2,3),(0,0))
# # data_train.工作年限要求.value_counts().plot(kind = 'pie')
# # plt.title("工作年限要求柱状图")
# # plt.ylabel("年限")
#
# plt.scatter(data_train.Area,data_train.Salary)
# plt.title("杭州区薪资分布")
# plt.ylabel("薪资待遇")
# plt.xticks(rotation = -45)
# # 网格设置：b=True显示网格，axis-y显示y轴的网格
# plt.grid(b = True,which='major',axis = 'y')
#
# plt.show()
class Visualization():
    # 单一数据柱状图绘制
    def Bar_visualization(self,data_x):
        plt.figure(figsize=(50,8))
        data_x.value_counts().plot(kind = 'bar')
        # Name = self.translate(data_x)
        # plt.title(Name + "柱状图")
        plt.xticks(rotation = -45)
        # plt.ylabel(Name)
        print("*"*100)
        plt.show()

    # 双数据柱状图绘制
    def Bar_stack_visualization(self,data_x,data_y,y1,y2):
        plt.subplot2grid((2,3),(0,0))
        df_y1 = data_train.data_x[data_train.data_y == y1].value_counts()
        df_y2 = data_train.data_x[data_train.data_y == y2].value_counts()
        df = pd.DataFrame({y1:df_y1,y2:df_y2})
        df.plot(kind = 'bar',stacked = True)
        Name_x = self.translate(data_x)
        Name_y = self.translate(data_y)
        plt.title(("按{}对照{}情况").format(Name_x,Name_y))
        plt.xlabel(Name_x)
        plt.xlabel(Name_y)
        plt.show()


    # 饼图绘制
    def Pie_visualization(self,data_x,data_y):
        data_train.data_x.value_counts().plot(kind = 'pie')
        plt.show()

    # 散点图绘制
    def Scatter_visualization(self,data_x,data_y):
        plt.scatter(data_train.data_x,data_train.data_y)
        Name_x = self.translate(data_x)
        Name_y = self.translate(data_y)
        plt.title(("按{}的{}分布").format(Name_x,Name_y))
        plt.grid(b = True)
        plt.show()

    # 折线图绘制
    def Line_visualization(self,data_x,data_y):
        pass

    # label翻译
    def translate(self,name):
        if name == "Classify":
            Name = "技术分类"
        if name == "Jobs":
            Name = "职位"
        if name == "Salary":
            Name = "薪资情况"
        if name == "Company_Name":
            Name = "公司"
        if name == "Industry":
            Name = "行业"
        if name == "Company_Size":
            Name = "公司规模"
        if name == "Pulish_Data":
            Name = "招聘数据发布时间"
        if name == "City":
            Name = "城市"
        if name == "Area":
            Name = "城区"
        if name == "Working_Seniority_Requirements":
            Name = "工作年限要求"
        if name == "Education_Requirements":
            Name = "学历要求"
        if name == "Job_Tempt":
            Name = "职位诱惑"
        if name == "Financing_Status":
            Name = "融资情况"

        return Name

if __name__ == '__main__':
    Visualization = Visualization()


















