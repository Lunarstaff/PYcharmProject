'''
从数据处理到人工智能：
    数据表示->数据清洗->数据统计->数据可视化->数据挖掘->人工智能

数据表示：采用合适方式用程序表达数据
数据清洗：数据归一化、数据转换、异常值处理
数据统计：数据的概要理解，数量、分布、中位数等
数据可视化：直观展示数据内涵的方式
数据挖掘：从数据分析获得知识，产生数据外的价值
人工智能：数据/语言/图像/视觉等方面尝试分析与决策

Python库之数据分析
    最基本的库 Numpy:表达N维数组的最基础的库
    http://www.numpy.org
        -Python接口使用，C语言实现，计算速度优异
        -Python数据 分析及科学计算的基础库，支撑Pandas等
        -提供直接的矩阵运算、广播函数、线性代数等功能

    Pandas:Python数据分析高层次应用库
    http://pandas.pydata.org
        -提供了简单易用的数据结构和数据分析工具
        -理解数据类型与索引的关系，操作索引即操作数据
        -Python最主要的数据分析功能库，基于Numpy开发

        Series = 索引 + 一维数据
        DataFrame = 行列索引 + 二维数据

    SciPy:数学、科学和工程计算功能
    http://www.scipy.org
        -提供了一批数学算法及工程数据运算功能
        -类似Matlab，可用于傅里叶变换、信号处理等应用
        -Python最主要的科学计算功能库，基于Numpy开发

Python库之数据可视化
    Matplotlib:高质量的二维护数据可视化功能库
        -提供了超过100种数据可视化展示效果
        -通过matplotlib.pyplot子库调用各可视化效果
        -Python最主要的数据可视化功能库，基于Numpy开发

    Seaborn:统计类数据可视化功能库
    http://seaborn.pydata.org
        -提供了一批高层次的数据可视化展示效果
        -主要展示数据间分布、分类和线性关系等
        -基于Matplotlib开发，支持Numpy和Pandas

    Mayavi:三维科学数据可视化功能库
    http://docs.enthought.com/mayavi/mayavi/
        -提供了一批简单易用的3D科学计算数据可视化展示效果
        -目前版本是Mayavi2，三维可视化最主要的第三方库
        -支持Numpy、TVTK、Traits、Envisage等第三方库


Python库之文本处理
    PyPDF2:用来处理pdf文件的工具集
    http:mstamy2.github.io/PyPDF2
        -提供了一批处理PDF文件的计算功能
        -支持获取信息、分隔/整合文件、加密解密等
        -完全Python语言主实现，不需要额外依赖，功能稳定

    NLTK：自然语言文本处理第三方库
    http://www.nltk.org
        -提供了一批简单易用的自然语言文本处理功能
        -支持语言文本分类、标记、语法语句、语义分析等
        -最优秀的Python自然语言处理库

    Python-docx:创建或更新Microsoft Word文件的第三方库
    http://python-docx.readthedocs.io/en/latest/index.html
        -提供创建或更新.doc、.docx等文件的计算功能
        -增加并配置段落、图片、表格、文字等，功能全面

Python库之机器学习
    Scikit-learn:机器学习方法工具集
    http://scikit-learn.org

    TensorFlow:AlphaGo背后的机器学习计算框架
    https://tensorflow.org
        -谷歌公司推动的开源机器学习框架
        -将数据流图作为基础，图节点代表运算，边代表张量
        -应用机器学习方法的一种方式，支撑谷歌人工智能应用

    MXNet:基于神经网络的深度学习计算框架
    https://mxnet.incubator.apache.org
        -提供可扩展的神经网络及深度学习计算功能
        -可用于自动驾驶、机器翻译、语音识别等众多领域
        -Python最重要的深度学习计算框架

'''