import requests
import os
url = 'https://www.duitang.com/blog/?id=188524677'
root = "C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\image"#定义根目录
path = root + url.split('/')[-1]#取得root加上文件名
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功，路径为：{}".format(path))
    else:
        print("文件已存在！")
except:
    print("爬取失败！")