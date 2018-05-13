#wordcloud-test.py
'''
词云展示库：wordcloud
wordcloud 安装：
Windows（cmd命令）：pip install wordcloud

wordcloud库把词云当作一个WordCloud对象
    -wordcloud.WordCloud() 代表一个文本对应的词云
    -可以根据文本中词语出现的频率等参数绘制词云
    -绘制词云的形状、尺寸和颜色都可以设定

w = wordcloud.WordCloud()
    -以WordCloud对象为基础
    -配置参数、加载文本、输出文件

w.generate(txt) #向WordCloud对象w中加载文本txt
    >>> import wordcloud
    >>> w = wordcloud.WordCloud()
    >>> w.generate("Python and WordCloud")

w.to_file(filename) #将词云输出为图像文件，.png或.jpg格式
    >>> w.to_file("outfile.png")
    <wordcloud.wordcloud.WordCloud object at 0x000001F1449D8EF0>

例1：
    import wordcloud
    w = wordcloud.WordCloud()
    w.generate("Python and WordCloud")
        #1-分隔：以空格分隔单词
        #2-统计：单词出现资料并过滤（会将很短的单词过滤掉）
        #3-字体：根据统计配置字号
        #4-布局：颜色环境尺寸
    w.to_file("outfile.png") #输出文件没有指定目录，默认为当前项目根目录：“C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject”



wordclout 库常规方法：
    -步骤1：配置对象参数
    -步骤2：加载词云文本
    -步骤3：输出词云文件

配置对象参数：
    w = wordcloud.WordCloud(<参数>)
        -width  指定词云对象生成图片的宽度，默认为400像素
                例：>>> w = wordcloud.WordCloud(width = 600)
        -heigth 指定词云对象生成图片的高度，默认为200像素
                例：>>> w = wordcloud.WordCloud(heigth = 400)
        -min_font_size  指定词云中字体的最小字号，默认为4号
                        例：>>> w = wordcloud.WordCloud(min_font_size = 10)
        -max_font_size  指定词云中字体的最大字号，根据高度自动调节
                        例：>>> w = wordcloud.WordCloud(max_font_size = 20)
        -font_step      指定词云中字体字号的步进间隔，默认为1
                        例：>>> w = wordcloud.WordCloud(font_step = 2)
        -font_path      指定字体文件的路径，默认为None
                        例：>>> w = wordcloud.WordCloud(font_path = "msyt.ttc")#msty.ttc-微软雅黑
        -max_words      指定词云显示的最大单词数量，默认为200
                        例：>>> w = wordcloud.WordCloud(max_words = 20)
        -stop_words     指定词云的排除列表，即不显示的单词列表
                        例：>>> w = wordcloud.WordCloud(stop_words = {"Python"})#{"Python"}为集合类型
        -mask   指定词云形状，默认为长方形，需要引用imread()函数
                例: >>> from scipy.misc import imread
                    >>> mk = imread("pci.png")
                    >>> w = wordcloud.WordCloud（mask = mk）
        -background_color   指定词云图片的背景颜色，默认为黑色
                            例：>>> w = wordcloud.WordCloud（background_color = "white"）

'''
#例2：
import wordcloud
txt = "life is short, you need python"
w = wordcloud.WordCloud(background_color="white")
w.generate(txt)
w.to_file("pywcloud.png")
