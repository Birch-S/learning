# 对称密码体系
from Crypto.Cipher import AES
import base64

secret = "12345678912345678912345678912345"  # 由用户输入16或24或32位长的密钥字符串
cipher = AES.new(secret)  # 通过AES处理初始密码字符串，并返回cipher对象
txt = input("请输入要加密的内容:")
while len(txt) % 16 != 0:
    txt += '\0'  # 若不足16n位，补至16n位
s = cipher.encrypt(txt)  # 输入需要加密的字符串，注意字符串长度要是16的倍数。16,32,48..
print(s)
print(base64.b64encode(s))  # 输出加密后的字符串的base64编码。
print(cipher.decrypt(s).decode())  # 解密
