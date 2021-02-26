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

# def getTextInput():
#     result=textExample.get("1.0","end")
#     print(result)

# textExample=Text(window, font=("Calibri 20"))

# textExample.place(x = 400, y = 400, width = 60, height = 40, anchor = "center", validate = "key")


# btnRead=Button(window, text="입력", command=getTextInput)
# btnRead.place(x = 550, y = 400, width = 100, height = 40, anchor = "center", bordermode="inside")

def calc(event):
    label.config(text="결과="+str(eval(entry.get())))

entry=Entry(window, validate = "key")
entry.bind("<Return>", calc)
entry.place(x = 400, y = 400, width = 60, height = 40, anchor = "center")

label=Label(window)
label.place(x = 550, y = 400, width = 100, height = 40, anchor = "center", bordermode="inside")


canvas = Canvas(window, width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
canvas.place(x = 0, y = 10, width = 720, height = 350, anchor = "nw")




# canvas.coords(xxx, 0,0, 100, 200);  #위에서 그린 선 위치와 크기 수정
# canvas.itemconfigure(xxx, fill = "#000");   #위에서 그린 선의 옵션 수정

# canvas.create_line(0, 0, 720, 0, width = 5, fill = "#000")    #test
# canvas.create_line(0, 340, 720, 340, width = 5, fill = "#000")    #test

canvas.create_line(205, 210, 260, 260, width = 5, fill = "#ccc")    #오른발
canvas.create_line(205, 210, 150, 260, width = 5, fill = "#ccc")    #왼발
canvas.create_line(205, 160, 260, 140, width = 5, fill = "#ccc")    #오른손
canvas.create_line(205, 160, 150, 140, width = 5, fill = "#ccc")    #왼손
canvas.create_line(205, 120, 205, 210, width = 5, fill = "#ccc")    #몸
canvas.create_oval(175, 60, 235, 120, width = 5, outline = "#ccc", tags = "circle") #머리

canvas.create_line(200, 10, 200, 60, width = 5, fill = "#ccc")                                #두번째 꺽임선
canvas.create_line(75, 10, 200, 10, width = 5, fill = "#ccc")                                 #첫 꺽임선
canvas.create_line(75, SCREEN_HEIGHT - 140, 75, 10, width = 5, fill = "#ccc")                   #기둥
canvas.create_line(10, SCREEN_HEIGHT - 140, 150, SCREEN_HEIGHT - 140, width = 5, fill = "#ccc")   #밑 바닥

# 색 칠해주는 테스트 코드
# for item in range(len(canvas.find_all()), 0, -1):

#     if canvas.find_withtag("circle")[0] == item:
#         canvas.itemconfigure(item, outline = "#000");
#     else:
#         canvas.itemconfigure(item, fill = "#000");


# inputWord = input("단어를 입력해주세요")

inputWord = "BANANA";
inputWordlist = list();

whatColor = "#ccc";

for item in range(len(inputWord)):
    inputWordlist.append([inputWord[item], whatColor])

inputText = "A"

for idx, value in enumerate(inputWordlist):

    if inputText == value[0]:
        value[1] = "#000";

# inputWordlist = ["B","O","Y","F","R","I","E","N","D",]

colorBlack  = "#000"
colorGrey   = "#ccc"

for idx, value in enumerate(inputWordlist):
    if value[1] == "#000":
        canvas.create_text(295 + (idx * 50), 180, font=('freemono', 30, 'bold'), anchor='center', text=value[0], fill = value[1])
    canvas.create_line(275 + (idx * 50), 210, 315 + (idx * 50), 210, width = 5, fill = value[1]) 




#boyfriend 

window.mainloop()

