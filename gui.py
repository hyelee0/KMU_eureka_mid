
import AES128_img, PIPO128_img
from pathlib import Path 
import webbrowser

from tkinter import *
from tkinter import messagebox as msgbox 
from tkinter import filedialog as fd
from PIL import Image, ImageTk

root = Tk() 
root.title('◈ ENCRYPT and DECRYPT your image file ◈ --------------------------------------------------------------------------------------------- ◈')  
root.geometry('900x600+400+300') 
root.config(background='#dbd8e3')
root.resizable(False, False)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

default = Image.open('black.jpg').resize((250, 250))
before_image = ImageTk.PhotoImage(default)
before_label = Label(root, image=before_image, relief='ridge', bd=5)
before_label.place(x=40, y=40)
after_image = ImageTk.PhotoImage(default)
after_label = Label(root, image=after_image, relief='ridge', bd=5)
after_label.place(x=600, y=40)
Label(root, text='------------- ◔ BEFORE ◔ ---------------------------------------------------------------- ◕ AFTER ◕ ----------------', font='나눔고딕 15', bg='#dbd8e3').place(y=320)

aframe = Frame(root, padx=9, pady=8, relief='groove', bd=2)
aframe.place(x=347, y=50)
Label(aframe, text='▶ APPLY', font='나눔고딕 13').pack()
apply_var = StringVar(value='iv')
apply1 = Radiobutton(aframe, value='enc', variable=apply_var, width=7, pady=7, text='암호화', font='나눔고딕 11')
apply2 = Radiobutton(aframe, value='dec', variable=apply_var, width=7, pady=7, text='복호화', font='나눔고딕 11')
apply1.pack(side='left')
apply2.pack(side='right')

cframe = Frame(root, padx=4, pady=8, relief='groove', bd=2)
cframe.place(x=345, y=135)
Label(cframe, text='▶ CIPHER', font='나눔고딕 13').pack()
cipher_var = StringVar(value='iv')
cipher1 = Radiobutton(cframe, value='aes', variable=cipher_var, width=7, pady=7, text='AES', font='나눔고딕 11')
cipher2 = Radiobutton(cframe, value='pipo', variable=cipher_var, width=7, pady=7, text='PIPO', font='나눔고딕 11')
cipher1.pack()
cipher2.pack()
Label(cframe, pady=10, text='').pack()

mframe = Frame(root, padx=4, pady=8, relief='groove', bd=2)
mframe.place(x=450, y=135)
Label(mframe, text='▶ MODE', font='나눔고딕 13').pack()
mode_var = StringVar(value='iv')
mode1 = Radiobutton(mframe, value='ecb', variable=mode_var, width=7, pady=7, text='ECB', font='나눔고딕 11')
mode2 = Radiobutton(mframe, value='cbc', variable=mode_var, width=7, pady=7, text='CBC', font='나눔고딕 11')
mode3 = Radiobutton(mframe, value='ctr', variable=mode_var, width=7, pady=7, text='CTR', font='나눔고딕 11')
mode1.pack()
mode2.pack()
mode3.pack()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def showImage(in_file, change='after'):
    global default
    global before_image
    global after_image
    default = Image.open(in_file)
    #wpercent = 250/float(default.size[0])
    #hsize = int(float(default.size[1]) * float(wpercent))
    default = default.resize((250, 250))
    if change == 'before':
        before_image = ImageTk.PhotoImage(default)
        before_label.config(image=before_image)
    else:
        after_image = ImageTk.PhotoImage(default)
        after_label.config(image=after_image)

in_file, out_path = '', ''
def fileChoice():
    global in_file 
    global default
    global before_image
    global after_image
    while True:
        in_file = fd.askopenfilename(title='이미지 파일을 선택하세요', initialdir='C:/', \
            filetypes=[('모든 파일', '*.*'), ('PNG 파일', '*.png'), ('JPG 파일', '*.jpg'), ('GIF 파일', '*.gif')])
        if in_file == '':
            response = msgbox.askretrycancel('✔ 확인', '파일이 선택되지 않았습니다. 다시 선택하시겠습니까?')
            if response == True:
                continue
        elif Path(in_file).suffix not in ('.png', '.jpg', '.jpeg', '.gif'):
            msgbox.showerror('✔ 주의', '이미지파일을 선택하세요.')
            return
        showImage(in_file, 'before')
        showfc_lab.config(text=Path(in_file).name) 
        break
