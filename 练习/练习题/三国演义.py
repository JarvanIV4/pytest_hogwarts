# 利用jieba库统计三国演义中人物的出场次数
# https://www.cnblogs.com/wkfvawl/p/9487165.html#_label3
import jieba

text = open('三国演义.txt', "r", encoding='utf-8').read()
words = jieba.lcut(text)
counts = {}
for word in words:
   if len(word) == 1:  #排除带个字符的分词效果
       continue
   else:
       counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
   word,count=items[i]
   print("{0:<10}{1:>5}".format(word,count))
