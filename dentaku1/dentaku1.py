import tkinter as tk

number = 0 #計算結果
plus = 0   #追加の値

class Num_calc():
    def num_calc_1(self): #1が押された時の処理
        global plus

        if plus == 0:
            plus = 1

        else:
            plus = plus * 10 + 1

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_2(self): #2が押された時の処理
        global plus

        if plus == 0:
            plus = 2

        else:
            plus = plus * 10 + 2

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_3(self):  # 3が押された時の処理
        global plus

        if plus == 0:
            plus = 3

        else:
            plus = plus * 10 + 3

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_4(self):  # 4が押された時の処理
        global plus

        if plus == 0:
            plus = 4

        else:
            plus = plus * 10 + 4

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_5(self): #5が押された時の処理
        global plus

        if plus == 0:
            plus = 5

        else:
            plus = plus * 10 + 5

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_6(self): #6が押された時の処理
        global plus

        if plus == 0:
            plus = 6

        else:
            plus = plus * 10 + 6

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_7(self):  # 7が押された時の処理
        global plus

        if plus == 0:
            plus = 7

        else:
            plus = plus * 10 + 7

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_8(self):  # 8が押された時の処理
        global plus

        if plus == 0:
            plus = 8

        else:
            plus = plus * 10 + 8

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_9(self):  # 9が押された時の処理
        global plus

        if plus == 0:
            plus = 9

        else:
            plus = plus * 10 + 9

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_calc_0(self):  # 0が押された時の処理
        global plus

        if plus == 0:
            plus = 0

        else:
            plus = plus * 10

        lb1["text"] = "追加：" + str(plus) + "                        "

    def num_clear(self): #ACが押された時の処理
        global number
        global plus

        number = 0
        plus = 0

        lb1["text"] = "追加：" + str(plus) + "                        "
        lb2["text"] = "結果：" + str(number) + "                        "

    def num_equal(self): #イコールが押された時の処理
        global number
        global plus

        if plus != 0 and number == 0:
            number = plus
            plus = 0

        lb1["text"] = "追加：" + str(plus) + "                        "
        lb2["text"] = "結果：" + str(number) + "                        "

    def num_plus(self): #+が押された時の処理
        global number
        global plus

        if number == 0:
            number = plus

        else:
            number += plus

        plus = 0

        lb1["text"] = "追加：" + str(plus) + "                        "
        lb2["text"] = "結果：" + str(number) + "                        "

    def num_minus(self): #-が押された時の処理
        global number
        global plus

        if number == 0:
            number = plus

        else:
            number -= plus

        plus = 0

        lb1["text"] = "追加：" + str(plus) + "                        "
        lb2["text"] = "結果：" + str(number) + "                        "

    def num_kake(self): #xが押された時の処理
        global number
        global plus

        if number == 0:
            number = plus

        elif number != 0 and plus != 0:
            number *= plus

        plus = 0

        lb1["text"] = "追加：" + str(plus) + "                        "
        lb2["text"] = "結果：" + str(number) + "                        "

    def num_waru(self): #÷が押された時の処理
        global number
        global plus

        if number == 0:
            number = plus

        elif number != 0 and plus != 0:
            number /= plus

        plus = 0

        lb1["text"] = "追加：" + str(plus) + "                        "
        lb2["text"] = "結果：" + str(number) + "                        "

root = tk.Tk()

num_calc = Num_calc()

root.title("ベルンの電卓")
root.geometry("800x600")
root.resizable(width = False, height = False)

lb1 = tk.Label(text = "追加：" + str(plus) + "                       ")
lb1.place(x = 400, y = 500)

lb2 = tk.Label(text = "結果：" + str(number))
lb2.place(x = 400, y = 530)

bt1 = tk.Button(width = 20, height = 5, text = "1", command = num_calc.num_calc_1)
bt1.place(x = 50, y = 100)

bt2 = tk.Button(width = 20, height = 5, text = "2", command = num_calc.num_calc_2)
bt2.place(x = 230, y = 100)

bt3 = tk.Button(width = 20, height = 5, text = "3", command = num_calc.num_calc_3)
bt3.place(x = 410, y = 100)

bt4 = tk.Button(width = 20, height = 5, text = "4", command = num_calc.num_calc_4)
bt4.place(x = 50, y = 200)

bt5 = tk.Button(width = 20, height = 5, text = "5", command = num_calc.num_calc_5)
bt5.place(x = 230, y = 200)

bt6 = tk.Button(width = 20, height = 5, text = "6", command = num_calc.num_calc_6)
bt6.place(x = 410, y = 200)

bt7 = tk.Button(width = 20, height = 5, text = "7", command = num_calc.num_calc_7)
bt7.place(x = 50, y = 300)

bt8 = tk.Button(width = 20, height = 5, text = "8", command = num_calc.num_calc_8)
bt8.place(x = 230, y = 300)

bt9 = tk.Button(width = 20, height = 5, text = "9", command = num_calc.num_calc_9)
bt9.place(x = 410, y = 300)

bt10 = tk.Button(width = 20, height = 5, text = "0", command = num_calc.num_calc_0)
bt10.place(x = 230, y = 400)

bt11 = tk.Button(width = 20, height = 5, text = "+", command = num_calc.num_plus)
bt11.place(x = 590, y = 100)

bt12 = tk.Button(width = 20, height = 5, text = "-", command = num_calc.num_minus)
bt12.place(x = 590, y = 200)

bt13 = tk.Button(width = 20, height = 5, text = "×", command = num_calc.num_kake)
bt13.place(x = 590, y = 300)

bt14 = tk.Button(width = 20, height = 5, text = "AC", command = num_calc.num_clear)
bt14.place(x = 50, y = 400)

bt15 = tk.Button(width = 20, height = 5, text = "÷", command = num_calc.num_waru)
bt15.place(x = 590, y = 400)

bt16 = tk.Button(width = 20, height = 5, text = "=", command = num_calc.num_equal)
bt16.place(x = 410, y = 400)

root.mainloop()