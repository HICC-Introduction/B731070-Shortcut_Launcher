from tkinter import *
from PIL import ImageTk, Image
import subprocess
import os
import webbrowser

Turbo = Tk() # 창 생성

Turbo.geometry("800x200")       # 창 크기 조절
Turbo.title("TurboLaunch")      # 창 제목

def notepad():                  # 메모장 실행 함수
    subprocess.run('notepad')
def calculator():               # 계산기 실행 함수
    subprocess.run('calc')
def c():                        # C 폴더 실행 함수
    os.startfile('c:')
def google():                   # 구글 실행 함수
    webbrowser.open('http://google.com') 

def_name = [notepad, calculator, c, google] # 함수이름 리스트

image_name = ["notepad.png", "calculator.png", "C드라이브.png", "Google.png", "trapcard.png"] # 이미지 위치를 저장한 리스트
image = []       # 원본 이미지를 저장하는 리스트
new_image = []   # 크기를 조정한 이미지를 저장하는 리스트

for i in range(len(image_name)):
    image.append(Image.open(image_name[i])) # 원본 이미지 저장
    new_image.append(ImageTk.PhotoImage(image[i].resize((80, 80), Image.ANTIALIAS))) # 40x40의 크기로 변환 후 리스트에 저장

def trap_card():                # 함정카드 발동
    for trap_num in range(4, 8):
        btn_list[trap_num].config(image = new_image[4]) # 나머지 버튼을 함정카드로 채운다.

btn_list = []                   # 버튼 리스트 생성
for row_btn in range(2):        # 2행
    for col_btn in range(4):    # 4열
        btn = Button(Turbo)     # 버튼 생성
        btn.config(image = new_image[col_btn]) # 버튼 이미지 넣기 
        if(row_btn < 1):        # 1행일 때만 메모장, 계산기 등의 기능 구현
            btn.config(command = def_name[col_btn]) # 버튼 기능 이식
        else:                   # 2행일 때는
            btn.config(command = trap_card)      # 함정카드 발동

        btn.grid(column = col_btn, row = row_btn, padx = 5, pady = 5) # 그리드 형식으로 버튼 생성
        btn_list.append(btn)    # 버튼을 리스트에 저장

Turbo.mainloop() 