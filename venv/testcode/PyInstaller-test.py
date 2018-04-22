#PyInstaller-test.py
"""
PyInstaller库的使用
将源程序编译打包成一个独立执行的程序

PyInstaller的安装

pip install pyinstaller

在Windows命令行中使用 pyinstaller 命令，如下：

 C:\E-Data-File\腾讯课堂\Python入门\Code>dir cl*
 驱动器 C 中的卷是 Windows
 卷的序列号是 CC7A-4265

C:\E-Data-File\腾讯课堂\Python入门\Code 的目录

2018/03/25  18:48             3,835 clock.py
2018/03/25  18:46             3,643 clock.py.bak
               2 个文件          7,478 字节
               0 个目录 71,220,191,232 可用字节

C:\E-Data-File\腾讯课堂\Python入门\Code>pyinstaller -F clock.py

在当前目录下会生成三个新的目录：
build
dist
__pycache__

其中在 dist 目录下有一个 对应py文件生成的 windows可执行程序：clock.exe
这个就是目的程序，在windows中双击可执行


pyinstaller命令的其他参数
-h 查看帮助
--clean 清理打包过程中产生的临时文件
-D,--onedir 默认值，生成dist文件夹
-F,--onefile 在dist文件夹中只生成独立的打包文件
-i<图标文件名.ico> 指定打包程序使用的图标（icon）文件
C:\E-Data-File\腾讯课堂\Python入门\Code\resources\images\clock.ico
"""
