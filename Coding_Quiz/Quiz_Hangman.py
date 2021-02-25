from tkinter import *

"""
나도 코딩 퀴즈 #2에서 설명한 행맨 게임을 그대로 만들어 볼 예정
tkinter로 gui부분을 만들예정
"""




window = Tk();
window.title("HangMan")
window.geometry("400x300+400+200")
window.resizable(False, False)

canvas = Canvas(window, width = 500, height = 500)
canvas.pack()
canvas.create_line(0, 0, 100, 100)
canvas.create_oval(100, 100, 120, 120, width = 10)
window.mainloop()

