import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror


class DecReport(Tk):
    def __init__(self): #기본 GUI
        Tk.__init__(self)
        self.title("TS for MDS")
        self.geometry("800x500+100+100")
        self.resizable(True, True)
        self.select_MDS()  

    def select_MDS(self): #장비 선택 창 나오게 하기
        self.selectframe = LabelFrame(self, text="장비 선택", labelanchor='n')
        self.selectframe.pack()
        self.selectResult = IntVar()
        self.selectMDS1=Radiobutton(self.selectframe, text="MDS", variable=self.selectResult, value="1") #1 MDS and MTA
        self.selectMDS1.pack()
        self.selectMDS2=Radiobutton(self.selectframe, text="MDS Manager", variable=self.selectResult, value="2") #1 MDS and MTA
        self.selectMDS2.pack()
        self.submutMDS = Button(self.selectframe, text="OK", command=self.load_file)
        self.submutMDS.pack()
  

    def load_file(self): #시스템 진단 보고서 열기 
        askopenfilename(filetypes=(("enc", "*.enc"),
                                       ("HTML files", "*.html;*.htm"),
                                       ("Text files", "*.text"),
                                       ("All files", "*.*") ))
        self.enter_password()
            
    def enter_password(self): #비밀번호 입력하기
        if self.selectResult.get() == 1:
            str = StringVar()
            self.lb1 = Label(self.selectframe, text='진단 보고서 비밀번호')
            self.lb1.pack()
            self.textbox = Entry(self.selectframe, width=20, textvariable=str)
            self.action = Button(self.selectframe, text = "Click", command=self.print_password)
            self.action.pack()
            self.textbox.pack()
                #Entry 입력 값을 prrintinput 에 전달 하고 싶은데...
        else:
            str = "MDS Manager 시스템 진단 보고서 파일이 선택되었습니다" #나중에는 MDS의 비밀번호가 입력될 수 있도록
            messagebox.showinfo("Button Clickec", str)

    def print_password(self): #SEED 알고리즘으로 복호화해야됨. 아직.. (decrypt_by seed algorithm)
        messagebox.showinfo("당신이 입력한 비번", self.textbox.get())

  
app = DecReport()
app.mainloop()