import tkinter as tk

file1 = ""
fp1 = ""

def bt1_act():
    global file1
    file1 = tb1.get()

    try:
        fp1 = open(file1)
    except OSError as e:
        lb1["text"] = e
    else:
        lb1["text"] = fp1.read()
        fp1.close()

root = tk.Tk()
root.title("ベルンのファイル内容表示プログラム")
root.geometry("800x600")
root.resizable(width = False, height = False)

tb1 = tk.Entry(width = 80)
tb1.place(x = 150, y = 200)

bt1 = tk.Button(text = "ファイルを獲得", command = bt1_act)
bt1.place(x = 350, y = 300)

lb1 = tk.Label(text = file1)
lb1.place(x = 150, y = 400)

tk.mainloop()