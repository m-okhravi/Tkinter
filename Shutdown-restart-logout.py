from tkinter import *
import os


def shutdown():
    return os.system("shutdown /s /t l")


def restart():
    return os.system("shutdown /r /t l")


def logout():
    return os.system("shutdown -l")


master = Tk()
master.geometry("300x300")
master.title("this is cool")
master.configure(bg="light gray")


Button(master, text="Shutdown", command=shutdown).place(x=110, y=20)
Button(master, text="Restart", command=restart).place(x=110, y=50)
Button(master, text="Log out", command=logout).place(x=110, y=80)
mainloop()

