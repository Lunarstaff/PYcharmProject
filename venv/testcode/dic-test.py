#dic-test.py
"""
字典类型
映射：是一种键（索引）和值（数据）的对应

创建一个空字典：
d = {}
增加值：
d["key1"] = "value1"

del d[k] 删除字典中键k对应的数据值
k in d 判断键k是否在字典d中，如果在返回True，否则返回False
d.keys() 返回字典d中所有的键值信息
d.values() 返回字典d中所有的值信息
d.items() 返回字段d中所有的键值对信息

d.get(k,<default>) 键k存在，则返回相应的值，不存在则返回<default>对应的值
d.pop(k,<default>) 键k存在，则取出相应的值，不存在则返回<default>对应的值
d.popitem() 随机从字典d中取出一个键值对，以元组形式返回
d.clear() 删除所有的键值对
len(d) 返回字典d中元素的个数


"""