def pathChoice(): 
    global out_path
    while True:
        out_path = fd.askdirectory(title='저장할 폴더를 선택하세요', initialdir='C:/')
        if out_path == '':
            response = msgbox.askretrycancel('✔ 확인', '폴더가 선택되지 않았습니다. 다시 선택하시겠습니까?')
            if response == True:
                continue
        elif out_path == 'C:/':
            showpc_lab.config(text='C드라이브')
        elif out_path == 'D:/':
            showpc_lab.config(text='D드라이브')
        else:
            showpc_lab.config(text=Path(out_path).name) 
        break
def clearChoice():
    global in_file
    global out_path 
    global save_path
    global state_label
    showImage('black.jpg', 'before')
    showImage('black.jpg')
    in_file, out_path, save_path = '', '', ''
    showfc_lab.config(text='')
    showpc_lab.config(text='')
    apply_var.set('iv')
    cipher_var.set('iv')
    mode_var.set('iv')
    state_label.config(text='▶ 현재 상태: 진행 전')

tframe = Frame(root, width=820, height=190, relief='groove', bd=3)
tframe.place(x=40, y=370)

fframe = Frame(root, padx=25, pady=23, relief='sunken', bd=4, bg='#e7e8f2')
fframe.place(x=75, y=398)
filechoice_btn = Button(fframe, command=fileChoice, width=12, pady=15, text='파일 선택', font='나눔고딕 12', bg='#b9bae3')
filechoice_btn.pack()
showfc_lab = Label(fframe, bg='#eaebf4')
showfc_lab.pack()

pframe = Frame(root, padx=25, pady=23, relief='sunken', bd=4, bg='#e7e8f2')
pframe.place(x=645, y=398)
pathchoice_btn = Button(pframe, command=pathChoice, width=12, pady=15, text='경로 선택', font='나눔고딕 12', bg='#b9bae3')
pathchoice_btn.pack()
showpc_lab = Label(pframe, bg='#eaebf4')
showpc_lab.pack()

clearchoice_btn = Button(root, command=clearChoice, width=12, pady=15, text='초기화', font='나눔고딕 12', bg='#dfe3f1')
clearchoice_btn.place(x=319, y=453)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

save_path = ''
def withAES():
    global in_file
    global out_path
    global save_path
    if tmpList[0] == 'enc':
        if tmpList[2] == 'ecb':
            out_file = out_path + '/enc_AESxECB' + Path(in_file).suffix
            AES128_img.imageEncrypt_ECB(in_file, out_file)
        elif tmpList[2] == 'cbc':
            out_file = out_path + '/enc_AESxCBC' + Path(in_file).suffix
            AES128_img.imageEncrypt_CBC(in_file, out_file)
        elif tmpList[2] == 'ctr':
            out_file = out_path + '/enc_AESxCTR' + Path(in_file).suffix
            AES128_img.imageEncrypt_CTR(in_file, out_file)  
        state_label.config(text='▶ 현재 상태: 암호화 완료')
        msgbox.showinfo('✔ 알림', '암호화가 완료되었습니다.\n폴더를 열어 확인하세요.')
    elif tmpList[0] == 'dec':
        if tmpList[2] == 'ecb':
            out_file = out_path + '/dec_AESxECB' + Path(in_file).suffix
            AES128_img.imageDecrypt_ECB(in_file, out_file)
        elif tmpList[2] == 'cbc':
            out_file = out_path + '/dec_AESxCBC' + Path(in_file).suffix
            AES128_img.imageDecrypt_CBC(in_file, out_file)
        elif tmpList[2] == 'ctr':
            out_file = out_path + '/dec_AESxCTR' + Path(in_file).suffix
            AES128_img.imageDecrypt_CTR(in_file, out_file)   
        state_label.config(text='▶ 현재 상태: 복호화 완료')
        msgbox.showinfo('✔ 알림', '복호화가 완료되었습니다.\n폴더를 열어 확인하세요.')
    showImage(out_file)
    save_path = out_path
    #in_file, out_path = '', ''
    #showfc_lab.config(text='')
    #showpc_lab.config(text='')
    #apply_var.set('iv')
    #cipher_var.set('iv')
    #mode_var.set('iv')

