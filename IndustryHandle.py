import jieba
from jieba import analyse
from pyecharts.charts import WordCloud
import pyecharts.options as opts
from pyecharts.globals import SymbolType
import pandas as pd
from collections import Counter


class WordCount(object):
    def CountWord(self, name):
        Name = []
        Num = []
        Content = open('./{}OutputContent.txt'.format(name), 'r', encoding='utf-8').read()
        Contentlist = Content.split(" ")
        Count = Counter(Contentlist)
        d = sorted(Count.items(), key=lambda x: x[1], reverse=True)
        print(d[0:50])
        print(len(d))
        for i in range(1, len(d)):
            Name.append(d[i][0])
            Num.append(d[i][1])
        return Name, Num


# 岗位技能中文分词
class WordCut(object):
    def __init__(self):
        jieba.load_userdict('./SkillSplitWordDict.txt')
        self.data = pd.read_csv('./Lagou_All.csv')
        self.StopWords = [i.strip() for i in open('./StopWords.txt', 'r', encoding='utf-8').readlines()]

    def wordcloud(self, words, name):
        c = (
            WordCloud()
                .add("", words, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
                .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-shape-diamond"))
        )

        c.render('./Paints/{}WordCut_WordCloud.html'.format(name))

    def SplitSentence(self, name):
        Content = [i.strip() for i in
                   open('./OutputCotent/{}RequirementOutput.txt'.format(name), 'r', encoding='utf-8').readlines()]
        # print(Content)
        outputs = open('./{}OutputContent.txt'.format(name), 'w', encoding='utf-8')

        for content in Content:
            outStr = ''
            sentenct = jieba.cut(content.strip())
            for word in sentenct:
                if word not in self.StopWords:
                    outStr += word
                    outStr += ' '
            outputs.write(outStr)
            outputs.write('\n')
            # print(outStr)

        outputs.close()

    def CalculateWords(self, name):
        text = open('./{}OutputContent.txt'.format(name), 'r', encoding='utf-8').read()
        # Analyse = jieba.analyse.set_idf_path('./TJ.txt')
        keywords = jieba.analyse.extract_tags(text, topK=100, withWeight=True)

        return keywords

    def Writein(self, name):
        file = open('./OutputCotent/{}RequirementOutput.txt'.format(name), 'w', encoding='utf-8')
        Content = self.data.Industry
        for content in Content:
            file.write(content)
            file.write('\n')
        file.close()

    def run(self):
        # todo 行业信息的文本
        # self.Writein("Industry")
        self.SplitSentence("Industry")

if __name__ == '__main__':
    WordCut = WordCut()
    WordCut.run()
    # WordCount = WordCount()
    # Classify = ['C#', 'Java', 'Python', '机器学习', '数据挖掘']
    # for classify in Classify:
    #     WordCount.CountWord(classify)








