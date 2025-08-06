import tkinter as tk
from tkinter import font
import keyboard
from time import sleep
import pyautogui as pya
import threading as th
import random

pya.PAUSE=0

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("512x384")
        self.minsize(512,384)
        self.maxsize(512,384)

        self.bold=font.Font(family="Javanese Text",size="12",weight="bold")

        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        for F in (MainPage,Credits):
            page_name = F.__name__
            frame=F(parent=container,cont=self)
            self.frames[page_name]=frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, cont):
        tk.Frame.__init__(self,parent)
        self.clickThread=th.Thread(target=self.clicks)
        self.clicking = False
        self.clickSpeed=1000
        self.clickVary=0
        self.cont = cont

        #Clicking -indicator
        self.ClickingOnLabel = tk.Label(self,text="OFF",font=cont.bold,bg="red")
        self.ClickingOnLabel.place(relx=0.5,rely=0.05,anchor="center",height="25")
        ShortcutLabel = tk.Label(self,text="CTRL + ALT + C")
        ShortcutLabel.place(relx=0.5,rely=0.1,anchor="center")

        #ClickSpeed text & entry
        ClickSpeedLabel = tk.Label(self,text="Click Speed",font=cont.bold)
        ClickSpeedLabel.place(relx=0.5,rely=0.2,anchor="center")
        MeasurementLabel = tk.Label(self,text="(ms)")
        MeasurementLabel.place(relx=0.5,rely=0.235,anchor="center")
        self.ClickSpeedEntry = tk.Entry(self,justify="center")
        self.ClickSpeedEntry.place(relx=0.5,rely=0.3,anchor="center")
        self.ClickSpeedEntry.insert(0,str(self.clickSpeed))

        #ClickSpeedVary text & entry
        ClickVaryLabel = tk.Label(self,text="Click Vary",font=cont.bold)
        ClickVaryLabel.place(relx=0.8,rely=0.2,anchor="center")
        MeasurementLabel = tk.Label(self,text="(ms)")
        MeasurementLabel.place(relx=0.8,rely=0.235,anchor="center")
        self.ClickVaryEntry = tk.Entry(self,justify="center")
        self.ClickVaryEntry.place(relx=0.8,rely=0.3,anchor="center",width="75")
        self.ClickVaryEntry.insert(0,str(self.clickVary))

        keyboard.add_hotkey('ctrl+alt+c', self.startClick)

    def startClick(self):
        self.clickSpeed=int(self.ClickSpeedEntry.get())
        self.clickVary=int(self.ClickVaryEntry.get())
        self.clicking = not self.clicking
        if self.clicking:
            self.ClickingOnLabel.config(text="ON",bg="lightgreen")
            try:
                self.clickThread.start()
            except RuntimeError:
                self.clickThread=th.Thread(target=self.clicks)
                self.clickThread.start()
        else:
            self.ClickingOnLabel.config(text="OFF",bg="red")

    def clicks(self):
        while True:
            if not self.clicking:
                break
            pya.click()
            sleep((self.clickSpeed/1000)+(random.randint(0,self.clickVary)/1000))
            if self.clickSpeed != int(self.ClickSpeedEntry.get()):
                self.startClick()
                break
        

class Credits(tk.Frame):
    def __init__(self,parent,cont):
        tk.Frame.__init__(self,parent)
        self.cont=cont
        Title=tk.Label(self,text="Credits")
        Title.grid(column=0,row=0)
        button = tk.Button(self,text="Leave credits",command=lambda: cont.show_frame("StartPage"))
        button.grid(column=0,row=1,sticky="W")

if __name__=="__main__":
    app=Main()
    app.mainloop()