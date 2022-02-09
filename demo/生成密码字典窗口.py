from tkinter import *
import itertools as its


class MyGui:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.get_min_value = IntVar()
        self.get_max_value = IntVar()
        self.get_words_value = StringVar()

    def set_init_window(self):
        self.init_window_name.title("生成字典")
        self.init_window_name.geometry('+500+200')
        labelframe = LabelFrame(width=400, height=200, text="设置")  # 框架，以下对象都是对于labelframe中添加的
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        self.min_text = Label(labelframe, text="密码最小位数：").grid(column=0, row=0)
        self.min_input = Entry(labelframe, width=15, textvariable=self.get_min_value).grid(column=1, row=0)
        self.max_text = Label(labelframe, text="密码最大位数：").grid(column=2, row=0)
        self.max_input = Entry(labelframe, width=15, textvariable=self.get_max_value).grid(column=3, row=0)

        self.words_text = Label(labelframe, text="要随机的字符串：").grid(column=0, row=1)
        self.words_input = Entry(labelframe, width=15, textvariable=self.get_words_value).grid(column=1, row=1)

        self.pojie = Button(labelframe, text="开始生成", command=self.create_pwd).grid(column=2, row=1)

    def create_pwd(self):
        # words = "1234568790"
        # words = "1234568790abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-.,;[]:><?{  }'`~/\|"""
        words = self.get_words_value.get()
        num = self.get_min_value.get()
        max = self.get_max_value.get()
        print("开始生成")
        while num <= max:
            r = its.product(words, repeat=num)
            dic = open("pass.txt", "a")
            for i in r:
                dic.write("".join(i))
                dic.write("".join("\n"))
            num += 1
        print("生成成功")


def gui_start():
    init_window = Tk()
    ui = MyGui(init_window)
    print(ui)
    ui.set_init_window()

    init_window.mainloop()


gui_start()
