import tkinter as tk
import random

class FontReturn():
    def title_messeage(self):
        return "ベルンのじゃんけんプログラム"

    def jan(self, hand):
        if hand == 0:
            return "グー"

        elif hand == 1:
            return "チョキ"

        else:
            return "パー"

    def judge_message(self, hantei):
        if hantei == 0:
            label2 = tk.Label(text = "引き分けです　　")
            label2.place(x = 350, y = 400)

        elif hantei == 1:
            label2 = tk.Label(text = "あなたの勝ちです")
            label2.place(x = 350, y = 400)

        else:
            label2 = tk.Label(text = "あなたの負けです")
            label2.place(x = 350, y = 400)

def guu():
    teki = random.randint(0, 2)

    if teki == 0:
        teki_mozi = "グー"

    elif teki == 1:
        teki_mozi = "チョキ"

    else:
        teki_mozi = "パー"

    label3["text"] = "自分:グー" + "敵:" + teki_mozi
    label3.place(x = 350, y = 350)

    if teki == 0:
        message = FontReturn()
        message.judge_message(0)

    elif teki == 1:
        message = FontReturn()
        message.judge_message(1)

    elif teki == 2:
        message = FontReturn()
        message.judge_message(2)

def choki():
    teki = random.randint(0, 2)

    if teki == 0:
        teki_mozi = "グー"

    elif teki == 1:
        teki_mozi = "チョキ"

    else:
        teki_mozi = "パー"

    label3["text"] = "自分:チョキ" + "敵:" + teki_mozi
    label3.place(x = 350, y = 350)

    if teki == 0:
        message = FontReturn()
        message.judge_message(2)

    elif teki == 1:
        message = FontReturn()
        message.judge_message(0)

    elif teki == 2:
        message = FontReturn()
        message.judge_message(1)

def paa():
    teki = random.randint(0, 2)

    if teki == 0:
        teki_mozi = "グー"

    elif teki == 1:
        teki_mozi = "チョキ"

    else:
        teki_mozi = "パー"

    label3["text"] = "自分:パー" + "敵:" + teki_mozi
    label3.place(x = 350, y = 350)

    if teki == 0:
        message = FontReturn()
        message.judge_message(1)

    elif teki == 1:
        message = FontReturn()
        message.judge_message(2)

    elif teki == 2:
        message = FontReturn()
        message.judge_message(0)

message = FontReturn()

root = tk.Tk()

root.geometry("800x600")
root.title(message.title_messeage())
root.resizable(width = False, height = False)

label1 = tk.Label(text = message.title_messeage())
label2 = tk.Label(text = "")
label3 = tk.Label(text = "")
button1 = tk.Button(text = message.jan(0), command = guu)
button2 = tk.Button(text = message.jan(1), command = choki)
button3 = tk.Button(text = message.jan(2), command = paa)

label1.place(x = 350, y = 100)
button1.place(x = 200, y = 250)
button2.place(x = 400, y = 250)
button3.place(x = 600, y = 250)

root.mainloop()