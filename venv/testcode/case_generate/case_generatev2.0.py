# -*- coding: GBK -*-
# ��һ�������ļ��ı����ʽ

case_html_f = "./˼ά��ͼ���ɰ���.html"

# ��ȡ.html�ļ��������ַ���
def get_case_file_str(case_html_file):
    with open(case_html_file, encoding="utf-8") as case_html_obj:
        case_html_str = case_html_obj.read()
    return case_html_str

case_str = get_case_file_str(case_html_f)
from bs4 import BeautifulSoup
case_soup = BeautifulSoup(case_str, "html.parser")
case_d = {"node": "text"}
case_div = case_soup.find(attrs="basetext")
case_root_text = case_div.div.text
print(case_root_text.strip())
print("case_div is " + case_div.name)
case_div_li = case_div.find(attrs="subexp")
for i in case_div_li.children:
    print(i.li.div)
