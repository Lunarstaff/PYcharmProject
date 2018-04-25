#jieba-test.py
"""
jieba库-中文分词第三方库
-中文文本需要通过分词获得单个的词语

jieba库的安装：
pip install jieba

常用函数：
jieba.lcut(s) -精确模式，返回一个列表类型的分词结果
例：
>>> import jieba
>>> jieba.lcut("中国是一个伟大的国家")
Building prefix dict from the default dictionary ...
Dumping model to file cache C:\Users\lywte\AppData\Local\Temp\jieba.cache
Loading model cost 0.748 seconds.
Prefix dict has been built succesfully.
['中国', '是', '一个', '伟大', '的', '国家']

jieba.lcut(s,cut_all = true) -全模式，返回一个列表类型的分词结果，存在冗余
例：
>>> jieba.lcut("中国是一个伟大的国家",cut_all = True)
['中国', '国是', '一个', '伟大', '的', '国家']

jieba.lcut_for_search(s) -搜索引擎模式，返回一个列表类型的分词结果，存在冗余
例：
>>> jieba.lcut_for_search("中华人民共和国是伟大的")
['中华', '华人', '人民', '共和', '共和国', '中华人民共和国', '是', '伟大', '的']

jieba.add_word(w) -向分词词库增加新词w
例：
>>>jieba.add_word("蟒蛇语言")
"""