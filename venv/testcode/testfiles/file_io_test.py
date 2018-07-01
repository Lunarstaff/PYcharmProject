'''
使用文本文件1（只读）：
C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\venv\testcode\testfiles\files-test.txt

文件内容：
i miss my blue blue sky
but aftet i left my home
blue blue sky is far away from me
and there is no star
i miss my blue blue sky
i miss my little little home

使用文本文件2（读写）：
C:\E-Data-File\腾讯课堂\Python入门\PYcharmProject\venv\testcode\testfiles\txt.txt

文件内容：
newline1
newline2
newline3

'''

#读文件
with open('files-test.txt') as fo:
    text = fo.read()
    print(text)