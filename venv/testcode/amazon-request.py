import requests
url_BooK_ID_B07922BZ99 = "https://www.amazon.cn/dp/B07922BZ99"
try:
    kv = {'user-agent':'Mozilla/5.0'}#通用请求文头参数 user-agent 指定用户引擎
    r = requests.get(url_BooK_ID_B07922BZ99) #获取响应的Response对象
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print("r.headers:{}".format(r.headers))
    print("r.text:".format(r.text[1000]))
except:
    print("错误！")



