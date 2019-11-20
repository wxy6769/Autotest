from tkinter import *
from tkinter import StringVar
import time


class Progress(object):

    def __init__(self):

        model = "AN-310-SW-R-8"

        self.root = Tk()
        self.root.geometry('245x30')
        self.root.title(model)

        self.var = StringVar()
        self.var.set("GO")
        self.button = Button(
            self.root,
            textvariable=self.var,
            command=self.start,
            width=5)
        self.button.grid(row=0, column=0, padx=5)

        # 建立一個背景色為白色的矩形
        self.canvas = Canvas(self.root, width=170, height=26, bg="white")

        # 建立矩形的外框(left_margin, top_margin, width, height, frame_width, color)
        self.out_line = self.canvas.create_rectangle(
            2, 2, 170, 27,
            width=1,
            outline="red")
        self.canvas.grid(row=0, column=1, ipadx=5)

        self.root.mainloop()

    def start(self):
        # 設定按鈕只允許點擊一次
        self.button.config(state="disable")
        fill_line = self.canvas.create_rectangle(
            2, 2, 0, 27,
            width=0, fill="blue")

        # 進度條最大值
        x = 1000
        # 矩形填滿所需要的次數
        n = 180 / x
        # 顯示值
        k = 100 / x

        for i in range(x):
            n = n + 180 / x
            k = k + 100 / x
            # 以矩形的長度作為更新基數
            self.canvas.coords(fill_line, (0, 0, n, 30))
            if k >= 100:
                self.var.set("100%")
            else:
                self.var.set(str(round(k, 1)) + "%")
            self.root.update()
            time.sleep(0.01)


if __name__ == '__main__':
    Progress()
