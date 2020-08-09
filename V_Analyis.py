import pyecharts.options as opts
from pyecharts.charts import Bar,Line
import pandas as pd
import numpy as np
from collections import Counter

"""
1.薪资和职业的关系
2.薪资和受教育的关系
3.薪资和地区的关系
"""

# 双柱状图
def Salary_Jobs_bar_stack(xaxis,yaxis1,yaxis2,title):
    c = (
        Bar(
            init_opts=opts.InitOpts(width='1500px')
        )
            .add_xaxis(xaxis)
            .add_yaxis("薪资下限平均值", yaxis1)
            .add_yaxis("薪资上限平均值", yaxis2)
            # .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
            title_opts=opts.TitleOpts(title=title,subtitle="单位：K"),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(interval=0,rotate=-45),
            ),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
        )
    )

    return c

# 单柱状图
def Salary_Jobs_bar(xaxis,yaxis1):
    c = (
        Bar(
            init_opts=opts.InitOpts(width='1000px')
        )
            .add_xaxis(xaxis)
            .add_yaxis("招聘数据数量", yaxis1)
            # .add_yaxis("薪资上限平均值", yaxis2)
            # .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各城市招聘数据数量柱状图",subtitle="单位：个"),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(interval=0),
            ),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
        )
    )

    return c

def Salary_Jobs_bar_Mutiply(xaxis,Name,Num,title):
    c = (
        Bar(
            init_opts=opts.InitOpts(width='1000px')
        )
            .add_xaxis(xaxis)
            # .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
            .set_global_opts(
            title_opts=opts.TitleOpts(title=title,subtitle="单位：K"),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(interval=0),
            ),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
        )
    )
    for name,num in zip(Name,Num):
        c.add_yaxis(name,num)

    return c

def Lines(x_data,y_data,title):
    c = (
        Line()
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            title_opts=opts.TitleOpts(title=title,subtitle="单位：个"),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    return c

def Lines_Mutiply(x_data,y1_data,y2_data,y3_data,title):
    c = (
        Line()
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            title_opts=opts.TitleOpts(title=title,subtitle="单位：个"),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="",
            y_axis=y1_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=True),
        )
            .add_yaxis(
            series_name="",
            y_axis=y2_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=True),
        )
            .add_yaxis(
            series_name="",
            y_axis=y3_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=True),
        )
    )
    return c

def Counts_Financing_Status(Financing_Status,Working_Senior):
    Status = []
    for ws in Working_Senior:
        temp = data.Financing_Status[data.Financing_Status == Financing_Status][data.Working_Seniority_Requirements == ws].value_counts()[0]
        temp = int(temp)
        Status.append(temp)
    return Status

def Counts_Companysize_Status(Company_Size,Working_Senior):
    Status = []
    for ws in Working_Senior:
        temp = data.Company_Size[data.Company_Size == Company_Size][data.Working_Seniority_Requirements == ws].value_counts()[0]
        temp = int(temp)
        Status.append(temp)
    return Status

def Counts_Companysize_Largeclassify(LargeClassify,CompanySize):
    Classify = []
    for LC in LargeClassify:
        C = []
        for CS in CompanySize:
            temp = data.Large_classify[data.Large_classify == LC][data.Company_Size == CS].value_counts()[0]
            temp = int(temp)
            C.append(temp)
        Classify.append(C)
    return Classify

