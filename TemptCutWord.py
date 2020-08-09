import jieba
from jieba import analyse
from pyecharts.charts import WordCloud,Bar
import pyecharts.options as opts
from pyecharts.globals import SymbolType
import pandas as pd
from collections import Counter

# 词频统计
class WordCount(object):
    def CountWord(self):
        Name = []
        Num = []
        Content = open('./TemptOutputContent.txt', 'r', encoding='utf-8').read()
        Contentlist = Content.split(" ")
        Count = Counter(Contentlist)
        d = sorted(Count.items(), key=lambda x: x[1], reverse=True)
        for i in range(1, len(d)):
            Name.append(d[i][0])
            Num.append(d[i][1])
        return Name,Num

    # 柱状图
    def WordCountBar(self,xaxis,yaxis1):
        c = (
            Bar(
                init_opts=opts.InitOpts(width='1500px')
            )
                .add_xaxis(xaxis)
                .add_yaxis("关键词数量", yaxis1)
                # .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="职位诱惑词频统计柱状图", subtitle="单位：个"),
                xaxis_opts=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(interval=0,rotate=-45),
                ),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
            )
        )

        c.render("./Paints/Tempt_WordCutCount_Bar.html")

    def run(self):
        Name,Num = self.CountWord()
        self.WordCountBar(Name[0:30],Num[0:30])

# 岗位诱惑中文分词
class WordCut(object):
    def __init__(self):
        jieba.load_userdict('./TemptSplitWordDict.txt')
        self.data = pd.read_csv('./Lagou_All.csv')
        self.StopWords = [ i.strip() for i in open('./StopWords.txt','r',encoding='utf-8').readlines()]

    def wordcloud(self,words):
        c = (
            WordCloud()
            .add("",words, word_size_range=[20, 100], shape=SymbolType.RECT)
            .set_global_opts(title_opts=opts.TitleOpts(title="职位诱惑关键词词云图"))
        )

        return c

    def SplitSentence(self):
        Content = [i.strip() for i in open('./OutputCotent/TemptOutput.txt','r',encoding='utf-8').readlines()]
        # print(Content)
        outputs = open('./TemptOutputContent.txt','w',encoding='utf-8')

        for content in Content:
            outStr = ''
            sentenct = jieba.cut(content.strip())
            for word in sentenct:
                if word not in self.StopWords:
                    outStr += word
                    outStr += ' '
            outputs.write(outStr)
            # print(outStr)

        outputs.close()

    def CalculateWords(self):
        text = open('./TemptOutputContent.txt','r',encoding='utf-8').read()
        # Analyse = jieba.analyse.set_idf_path('./TJ.txt')
        keywords = jieba.analyse.extract_tags(text,topK=125,withWeight=True)
        return keywords

        # key = self.wordcloud(keywords)
        # key.render('./{}Requirements_WordCloud.html')

    def Writein(self):
        file = open('./OutputCotent/TemptOutput.txt','w',encoding='utf-8')
        Content = self.data.Job_Tempt
        for content in Content:
            file.write(content)
            file.write('\n')
        file.close()

    def run(self):
        # self.Writein()
        # self.SplitSentence()
        keywords = self.CalculateWords()
        # print(keywords)
        WordCloud = self.wordcloud(keywords)
        WordCloud.render("./Paints/TemptWordCut_WordCloud.html")


if __name__ == '__main__':
    # WordCut = WordCut()
    wordCount = WordCount()
    # WordCut.run()
    wordCount.run()







