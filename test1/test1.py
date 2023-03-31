import tkinter as tk

def bt_event():


    label2 = tk.Label(text = textBox1.get() + "                            ")
    label2.place(x = 350, y = 400)

root = tk.Tk()

root.title("ベルンのテキストプログラム")
root.geometry("800x600")
root.resizable(width = False, height = False)

label1 = tk.Label(text = "ベルンのテキストプログラム")
label1.place(x = 350, y = 100)

textBox1 = tk.Entry(width = "40")
textBox1.place(x = 300, y = 200)

button1 = tk.Button(text = "押せ", command = bt_event)
button1.place(x = 390, y = 300)

tk.mainloop()