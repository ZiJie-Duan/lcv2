import base64

from Crypto.Cipher import AES


# str不是16的倍数那就补足为16的倍数
def add_to_16(text):
	while len(text) % 16 != 0:
		text += '\0'
	return str.encode(text)  # 返回bytes


#key = '123456'  # 密码

#text = 'abc123def456'  # 待加密文本

def adm(key,text):

	aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器

	encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')  # 加密
	return encrypted_text

def jm(key,encrypted_text):

	aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器

	text_decrypted = str(aes.decrypt(base64.decodebytes(bytes(encrypted_text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))  # 解密
	return text_decrypted

