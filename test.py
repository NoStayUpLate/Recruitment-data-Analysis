import jieba
from jieba import analyse
from collections import Counter
import pandas as pd

# text = open('./C#OutputContent.txt', 'r', encoding='utf-8').read()
# # Analyse = jieba.analyse.set_idf_path('./TJ.txt')
# keywords = jieba.analyse.extract_tags(text, topK=50, withWeight=True)
#
#
# print(keywords)

name = []
num = []

Content = open('./TemptOutputContent.txt','r',encoding='utf-8').read()

Contentlist = Content.split(" ")


Count = Counter(Contentlist)

d = sorted(Count.items(),key=lambda x:x[1],reverse=True)

print(len(d))

for i in range(1,len(d)):
    name.append(d[i][0])
    # num.append(d[i][1])
print(name[0:30])
