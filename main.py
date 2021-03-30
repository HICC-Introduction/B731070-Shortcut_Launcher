from tkinter import *
from PIL import ImageTk, Image
import subprocess

Turbo = Tk() # 창 생성

Turbo.geometry("800x200") # 창 크기 조절
Turbo.title("TurboLaunch") # 창 제목

def notepad(): # 메모장 실행 함수
    subprocess.run('notepad')

image = Image.open("C:\\Users\\Lenovo\\Desktop\\notepad.png") # 이미지 불러들임
resized_image = image.resize((40, 40), Image.ANTIALIAS)       # 40x40의 크기로 이미지 조정
new_image = ImageTk.PhotoImage(resized_image)                 # 40x40으로 맞춘 이미지 변수에 저장

btn = Button(Turbo) # 버튼 생성
btn.config(image = new_image) # 버튼 내용
btn.config(command = notepad) # 메모장 함수 실행
btn.grid(column = 0, row = 0, padx = 10, pady = 10)           # 그리드 형식을 버튼 생성

Turbo.mainloop()