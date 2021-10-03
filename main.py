from tkinter import *
import pytest
import sqlite3
import body

@pytest.fixture()
def numbers():
    a ="bikks"
    b ="9841"
    return(a,b)
@pytest.mark.xfail
def test_method1():
    assert numbers[0] == bikks.get()
    assert numbers[0] == passw.get()

@pytest.mark.xfail
def test_method2():
    assert numbers[1] == bikks.get()
    assert numbers[1] == passw.get()

@pytest.mark.skip
def test_method3():
    assert numbers[0] == bikks.get()
    assert numbers[0] == passw.get()
@pytest.mark.skip
def test_method4():
    assert numbers[1] == bikks.get()
    assert numbers[1] == passw.get()




def check():
    if bikks.get() =="bikks" and passw.get() == "9841":
        call()
    else:
        user_entry.delete(0,END)
        password_entry.delete(0,END)
        label=Label(text="Details does not match",font=("times", "15", "bold")).pack()
        mainloop.destroy()
        login()

def call():
    body.root()




def login():
    mainroot = Tk()

    mainroot.geometry("600x500")
    mainroot.title("login")
    mainroot.config(bg="red")

    global user_entry
    global password_entry
    global bikks
    global passw

    bikks=StringVar()
    passw=StringVar()

    # =============== creating the entries and labels for the login =========================

    label1 = Label(mainroot, bg="yellow", text="Entry System", font=("times", "20", "bold"), width=400, height=2).pack()
    user_entry = Entry(mainroot, bg="white", fg="black",textvariable=bikks, font=("times", "20", "bold"))
    user_entry.pack()
    user = Label(mainroot, bg="red", text="User Name", font=("times", "20", "bold"), width=40, height=2).pack()
    password_entry = Entry(mainroot, bg="white", fg="black",textvariable=passw, font=("times", "20", "bold"))
    password_entry.pack()
    password = Label(mainroot, bg="red", text="Password", font=("times", "20", "bold"), width=40, height=2).pack()
    login = Button(mainroot, bg="ghost white", font=("times", "15", "bold"), text="Login", command=check).pack()

    mainloop()

login()