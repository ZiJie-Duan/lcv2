from su.aes import encrypt, decrypt

input_text = "abc"
secret_key = "my_sec_key"

encrypted = encrypt(secret_key, input_text)

print(encrypted)


decrypted = decrypt(secret_key, encrypted)

print(decrypted)