if __name__ == '__main__':
    data = pd.read_csv("./Lagou_All.csv")

    # # todo 按照十一个大的类别分类,分析薪资上下限的高低
    # Large_classify_name = data.Large_classify.value_counts().index.tolist()
    #
    # Salary_min_average_LC = []
    # Salary_max_average_LC = []
    #
    # for large_classify_name in Large_classify_name:
    #     temp_min = np.mean(data.Salary_min[data.Large_classify == large_classify_name])
    #     temp_max = np.mean(data.Salary_max[data.Large_classify == large_classify_name])
    #     temp_min = np.around(temp_min,decimals=2)
    #     temp_max = np.around(temp_max,decimals=2)
    #     # print("name:{}...min_average:{}...max_average{}".format(large_classify_name,temp_min,temp_max))
    #     Salary_min_average_LC.append(temp_min)
    #     Salary_max_average_LC.append(temp_max)
    #
    # Salary_Jobs_bar_stack(Large_classify_name,Salary_min_average_LC,Salary_max_average_LC)

    # # todo 薪资上下限与学历的关系
    # Education = data.Education_Requirements.value_counts().index.tolist()
    #
    # Salary_min_average_E = []
    # Salary_max_average_E = []
    #
    # for education in Education:
    #     temp_min = np.mean(data.Salary_min[data.Education_Requirements == education])
    #     temp_max = np.mean(data.Salary_max[data.Education_Requirements == education])
    #     temp_min = np.around(temp_min,decimals=2)
    #     temp_max = np.around(temp_max,decimals=2)
    #     Salary_min_average_E.append(temp_min)
    #     Salary_max_average_E.append(temp_max)
    #
    # Salary_Jobs_bar_stack(Education,Salary_min_average_E,Salary_max_average_E)

    # # todo 薪资上下限与工作年限的关系
    # Working_senior = data.Working_Seniority_Requirements.value_counts().index.tolist()
    #
    # Salary_min_average_W = []
    # Salary_max_average_W = []
    #
    # for working_senior in Working_senior:
    #     temp_min = np.mean(data.Salary_min[data.Working_Seniority_Requirements == working_senior])
    #     temp_max = np.mean(data.Salary_max[data.Working_Seniority_Requirements == working_senior])
    #     temp_min = np.around(temp_min,decimals=2)
    #     temp_max = np.around(temp_max,decimals=2)
    #     Salary_min_average_W.append(temp_min)
    #     Salary_max_average_W.append(temp_max)
    #
    # Salary_Jobs_bar_stack(Working_senior,Salary_min_average_W,Salary_max_average_W)

    # # todo 薪资与城市
    # City = data.City.value_counts().index.tolist()
    #
    # Salary_min_average_C = []
    # Salary_max_average_C = []
    #
    # for city in City:
    #     temp_min = np.mean(data.Salary_min[data.City == city])
    #     temp_max = np.mean(data.Salary_max[data.City == city])
    #     temp_min = np.around(temp_min,decimals=2)
    #     temp_max = np.around(temp_max,decimals=2)
    #     Salary_min_average_C.append(temp_min)
    #     Salary_max_average_C.append(temp_max)
    #
    # Salary_Jobs_bar_stack(City,Salary_min_average_C,Salary_max_average_C)

    # # todo 各城市招聘数据数量
    # City = data.City.value_counts().index.tolist()
    # Job_counts = data.City.value_counts().tolist()
    #
    # Salary_Jobs_bar(City,Job_counts)

    # # todo 各种融资类型的企业对于工作年限的需求
    # # 工作年限
    # Working_Senior = data.Working_Seniority_Requirements.value_counts().index.tolist()
    #
    # A_Finan = Counts_Financing_Status("A轮",Working_Senior)
    # B_Finan = Counts_Financing_Status("B轮",Working_Senior)
    # C_Finan = Counts_Financing_Status("C轮",Working_Senior)
    # D_Finan = Counts_Financing_Status("D轮及以上",Working_Senior)
    # NoNeed_Finan = Counts_Financing_Status("不需要融资",Working_Senior)
    # Angle_Finan = Counts_Financing_Status("天使轮",Working_Senior)
    # Not_Finan = Counts_Financing_Status("未融资",Working_Senior)
    # Publiced_Finan = Counts_Financing_Status("上市公司",Working_Senior)
    #
    # Salary_Jobs_bar_Mutiply(Working_Senior,A_Finan,B_Finan,C_Finan,D_Finan,NoNeed_Finan,Angle_Finan,Not_Finan,Publiced_Finan)

    # # todo 各种规模企业对于工作年限的需求
    # Working_Senior = data.Working_Seniority_Requirements.value_counts().index.tolist()
    #
    # Less15 = Counts_Companysize_Status("少于15人",Working_Senior)
    # _15to50 = Counts_Companysize_Status("15-50人",Working_Senior)
    # _50to150 = Counts_Companysize_Status("50-150人",Working_Senior)
    # _150to500 = Counts_Companysize_Status("150-500人",Working_Senior)
    # _500to2000 = Counts_Companysize_Status("500-2000人",Working_Senior)
    # More2000 = Counts_Companysize_Status("2000人以上",Working_Senior)
    #
    # WorkingSenior_Companysize = Salary_Jobs_bar_Mutiply(Working_Senior,Less15,_15to50,_50to150,_150to500,_500to2000,More2000)
    # WorkingSenior_Companysize.render("./WorkingSenior_CompanySize.html")

    # # todo 企业规模与岗位分类情况
    # Company_Size = data.Company_Size.value_counts().index.tolist()
    # Large_Classify = data.Large_classify.value_counts().index.tolist()
    # Large = Counts_Companysize_Largeclassify(Large_Classify,Company_Size)
    # CompanySize_LargeClassify = Salary_Jobs_bar_Mutiply(Company_Size,Large_Classify,Large)
    #
    # CompanySize_LargeClassify.render("./CompanySize_LargeClassify_Bar.html")

    # # todo 后端开发岗位下的职位的薪资分布
    # # 职位
    # Job_Classify = data.Classify[data.Large_classify == "后端开发"].value_counts().index.tolist()
    #
    # Salary_min_average_J = []
    # Salary_max_average_J = []
    #
    # for job_classify in Job_Classify:
    #     temp_min = np.mean(data.Salary_min[data.Classify == job_classify])
    #     temp_max = np.mean(data.Salary_max[data.Classify == job_classify])
    #     temp_min = np.around(temp_min,decimals=2)
    #     temp_max = np.around(temp_max,decimals=2)
    #     Salary_min_average_J.append(temp_min)
    #     Salary_max_average_J.append(temp_max)
    #
    # c = Salary_Jobs_bar_stack(Job_Classify,Salary_min_average_J,Salary_max_average_J,"后端开发分类下的职位薪资上下限柱状图")
    # c.render("./Salary_JobClassify_BackDevelopement_Bar.html")

    # # todo 后端开发岗位下的职位的薪资分布
    # # 职位
    # Job_Classify = data.Classify[data.Large_classify == "后端开发"].value_counts().index.tolist()
    #
    # Salary_min_average_J = []
    # Salary_max_average_J = []
    #
    # for job_classify in Job_Classify:
    #     temp_min = np.mean(data.Salary_min[data.Classify == job_classify][data.Working_Seniority_Requirements == '应届毕业生'])
    #     temp_max = np.mean(data.Salary_max[data.Classify == job_classify][data.Working_Seniority_Requirements == '应届毕业生'])
    #     temp_min = np.around(temp_min,decimals=2)
    #     temp_max = np.around(temp_max,decimals=2)
    #     Salary_min_average_J.append(temp_min)
    #     Salary_max_average_J.append(temp_max)
    #
    # c = Salary_Jobs_bar_stack(Job_Classify,Salary_min_average_J,Salary_max_average_J,"后端开发分类下应届毕业生的职位薪资上下限柱状图")
    # c.render("./Graduate_BackDevelopement_Bar.html")

    # # todo 应届毕业生在后端开发的岗位分布下的薪资分布
    # Salary_B = data.Salary[data.Large_classify == "后端开发"][data.Working_Seniority_Requirements == '应届毕业生'].value_counts()
    # Salary_name_B = Salary_B.index.tolist()
    # Salary_num_B = Salary_B.tolist()

    # C = Lines(Salary_name,Salary_num,"应届毕业生在后端开发岗位分类下的薪资折线图")
    # C.render("./BackDevelopement_Graduate.html")

    # # todo 人工智能岗位下的职位的薪资分布
    # # 职位
    # Job_Classify = data.Classify[data.Large_classify == "人工智能"].value_counts().index.tolist()
    #
    # Salary_min_average_J = []
    # Salary_max_average_J = []
    #
    # for job_classify in Job_Classify:
    #     temp_min = np.mean(data.Salary_min[data.Classify == job_classify][data.Working_Seniority_Requirements == '应届毕业生'])
    #     temp_max = np.mean(data.Salary_max[data.Classify == job_classify][data.Working_Seniority_Requirements == '应届毕业生'])
    #     temp_min = np.around(temp_min,decimals=2)
    #     temp_max = np.around(temp_max,decimals=2)
    #     Salary_min_average_J.append(temp_min)
    #     Salary_max_average_J.append(temp_max)
    #
    # c = Salary_Jobs_bar_stack(Job_Classify,Salary_min_average_J,Salary_max_average_J,"人工智能分类下应届毕业生的职位薪资上下限柱状图")
    # c.render("./Paints/Graduate_AI_Bar.html")
    #
    # # todo 应届毕业生在人工智能的岗位分布下的薪资分布
    # Salary = data.Salary[data.Large_classify == "人工智能"][data.Working_Seniority_Requirements == '应届毕业生'].value_counts()
    # Salary_name = Salary.index.tolist()
    # Salary_num = Salary.tolist()
    # C = Lines(Salary_name,Salary_num,"应届毕业生在人工智能岗位分类下的薪资折线图")
    # C.render("./Paints/AI_Graduate_Line.html")

    # #todo DBA岗位下的职位的薪资分布
    # # 职位
    # Job_Classify = data.Classify[data.Large_classify == "DBA"].value_counts().index.tolist()
    #
    # Salary_min_average_J = []
    # Salary_max_average_J = []
    #
    # for job_classify in Job_Classify:
    #     temp_min = np.mean(data.Salary_min[data.Classify == job_classify][data.Working_Seniority_Requirements == '应届毕业生'])
    #     temp_max = np.mean(data.Salary_max[data.Classify == job_classify][data.Working_Seniority_Requirements == '应届毕业生'])
    #     temp_min = np.around(temp_min,decimals=2)
    #     temp_max = np.around(temp_max,decimals=2)
    #     Salary_min_average_J.append(temp_min)
    #     Salary_max_average_J.append(temp_max)
    #
    # c = Salary_Jobs_bar_stack(Job_Classify,Salary_min_average_J,Salary_max_average_J,"DBA分类下应届毕业生的职位薪资上下限柱状图")
    # c.render("./Paints/Graduate_DBA_Bar.html")
    #
    # # todo 应届毕业生在DBA的岗位分布下的薪资分布
    # Salary = data.Salary[data.Large_classify == "DBA"][data.Working_Seniority_Requirements == '应届毕业生'].value_counts()
    # Salary_name = Salary.index.tolist()
    # Salary_num = Salary.tolist()
    # C = Lines(Salary_name,Salary_num,"应届毕业生在DBA岗位分类下的薪资折线图")
    # C.render("./Paints/DBA_Graduate_Line.html")

    # # todo 五个职业下的工作年限要求薪资分类分布图
    # Five_jobs = ['Python','Java','C#','机器学习','数据挖掘']
    # Working_Senior = data.Working_Seniority_Requirements.value_counts().index.tolist()
    #
    # Salary_min = []
    # Salary_max = []
    #
    # for job in Five_jobs:
    #     Salary_average_min_F = []
    #     Salary_average_max_F = []
    #     for workingSenior in Working_Senior:
    #         temp_min = np.mean(data.Salary_min[data.Classify == job][data.Working_Seniority_Requirements == workingSenior])
    #         temp_max = np.mean(data.Salary_max[data.Classify == job][data.Working_Seniority_Requirements == workingSenior])
    #         temp_min = np.around(temp_min,decimals=2)
    #         temp_max = np.around(temp_max,decimals=2)
    #         Salary_average_min_F.append(temp_min)
    #         Salary_average_max_F.append(temp_max)
    #     Salary_min.append(Salary_average_min_F)
    #     Salary_max.append(Salary_average_max_F)
    #
    # FiveJobsMin = Salary_Jobs_bar_Mutiply(Working_Senior,Five_jobs,Salary_min,'五个分类下的薪资下限平均值')
    # FiveJobsMin.render('./Paints/FiveJobs_WorkingSenior_Salary_min_Bar.html')
    #
    # FiveJobsMax = Salary_Jobs_bar_Mutiply(Working_Senior,Five_jobs,Salary_max,'五个分类下的薪资上限平均值')
    # FiveJobsMax.render('./Paints/FiveJobs_WorkingSenior_Salary_max_Bar.html')

    # # todo 五个职业下的学历薪资分类分布图
    # Five_jobs = ['Python','Java','C#','机器学习','数据挖掘']
    # Education = data.Education_Requirements.value_counts().index.tolist()
    # print(Education)
    #
    # Salary_min = []
    # Salary_max = []
    #
    # for job in Five_jobs:
    #     Salary_average_min_F = []
    #     Salary_average_max_F = []
    #     for education in Education:
    #         temp_min = np.mean(data.Salary_min[data.Classify == job][data.Education_Requirements == education])
    #         temp_max = np.mean(data.Salary_max[data.Classify == job][data.Education_Requirements == education])
    #         temp_min = np.around(temp_min,decimals=2)
    #         temp_max = np.around(temp_max,decimals=2)
    #         Salary_average_min_F.append(temp_min)
    #         Salary_average_max_F.append(temp_max)
    #     Salary_min.append(Salary_average_min_F)
    #     Salary_max.append(Salary_average_max_F)
    #
    #
    # FiveJobsMin = Salary_Jobs_bar_Mutiply(Education,Five_jobs,Salary_min,'五个分类下的薪资下限平均值')
    # FiveJobsMin.render('./FiveJobs_EducationSenior_Salary_min_Bar.html')
    #
    # FiveJobsMax = Salary_Jobs_bar_Mutiply(Education,Five_jobs,Salary_max,'五个分类下的薪资上限平均值')
    # FiveJobsMax.render('./FiveJobs_EducationSenior_Salary_max_Bar.html')

    # # todo 职位诱惑词频柱状图
    # Name = []
    # Num = []
    #
    # Content = open('./TemptOutputContent.txt', 'r', encoding='utf-8').read()
    #
    # Contentlist = Content.split(" ")
    #
    # Count = Counter(Contentlist)
    #
    # d = sorted(Count.items(), key=lambda x: x[1], reverse=True)
    #
    # for i in range(1, len(d)):
    #     Name.append(d[i][0])
    #     Num.append(d[i][1])
    # todo 三个较高薪的岗位的折线图汇总
    # todo 应届毕业生在后端开发的岗位分布下的薪资分布
    Salary_B = data.Salary[data.Large_classify == "后端开发"][data.Working_Seniority_Requirements == '应届毕业生'].value_counts()
    Salary_name_B = Salary_B.index.tolist()
    Salary_num_B = Salary_B.tolist()
    # todo 应届毕业生在人工智能的岗位分布下的薪资分布
    Salary_AI = data.Salary[data.Large_classify == "人工智能"][data.Working_Seniority_Requirements == '应届毕业生'].value_counts()
    Salary_name_AI = Salary_AI.index.tolist()
    Salary_num_AI = Salary_AI.tolist()
    # todo 应届毕业生在DBA的岗位分布下的薪资分布
    Salary_DBA = data.Salary[data.Large_classify == "DBA"][data.Working_Seniority_Requirements == '应届毕业生'].value_counts()
    Salary_name_DBA = Salary_DBA.index.tolist()
    Salary_num_DBA = Salary_DBA.tolist()




