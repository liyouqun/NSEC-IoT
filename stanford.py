#   coding=utf-8

from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'D:/application/stanford-corenlp-full-2018-10-05/stanford-corenlp-full-2018-10-05')

sentence = "resolve dni address"
#print("中文分词：")
#print(nlp.word_tokenize(sentence))  # 中文分词
print("词性标注：")
print(nlp.pos_tag(sentence))  # 词性标注
#print("命名实体分析：")
#print(nlp.ner(sentence))  # 命名实体分析
#print("解析语法：")
#print(nlp.parse(sentence))  # 解析语法
#print("解析语法关系：")
#print(nlp.dependency_parse(sentence))  # 解析语法关系
nlp.close()