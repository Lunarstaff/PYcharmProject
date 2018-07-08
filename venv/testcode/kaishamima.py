password_mingwen = input("")
password_miwen = ''
alphabet_s = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(password_mingwen)):
    if password_mingwen[i] == ' ':
        password_miwen = password_miwen + ' '
    else:
        x = (alphabet_s.find(password_mingwen[i])+3)%26
        password_miwen = password_miwen + alphabet_s[x]
print(password_miwen)

# # 凯撒密码：
# alphabet_s = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# mingwen = input("")
# miwen = ""
# for i in mingwen:
#     if i in alphabet_s:
#         x = (alphabet_s.find(i) + 3) % 26
#         miwen = miwen + alphabet_s[x]
#     elif i in alphabet_S:
#         x = (alphabet_S.find(i) + 3) % 26
#         miwen = miwen + alphabet_S[x]
#     else:
#         miwen = miwen + i
# print(miwen)