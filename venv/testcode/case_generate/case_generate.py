# case_generate.py
"""
预期：
root,a1,b1
root,a1,b2
root,a1,b3
root,a2,b4
root,a2,b5
root,a3

line,deep
deep = h_max
line = h1_num * h2_num * h3_num * ... * hdeep_num

case {'root': root}
root {'a1': a1, 'a2': a2, 'a3': a3}
a1 {'b1': '', 'b2': '', 'b3': ''}

ls: [h1,h2,h3,...,h_max]
d:  h1 = {}
    h2 = {}




"""
from bs4 import BeautifulSoup

# 打开案例生成的html文件，读出内容返回为字符串（bs4可生成soup的内容）
def get_html_str(html_file):
    try:
        with open(html_file, "r") as html_file_obj:
            html_str = html_file_obj.read()
            return html_str
    except:
        print("读取案例生成的html文件异常！")

# 生成soup对象，
def get_soup(html_str):
    return BeautifulSoup(html_str, "html.parser")

# 找到案例根节点，返回根节点下面节点
def get_root(case_soup):
    # 获取root节点下所子节点
    body_children_ls = case_soup.body.children
    return body_children_ls

# 完成遍历并存储,返回树的深度和宽度
def run_1(case_ls):
    case_deepth = 0
    case_lines = 0
    case_ls_2 = []  # 数据清理后的列表
    for i in case_ls:
        print(i.name)
        try:
            if i != "\n":
                case_ls_2.append(i)
                print("+1")
                if i.child is None:
                    case_lines += 1     # 获取案例数
        except:
            print("run_1() 遍历跳过...")
    return case_ls_2    # , case_deepth, case_lines

# 生成案例：
def generat_case(case_list):
    print("generat_case")
    cases = {"tag_name": "tag_string"}
    t = 1
    for i in case_list:
        # print(i.name + ":\t" + i.text.strip())
        i_name = i.name
        if i_name in cases.keys():
            i_name = i_name + "_" + str(t)
            t += 1
        cases[i_name] = i.text.strip()
    for key in cases.keys():
        print(key + ":\t" + cases[key])
    print("X")


rootTestCaseHtml = "C:\\E-Data-File\\腾讯课堂\\Python入门\\PYcharmProject\\venv\\testcode\\case_generate\\root.html"
root_test_case_html_str = get_html_str(rootTestCaseHtml)
# print(root_test_case_html_str)
root_soup = get_soup(root_test_case_html_str)
# print(root_soup)
root_body = get_root(root_soup)
# print(root_body)
root_case_1 = run_1(root_body)
generat_case(root_case_1)
