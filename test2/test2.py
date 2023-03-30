import tkinter as tk
import random

class FontReturn():
    def title_messeage(self):
        return "ベルンのランダム得点プログラム"

    def jan(self, hand):
        return "ポイント"

def keisan():
    point = random.randint(0, 100)
    label2["text"] = str(point)
    label3["text"] = "今日の得点は" + str(point) + "点です"

root = tk.Tk()

message = FontReturn()

root.geometry("800x600")
root.title(message.title_messeage())
root.resizable(width = False, height = False)

label1 = tk.Label(text = message.title_messeage())
label2 = tk.Label(text = "")
label3 = tk.Label(text = "")

label1.place(x = 350, y = 100)
label2.place(x = 390, y = 350)
label3.place(x = 350, y = 400)

button1 = tk.Button(text = message.jan(0), command = keisan)
button1.place(x = 380, y = 250)

root.mainloop()