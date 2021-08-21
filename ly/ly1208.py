def xor_encrypt(tips, key):
    ltips = len(tips)

    lkey = len(key)  # key长度

    secret = []  # 声明用于存放加密后内容的list

    num = 0

    for each in tips:

        if num >= lkey:
            num = num % lkey  # 将tips按照key的长度循环

        secret.append(chr(ord(each) ^ ord(key[num])))  # 将tips的ASCII码与key的ASCII码逐字异或进行加密，生成list

        num += 1

    return "".join(secret)  # 将加密后的list整合为字符串


def xor_decrypt(secret, key):
    tips = secret

    lkey = len(key)  # key长度

    secret = []  # # 声明用于存放解密后内容的list

    num = 0

    for each in tips:

        if num >= lkey:
            num = num % lkey  # 将tips按照key的长度循环

        secret.append(chr(ord(each) ^ ord(key[num])))  # 将tips的ASCII码与key的ASCII码逐字异或进行解密，生成list

        num += 1

    return "".join(secret)  # 将解密后的list整合为字符串


tips = "明天七点发动进攻"

key = "owen"

secret = xor_encrypt(tips, key)  # 加密

print("cipher_text:", secret)

plaintxt = xor_decrypt(secret, key)  # 解密

print("plain_text:", plaintxt)
