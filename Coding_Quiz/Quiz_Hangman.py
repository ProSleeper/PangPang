from tkinter import *

"""
나도 코딩 퀴즈 #2에서 설명한 행맨 게임을 그대로 만들어 볼 예정
tkinter로 gui부분을 만들예정
"""

SCREEN_WIDTH     = 720;
SCREEN_HEIGHT    = 480;
screenSize      = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT);

window = Tk();
window.title("HangMan")
window.geometry(screenSize + "+250+100")
window.resizable(False, False)

canvas = Canvas(window, width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
canvas.pack()
canvas.create_line(10, SCREEN_HEIGHT - 50, 250, SCREEN_HEIGHT - 50, width = 5, fill = "#ccc")
canvas.create_line(125, SCREEN_HEIGHT - 50, 125, 100, width = 5, fill = "#ccc")
yyy = canvas.create_line(125, 100, 250, 100, width = 5, fill = "#ccc")
xxx = canvas.create_line(250, 100, 250, 150, width = 5, fill = "#ccc")

# canvas.coords(xxx, 0,0, 100, 200);  #위에서 그린 선 위치와 크기 수정
# canvas.itemconfigure(xxx, fill = "#000");   #위에서 그린 선의 옵션 수정



canvas.create_oval(100, 100, 150, 150, width = 5, outline = "#ccc")
window.mainloop()

