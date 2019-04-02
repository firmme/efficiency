import tkinter as tk

window = tk.Tk()
window.title("网管工具箱")

window.geometry("500x300")
var = tk.StringVar()
on_click = False
var.set("Click button")

label1 = tk.Label(window, textvariable=var, bg="#f8eec7", font=('Comic Sans MS', '12'), width=30, height=2)

label1.pack()


def clickfunc():
    global on_click
    if on_click:
        var.set("Click button")
        on_click = False
    else:
        var.set("GUN")
        on_click = True


def insert_point():
    var = entry1.get()
    text1.insert("insert", var)


def insert_end():
    var = entry1.get()
    text1.insert("end", var)


button1 = tk.Button(window, text="click", width=15, height=2, command=clickfunc)
button1.pack()
button2 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
button2.pack(side="left")

button3 = tk.Button(window, text="insert end", width=15, height=2, command=insert_end)
button3.pack(side="right")

entry1 = tk.Entry(window, show=None)
entry1.pack()

text1 = tk.Text(window, height=3)
text1.pack()
window.mainloop()
