from tkinter import *
import re
import random

"""
나도 코딩 퀴즈 #2에서 설명한 행맨 게임을 그대로 만들어 볼 예정
tkinter로 gui부분을 만들예정
"""


SCREEN_WIDTH     = 720;
SCREEN_HEIGHT    = 480;
DEFAULT_WORD_COLOR_GREY = "#ccc"
ANSWER_WORD_COLOR_BLACK = "#000"

screenSize      = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT);

window = Tk();
window.title("HangMan")
window.geometry(screenSize + "+250+100")
window.resizable(False, False)

canvas = Canvas(window, width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
canvas.place(x = 0, y = 10, width = 720, height = 350, anchor = "nw")

inputAlphabet = StringVar();
sliceQuestWord = list();

def CheckCharactersCount():
    if len(inputAlphabet.get()) > 1:    # 현재 입력받은 수가 1이상이 되면
        inputAlphabet.set(inputAlphabet.get()[1]);    # 새로 입력한 알파벳으로 현재 inputbox변경

def CheckAlphabet():
    condition = re.compile('[a-zA-Z]')      #알파벳만을 입력받기 위한 정규식
    isAlphabet = condition.match(inputAlphabet.get()) #위에서 만든 정규식과 match하는 검사한 결과를 return 해준다
    if not isAlphabet:
        inputAlphabet.set("");

def ConverToUppercase():
    inputAlphabet.set(inputAlphabet.get().upper())  # 입력받은 알파벳 대문자로 변환

def InputboxRestrictions(event):

    # 엔터처리
    if event.keysym == "Return":
        print("엔터")
        AttemptToVerifyWords();
        return;
 
    CheckCharactersCount();
    CheckAlphabet();
    ConverToUppercase();

def AttemptToVerifyWords():



    canvas.itemconfigure(10, fill = "#000");

def InitData():

    InitHangMan();
    InitQuestWord();
    InitInputBox();

def InitHangMan():
    # 행맨 그림 그려주는 코드
    canvas.create_line(205, 210, 260, 260, width = 5, fill = DEFAULT_WORD_COLOR_GREY)                                #오른발
    canvas.create_line(205, 210, 150, 260, width = 5, fill = DEFAULT_WORD_COLOR_GREY)                                #왼발
    canvas.create_line(205, 160, 260, 140, width = 5, fill = DEFAULT_WORD_COLOR_GREY)                                #오른손
    canvas.create_line(205, 160, 150, 140, width = 5, fill = DEFAULT_WORD_COLOR_GREY)                                #왼손
    canvas.create_line(205, 120, 205, 210, width = 5, fill = DEFAULT_WORD_COLOR_GREY)                                #몸
    canvas.create_oval(175, 60, 235, 120, width = 5, outline = DEFAULT_WORD_COLOR_GREY, tags = "circle")             #머리
    canvas.create_line(200, 10, 200, 60, width = 5, fill = DEFAULT_WORD_COLOR_GREY)                                  #두번째 꺽임선
    canvas.create_line(75, 10, 200, 10, width = 5, fill = DEFAULT_WORD_COLOR_GREY)                                   #첫 꺽임선
    canvas.create_line(75, SCREEN_HEIGHT - 140, 75, 10, width = 5, fill = DEFAULT_WORD_COLOR_GREY)                   #기둥
    canvas.create_line(10, SCREEN_HEIGHT - 140, 150, SCREEN_HEIGHT - 140, width = 5, fill = DEFAULT_WORD_COLOR_GREY) #밑 바닥

def InitQuestWord():
    # 단어 입력은 최대 9글자로 받거나 9글자 이하 단어만 문제로 나오게 함
    savedWordList = ["BANANA", "ORANGE", "APPLE", "MELON", "MANGO", "CHOCOLATE", "STARBUCKS", "LANGUAGE", "NAPKIN"];
    randQuestion = savedWordList[random.randrange(0, len(savedWordList))];

    # 랜덤하게 고른 단어를 알파벳 한개씩 쪼개서 list에 저장
    for alphabet in range(len(randQuestion)):
        sliceQuestWord.append([randQuestion[alphabet], DEFAULT_WORD_COLOR_GREY])

    # 밑 줄 그리기 + 정답을 맞추면 단어도 그리고 밑줄도 같이 검은색으로 변경
    for idx, value in enumerate(sliceQuestWord):
        # if value[1] == ANSWER_WORD_COLOR_BLACK:
        canvas.create_text(295 + (idx * 50), 180, font=('Calibri', 30, 'bold'), anchor='center', text=value[0], fill = value[1])
        canvas.create_line(275 + (idx * 50), 210, 315 + (idx * 50), 210, width = 5, fill = value[1]);

def InitInputBox():
    inputBox = Entry(window, font=("Calibri 30 bold"), textvariable=inputAlphabet)
    inputBox.place(x = 400, y = 400, width = 35, height = 40, anchor = "center")
    inputBox.bind("<Return>",  lambda x: x)
    inputBox.bind("<KeyRelease>", InputboxRestrictions)
    inputBox.focus()

InitData();

window.mainloop()

# canvas.coords(xxx, 0,0, 100, 200);  #위에서 그린 선 위치와 크기 수정
# canvas.itemconfigure(xxx, fill = "#000");   #위에서 그린 선의 옵션 수정

# 색 칠해주는 테스트 코드
# for item in range(len(canvas.find_all()), 0, -1):

#     if canvas.find_withtag("circle")[0] == item:
#         canvas.itemconfigure(item, outline = "#000");
#     else:
#         canvas.itemconfigure(item, fill = "#000");

