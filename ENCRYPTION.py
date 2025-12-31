import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)

key = chars.copy()

random.shuffle(key)

# print(f"chars:{chars}")
# print(f"key:{key}")

# ENCRYPT
plain_text = input("ENTER TEXT:")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"ENCRYPTED TEXT:{cipher_text}")

# DECRYPT

cipher_text = input("ENTER TEXT:")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"DECRYPTED TEXT: {plain_text}")
