import requests
url_baidu_search_api = "http://www.baidu.com/s" #百度搜索关键字的url
keyword = "Python" #关键字变量
try:
    kv = {'wd': keyword}  # 定义请求url参数中 wd对应的值
    r = requests.get(url_baidu_search_api, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.url) #打印响应报文对应的请求url
except:
    print("百度搜索失败！")

