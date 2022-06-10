import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from PIL import Image
import random
import string

int_key = 326654965484733286517823092576650061268
key = int_key.to_bytes(16, 'little')
int_iv = 222319660015462502572442931603212116883
iv = int_iv.to_bytes(16, 'little')
int_noce = 12227642339409909085
nonce = int_noce.to_bytes(8, 'little')
block_size = 16

def trans_format_RGB(data):
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(red, green, blue))
    return pixels

def imageEncrypt_ECB(in_file, out_file): 
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    paddedtext = pad(value_vector, block_size) 
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_data = cipher.encrypt(paddedtext) 

    value_encrypt = trans_format_RGB(cipher_data[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

def imageEncrypt_CBC(in_file, out_file):
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    paddedtext = pad(value_vector, block_size) 
    cipher = AES.new(key, AES.MODE_CBC, iv=iv) 
    cipher_data = cipher.encrypt(paddedtext)

    value_encrypt = trans_format_RGB(cipher_data[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

def imageEncrypt_CTR(in_file, out_file): 
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    paddedtext = pad(value_vector, block_size) 
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    cipher_data = cipher.encrypt(paddedtext)

    value_encrypt = trans_format_RGB(cipher_data[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

def imageDecrypt_ECB(in_file, out_file):
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    decipher = AES.new(key, AES.MODE_ECB)
    decipher_data = decipher.decrypt(value_vector)

    value_encrypt = trans_format_RGB(decipher_data[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

def imageDecrypt_CBC(in_file, out_file): 
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    decipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decipher_data = decipher.decrypt(value_vector)

    value_encrypt = trans_format_RGB(decipher_data[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

def imageDecrypt_CTR(in_file, out_file): 
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    decipher = AES.new(key, AES.MODE_CTR, nonce=nonce) 
    decipher_data = decipher.decrypt(value_vector) 

    value_encrypt = trans_format_RGB(decipher_data[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)
