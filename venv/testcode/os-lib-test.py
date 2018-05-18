'''
os库是Python标准库，包含几百个函数
常用路径操作、进程管理、环境参数等几类
    -路径 操作：os.path 子库，处理文件路径及信息
    -进程管理：启动系统中其他程序
    -环境参数：获得系统硬件信息等环境参数

路径操作：
    os.path子库以path为入口，用于操作和处理文件路径
    import os.path
    import os.path as op
        -os.path.abspath(path)  #返回path在当前系统中的绝对路径
            >>> help(op.abspath)
            Help on function abspath in module ntpath:

            abspath(path)
                Return the absolute version of a path.

        -os.path.normpath(path) #归一化path的表示形式，统一用\\分隔路径
            >>> help(op.normpath)
            Help on function normpath in module ntpath:

            normpath(path)
                Normalize path, eliminating double slashes, etc.

        -os.path.relpath(path)  #返回当前程序与文件之间的相对路径（relative path）
            >>> help(op.relpath)
            Help on function relpath in module ntpath:

            relpath(path, start=None)
                Return a relative version of a path

        -os.path.dirname(path)  #返回path中的目录名称
            >>> help(op.dirname)
            Help on function dirname in module ntpath:

            dirname(p)
                Returns the directory component of a pathname

        -os.path.basename(path) #返回path中最后的文件名称
            >>> help(op.basename)
            Help on function basename in module ntpath:

            basename(p)
                Returns the final component of a pathname

        -os.path.join(path,*paths)  #组合path与paths，反，回一个路径字符串
            >>> help(op.join)
            Help on function join in module ntpath:

            join(path, *paths)
                # Join two (or more) paths.

        -os.path.exists(path)   #判断path对应的文件或者目录是否存在，返回True或者False
            >>> help(op.exists)
            Help on function exists in module genericpath:

            exists(path)
                Test whether a path exists.  Returns False for broken symbolic links

        -os.path.isfile(path)   #判断path对应的是否是已存在的文件，返回True或者False
        -os.path.isdir(path)    #判断path对应的是否是已存在的目录，返回True或者False


        -os.path.getatime(path) #返回path对应文件或目录上一次的访问（access）时间
        -os.path.getmtime(path) #返回path对应文件或目录最近一次修改(modify)的时间
        -os.path.getctime(path) #返回path对应文件或目录的创建(creat)时间

        -os.path.getsize(path)  #返回path对应文件的大小，以字节为单位

进程管理：
    os.system(command)
        -执行程序或命令command
        -在Windows系统中，反回值为cmd的调用返回信息
            >>> import os
            >>> os.system("C:\\Windows\\System32\\calc.exe")
            0

环境参数：
    os.chdir(path)  #修改当前程序操作的路径
    os.getcwd()     #返回程序的当前路径
        >>> os.getcwd()
        'C:\\WINDOWS\\system32'
        >>> os.chdir(".\\..\\")
        >>> os.getcwd()
        'C:\\WINDOWS'

    os.getlogin()   #返回当前系统登记用户名称
    os.cpu_count()  #返回当前系统的CPU数量
        >>> os.getlogin()
        'Lunar12'
        >>> os.cpu_count()
        8

    os.urandom(n)   #获得n个长度的随机字符串，通常用于加解密运算
        >>> os.urandom(10)
        b'\x85\xa5\x1a\xf4\x8b\xcaR\x8c\xeb\xd4'

'''