# PYcharmProject 说明

![Alt text](./image/pycharm.jpg)

>---
### 说明
    - Linux中Git使用
    - Linux中的Python环境
    - Pycharm-GitHub-使用
    - 在Linux中安装git
    - 在readme.md文件中显示图片
    - 手动安装第三方库
>---
### 异常记录
>---
### Markdown 语法说明[<sup>参考1</sup>][参考1]
+ 展示代码
  
    1、高亮语句中的某个函数名或关键字  
    >使用\` \`框住高亮语句中的某个函数名或关键字，像这样\`class\`,\`import\`,\`for\`会展示为如下效果：
    `class`,`import`,`for`
    
    2、高亮一段代码，并指定一种语言      
    >使用\``` \```框住高亮语句的一段代码，并在\```后面指定某种语言，像这样  
    \```python  
    def getText():  
    txt = open("hamlet.txt", "r").read()  
    txt = txt.lower()  
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':  
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格  
    return txt  
    \````  
    会展示为如下效果:  
    ```python
    def getText():
        txt = open("hamlet.txt", "r").read()
        txt = txt.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
            txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
        return txt
    ```
    3、也可以使用4空格缩进，再贴上代码，实现相同的的效果  

+ 链接  
    1、文本链接  
    ```  
    [百度](https://www.baidu.com/)
    ```  
    [百度](https://www.baidu.com/)  
    [知了智能主页](https://zhi.hao123.com/)  
    
    2、网址链接  
    ```
    <https://www.baidu.com/>
    ```
    <https://www.baidu.com/>
    
    3、高级链接
    >给链接定义变量名，在下方给变量赋值
    ```
    这个链接用 baidu 作为网址变量 [www.baidu.com][baidu]  
    这个链接用 知了 作为网址变量 [知了智能主页][知了]  
    这个链接用 1 作为网址变量 [hao123][1]  
    然后在文档的结尾为变量赋值（网址）
    
    [1]: http://www.hao123.com/  
    [baidu]: https://www.baidu.com/  
    [知了]: https://zhi.hao123.com/  
    ```
    这个链接用 baidu 作为网址变量 [www.baidu.com][baidu]  
    这个链接用 知了 作为网址变量 [知了智能主页][知了]  
    这个链接用 1 作为网址变量 [hao123][1]  
    然后在文档的结尾为变量赋值（网址）
    
    [1]: https://www.hao123.com/  
    [baidu]: https://www.baidu.com/  
    [知了]: https://zhi.hao123.com/  
    

+ 图片  
    >1、跟链接的方法区别在于前面加了个感叹号 !  
    
    ```
    ![百度](image/badu_logo.gif)
    ![知了](image/zhiliao_logo.png)    
    ```  
    ![百度](image/badu_logo.gif)
    ![知了](image/zhiliao_logo.png)  
    >2、也可以给图片链接定义变量，注意变量名不能重复
    ```
    ![百度][1]
    ![知了][知了_logo]  
    
    [1]: ./image/badu_logo.gif
    [知了_logo]: ./image/zhiliao_logo.png
    ```
    ![百度][3]
    ![知了][知了_logo]  
    
    [3]: ./image/badu_logo.gif
    [知了_logo]: ./image/zhiliao_logo.png


+ 文本  
    1、脚标[<sup>参考2</sup>][参考2]  
    2、斜体粗体字
 
+ emoji[网址](https://www.webfx.com/tools/emoji-cheat-sheet/ "emoji")
中国国旗：  
:cn:  
晴天：  
:sunny:


+ PyCharm 2019.1.4 (Community Edition) 这个版本还有很多markdown语法不支持，  
可以参考[mdeditor][参考3]

```
PyCharm 2019.1.4 (Community Edition)
Build #PC-191.8026.44, built on July 30, 2019
JRE: 11.0.2+9-b159.64 amd64
JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
Windows 10 10.0
```


>---
[参考1]: https://segmentfault.com/markdown/
[参考2]: https://www.jianshu.com/p/13b3366f0260
[参考3]: https://www.mdeditor.com/ "www.mdeditor.com"
