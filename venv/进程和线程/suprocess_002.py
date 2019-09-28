# suprocess_002.py
import subprocess

print("执行命令nslookup")
p = subprocess.Popen(["nslookup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
output, err = p.communicate(b"set q=mx\npython.org\nexit\n")
print("*"*18)
print(output.decode("gbk")) # 如果输出有乱码，可尝试使用其他常用编码格式"utf-8"
print("Exit code:", p.returncode)