def withPIPO():
    global in_file
    global out_path
    global save_path
    if tmpList[0] == 'enc':
        if tmpList[2] == 'ecb':
            out_file = out_path + '/enc_PIPOxECB' + Path(in_file).suffix
            PIPO128_img.imageEncrypt_ECB(in_file, out_file)
        elif tmpList[2] == 'cbc':
            out_file = out_path + '/enc_PIPOxCBC' + Path(in_file).suffix
            PIPO128_img.imageEncrypt_CBC(in_file, out_file)
        elif tmpList[2] == 'ctr':
            out_file = out_path + '/enc_PIPOxCTR' + Path(in_file).suffix
            PIPO128_img.imageEncrypt_CTR(in_file, out_file)  
        state_label.config(text='▶ 현재 상태: 암호화 완료')
        msgbox.showinfo('✔ 알림', '암호화가 완료되었습니다.\n폴더를 열어 확인하세요.')
    elif tmpList[0] == 'dec':
        if tmpList[2] == 'ecb':
            out_file = out_path + '/dec_PIPOxECB' + Path(in_file).suffix
            PIPO128_img.imageDecrypt_ECB(in_file, out_file)
        elif tmpList[2] == 'cbc':
            out_file = out_path + '/dec_PIPOxCBC' + Path(in_file).suffix
            PIPO128_img.imageDecrypt_CBC(in_file, out_file)
        elif tmpList[2] == 'ctr':
            out_file = out_path + '/dec_PIPOxCTR' + Path(in_file).suffix
            PIPO128_img.imageDecrypt_CTR(in_file, out_file)   
        state_label.config(text='▶ 현재 상태: 복호화 완료')
        msgbox.showinfo('✔ 알림', '복호화가 완료되었습니다.\n폴더를 열어 확인하세요.')
    showImage(out_file)
    save_path = out_path
    #in_file, out_path = '', ''
    #showfc_lab.config(text='')
    #showpc_lab.config(text='')
    #apply_var.set('iv')
    #cipher_var.set('iv')
    #mode_var.set('iv')
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def userChoice():
    global in_file
    global out_path
    global tmpList
    global state_label
    if in_file == '' or out_path == '':
        msgbox.showerror('✔ 주의', '파일과 경로를 모두 선택하세요.')
        return
    tmpList = [apply_var.get(), cipher_var.get(), mode_var.get()]
    if 'iv' in tmpList:
        msgbox.showerror('✔ 주의', '모든 방식을 선택하세요.')
    elif tmpList[1] == 'aes' and msgbox.askyesno('✔ 확인', '정말 진행하시겠습니까?') == True:
        withAES()
    elif tmpList[1] == 'pipo' and msgbox.askyesno('✔ 확인', '정말 진행하시겠습니까?') == True:
        withPIPO()
    
def pathsave():
    global save_path
    if save_path == '':
        msgbox.showerror('✔ 주의', '아직 완료되지 않았습니다.')
    else:
        webbrowser.open(save_path)

start_btn = Button(root, command=userChoice, width=12, pady=15, text='시작', font='나눔고딕 12', bg='#c2c9ea')
start_btn.place(x=380, y=390)

state_label = Label(root, text='▶ 현재 상태: 진행 전', font='나눔고딕 13')
state_label.place(x=365, y=520)

check_btn = Button(root, command=pathsave, width=12, pady=15, text='열어보기', font='나눔고딕 12', bg='#dfe3f1')
check_btn.place(x=450, y=453)

root.mainloop()

