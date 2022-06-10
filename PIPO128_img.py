# 불러온 파일에는 (ECB모드로, CBC모드로, CTR모드로) x (암호화, 복호화) --> 6개의 PIPO 알고리즘 함수들이 있음
import PIPO128_bin 
from PIL import Image

# 3가지의 랜덤한 비트열을 만듦 
# 암복호화를 할 때마다 필요한 secretkey / CBC모드에서 필요한 iv / CTR모드에서 필요한 nonce
from secrets import randbits 
secretkey =  326654965484733286517823092576650061268 
iv = 222319660015462502572442931603212116883
nonce = 12227642339409909085

def trans_format_RGB(data):
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(red, green, blue))
    return pixels

def bytes2int(input):
    output = 0
    for i in range(len(input)): 
        output = output << 8 | input[i]
    return output

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imageEncrypt_ECB(in_file, out_file):
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    plainblock_list = []
    for i in range(0, len(value_vector), 8): 
        binary_data = value_vector[i:i+8]
        plainblock = bytes2int(binary_data)
        plainblock_list.append(plainblock)

    cipherblock_list = PIPO128_bin.Encrypt_ECB(plainblock_list, secretkey)
    cipherimage = []
    for cipherblock in cipherblock_list:
        for i in range(8):
            int_data = (cipherblock >> 8*(7-i)) & 0xff
            cipherimage.append(int_data)

    value_encrypt = trans_format_RGB(cipherimage[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imageEncrypt_CBC(in_file, out_file):
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    plainblock_list = []
    for i in range(0, len(value_vector), 8): 
        binary_data = value_vector[i:i+8]
        plainblock = bytes2int(binary_data)
        plainblock_list.append(plainblock)
        
    cipherblock_list = PIPO128_bin.Encrpyt_CBC(iv, plainblock_list, secretkey)
    cipherimage = []
    for cipherblock in cipherblock_list:
        for i in range(8):
            int_data = (cipherblock >> 8*(7-i)) & 0xff
            cipherimage.append(int_data)

    value_encrypt = trans_format_RGB(cipherimage[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imageEncrypt_CTR(in_file, out_file):
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    plainblock_list = []
    for i in range(0, len(value_vector), 8): 
        binary_data = value_vector[i:i+8]
        plainblock = bytes2int(binary_data)
        plainblock_list.append(plainblock)
        
    cipherblock_list = PIPO128_bin.Common_CTR(nonce, plainblock_list, secretkey)
    cipherimage = []
    for cipherblock in cipherblock_list:
        for i in range(8):
            int_data = (cipherblock >> 8*(7-i)) & 0xff
            cipherimage.append(int_data)

    value_encrypt = trans_format_RGB(cipherimage[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imageDecrypt_ECB(in_file, out_file):
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    cipherblock_list = []
    for i in range(0, len(value_vector), 8): 
        binary_data = value_vector[i:i+8]
        cipherblock = bytes2int(binary_data)
        cipherblock_list.append(cipherblock)

    decipherblock_list = PIPO128_bin.Decrypt_ECB(cipherblock_list, secretkey)
    decipherimage = []
    for decipherblock in decipherblock_list:
        for i in range(8):
            int_data = (decipherblock >> 8*(7-i)) & 0xff
            decipherimage.append(int_data)

    value_encrypt = trans_format_RGB(decipherimage[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imageDecrypt_CBC(in_file, out_file):
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    cipherblock_list = []
    for i in range(0, len(value_vector), 8): 
        binary_data = value_vector[i:i+8]
        cipherblock = bytes2int(binary_data)
        cipherblock_list.append(cipherblock)
        
    decipherblock_list = PIPO128_bin.Decrypt_CBC(iv, cipherblock_list, secretkey)
    decipherimage = []
    for decipherblock in decipherblock_list:
        for i in range(8):
            int_data = (decipherblock >> 8*(7-i)) & 0xff
            decipherimage.append(int_data)
 
    value_encrypt = trans_format_RGB(decipherimage[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imageDecrypt_CTR(in_file, out_file):
    im = Image.open(in_file)
    value_vector = im.convert("RGB").tobytes()

    imlength = len(value_vector)
    cipherblock_list = []
    for i in range(0, len(value_vector), 8): 
        binary_data = value_vector[i:i+8]
        cipherblock = bytes2int(binary_data)
        cipherblock_list.append(cipherblock)

    decipherblock_list = PIPO128_bin.Common_CTR(nonce, cipherblock_list, secretkey)
    decipherimage = []
    for decipherblock in decipherblock_list:
        for i in range(8):
            int_data = (decipherblock >> 8*(7-i)) & 0xff
            decipherimage.append(int_data)

    value_encrypt = trans_format_RGB(decipherimage[:imlength])
    im2 = Image.new(im.mode, im.size)
    im2.putdata(value_encrypt)

    im2.save(out_file)