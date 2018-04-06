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
