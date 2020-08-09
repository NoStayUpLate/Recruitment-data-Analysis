import pyecharts.options as opts
from pyecharts.charts import Bar,Line
import pandas as pd
import numpy as np

def Salary_Jobs_bar_Mutiply(xaxis,Name,Num):
    c = (
        Bar(
            init_opts=opts.InitOpts(width='1500px')
        )
            .add_xaxis(xaxis)
            # .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="企业规模与岗位分类柱状图",subtitle="单位：个"),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(interval=0),
            ),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
        )
    )
    for name,num in zip(Name,Num):
        c.add_yaxis(name,num)

    return c

def Grid():
    grid = Grid()
    grid.add(Salary_Jobs_bar_Mutiply(Five_jobs, Working_Senior, Salary_min))
    grid.add(Salary_Jobs_bar_Mutiply(Five_jobs, Working_Senior, Salary_max))
    grid.render("grid_geo_bar.html")

if __name__ == '__main__':
    data = pd.read_csv("./Lagou_All.csv")
    # todo 五个职业下的学历要求薪资分类分布图
    Five_jobs = ['Python', 'Java', 'C#', '机器学习', '数据挖掘']
    Working_Senior = data.Working_Seniority_Requirements.value_counts().index.tolist()

    Salary_min = []
    Salary_max = []

    for job in Five_jobs:
        Salary_average_min_F = []
        Salary_average_max_F = []
        for workingSenior in Working_Senior:
            temp_min = np.mean(data.Salary_min[data.Classify == job][data.Working_Seniority_Requirements == workingSenior])
            temp_max = np.mean(data.Salary_max[data.Classify == job][data.Working_Seniority_Requirements == workingSenior])
            temp_min = np.around(temp_min, decimals=2)
            temp_max = np.around(temp_max, decimals=2)
            Salary_average_min_F.append(temp_min)
            Salary_average_max_F.append(temp_max)
        Salary_min.append(Salary_average_min_F)
        Salary_max.append(Salary_average_max_F)

    # FiveJobsMin = Salary_Jobs_bar_Mutiply(Five_jobs, Working_Senior, Salary_min)
    # FiveJobsMin.render('./FiveJobs_WorkingSenior_Bar.html')
    Grid()