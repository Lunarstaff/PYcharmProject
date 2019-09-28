# subprocess_001.py
import subprocess
print("执行命令： nslookup www.python.org")
r = subprocess.call(["nslookup", "www.python.org"])
print("Exit code:", r)
