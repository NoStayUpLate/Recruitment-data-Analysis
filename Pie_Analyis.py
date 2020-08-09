import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Page
import pandas as pd
import numpy as np

def pie_rosetype(Classify,Counts,title):
    c = (
        Pie()
        .add(
            "image 1",
            [list(z) for z in zip(Classify,Counts)],
            radius=["30%", "75%"],
            center=["50%", "60%"],
            rosetype="radius",
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            legend_opts=opts.LegendOpts(is_show=False,orient='vertical',pos_top="15%",pos_left="2%")
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    return c

def page_draggable_layout(Area,Area_Num,Title):
    page = Page(layout=Page.DraggablePageLayout)

    for area,area_num,title in zip(Area,Area_Num,Title):
        page.add(
            pie_rosetype(area,area_num,title),
        )

    page.render("Each_Area_Job_Distribute.html")

if __name__ == '__main__':
    data = pd.read_csv("./Lagou_All.csv")

    City = data.City.value_counts().index.tolist()
    Area = []
    Area_Num = []
    title = []
    for city in City:
            temp_Area = data.Area[data.City == city].value_counts().index.tolist()[0:6]
            temp_Area_Num = data.Area[data.City == city].value_counts().tolist()[0:6]
            temp_title = city + "各区招聘数据数量分布图"
            Area.append(temp_Area)
            Area_Num.append(temp_Area_Num)
            title.append(temp_title)

    page_draggable_layout(Area,Area_Num,title)