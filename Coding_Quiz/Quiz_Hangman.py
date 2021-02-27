from tkinter import *
import re
import random

"""
나도 코딩 퀴즈 #2에서 설명한 행맨 게임을 그대로 만들어 볼 예정
tkinter로 gui부분을 만들예정
"""


SCREEN_WIDTH            = 720;
SCREEN_HEIGHT           = 480;
HANGMAN_ATTEMPT_COUNT   = 10;
DEFAULT_WORD_COLOR_GREY = "#ccc"
ANSWER_WORD_COLOR_BLACK = "#000"

SCREEN_SIZE             = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT);

window = Tk();
window.title("HangMan")
window.geometry(SCREEN_SIZE + "+250+100")
window.resizable(False, False)

canvas = Canvas(window, width = SCREEN_WIDTH, height = 350)
canvas.place(x = 0, y = 10, width = 720, height = 350, anchor = "nw")

sliceQuestWord  = list();
hangmanLine     = list();
inputBox        = None;
questWordCount  = 0;
hangmanLife     = HANGMAN_ATTEMPT_COUNT

def InitData():
    
    DrawHangMan();
    CreateInputBox();
    # 단어 입력은 최대 9글자로 받거나 9글자 이하 단어만 문제로 나오게 함
    
    savedWordList = ["BANANA", "ORANGE", "APPLE", "MELON", "MANGO", "CHOCOLATE", "STARBUCKS", "LANGUAGE", "NAPKIN"];
    # savedWordList = ["BANANA"];
    randQuestion = savedWordList[random.randrange(0, len(savedWordList))];

    # 랜덤하게 고른 단어를 알파벳 한개씩 쪼개서 list에 저장
    for alphabet in range(len(randQuestion)):
        sliceQuestWord.append([randQuestion[alphabet]])


    # 밑 줄 그리기 + 정답을 맞추면 단어도 그리고 밑줄도 같이 검은색으로 변경
    for idx, value in enumerate(sliceQuestWord):
        sliceQuestWord[idx].append(canvas.create_text(295 + (idx * 50), 180, font=('Calibri', 30, 'bold'), anchor='center', text=value[0], fill = ""))
        sliceQuestWord[idx].append(canvas.create_line(275 + (idx * 50), 210, 315 + (idx * 50), 210, width = 5, fill = DEFAULT_WORD_COLOR_GREY));
        sliceQuestWord[idx].append(False);
    global questWordCount
    questWordCount = len(sliceQuestWord);


def CheckCharactersCount(value_if_allowed):
    if len(value_if_allowed) > 1:
        return False;
    else:
        return True;

def CheckAlphabet(text):
    condition = re.compile('[a-zA-Z]')      #알파벳만을 입력받기 위한 정규식
    isAlphabet = condition.match(text) #위에서 만든 정규식과 match하는 검사한 결과를 return 해준다
    
    if isAlphabet: # or value_if_allowed == "":
        return True
    else:
        return False

def PressReturn(event):

    global hangmanLife;
    global questWordCount;
    
    upperInputText = inputBox.get().upper();
    
    if upperInputText == "":
        return;

    inputBox.delete(0, END)

    isWord, answerCount = AttemptToVerifyWords(upperInputText)

    if not isWord:
        canvas.itemconfigure(hangmanLine[hangmanLife - 1], fill = "#000");
        hangmanLife -= 1;
        if hangmanLife == 0:
            EndGame("Game Over!")
            return;

    
    questWordCount -= answerCount;
    if questWordCount == 0:
        EndGame("Game Success!")
        return;

def EndGame(endText):
    canvas.delete("all")
    inputBox.destroy()

    label=Label(window, text=endText, font=("Calibri 30 bold"), width=20, height=1, relief="solid")
    label.pack()

    button = Button(window, text = "START", overrelief="solid", width=15, command= lambda: ResetGame(button, label), repeatdelay=1000, repeatinterval=100)
    button.pack(expand = True, fill = "both", padx = "250", pady = "160")


def ResetGame(button, label):
    global hangmanLife
    button.destroy();
    label.destroy();

    sliceQuestWord.clear()
    hangmanLine.clear()

    questWordCount  = 0;
    hangmanLife     = HANGMAN_ATTEMPT_COUNT;

    InitData();

def AttemptToVerifyWords(upperInputText):
    answerCount = 0;
    result = False;
    for alphabet in sliceQuestWord:
        if alphabet[0] == upperInputText and alphabet[3] == False:
            answerCount += 1
            result = True;
            canvas.itemconfigure(alphabet[1], fill = ANSWER_WORD_COLOR_BLACK);
            canvas.itemconfigure(alphabet[2], fill = ANSWER_WORD_COLOR_BLACK);
            alphabet[3] = True;

    return result, answerCount;

def DrawHangMan():

    # 행맨 그림 그려주는 코드
    hangmanLine.append(canvas.create_line(205, 210, 260, 260, width = 5, fill = DEFAULT_WORD_COLOR_GREY))                                #오른발
    hangmanLine.append(canvas.create_line(205, 210, 150, 260, width = 5, fill = DEFAULT_WORD_COLOR_GREY))                                #왼발
    hangmanLine.append(canvas.create_line(205, 160, 260, 140, width = 5, fill = DEFAULT_WORD_COLOR_GREY))                                #오른손
    hangmanLine.append(canvas.create_line(205, 160, 150, 140, width = 5, fill = DEFAULT_WORD_COLOR_GREY))                                #왼손
    hangmanLine.append(canvas.create_line(205, 120, 205, 210, width = 5, fill = DEFAULT_WORD_COLOR_GREY))                                #몸
    hangmanLine.append(canvas.create_oval(175, 60, 235, 120, width = 5, outline = DEFAULT_WORD_COLOR_GREY, tags = "circle"))             #머리
    hangmanLine.append(canvas.create_line(200, 10, 200, 60, width = 5, fill = DEFAULT_WORD_COLOR_GREY))                                  #두번째 꺽임선
    hangmanLine.append(canvas.create_line(75, 10, 200, 10, width = 5, fill = DEFAULT_WORD_COLOR_GREY))                                   #첫 꺽임선
    hangmanLine.append(canvas.create_line(75, SCREEN_HEIGHT - 140, 75, 10, width = 5, fill = DEFAULT_WORD_COLOR_GREY))                   #기둥
    hangmanLine.append(canvas.create_line(10, SCREEN_HEIGHT - 140, 150, SCREEN_HEIGHT - 140, width = 5, fill = DEFAULT_WORD_COLOR_GREY)) #밑 바닥

def CreateInputBox():
    global inputBox;
    vcmd = (window.register(Validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    inputBox = Entry(window, font=("Calibri 30 bold"), validate = 'key', validatecommand = vcmd)
    inputBox.place(x = 400, y = 400, width = 35, height = 40, anchor = "center")
    inputBox.bind("<Return>",  PressReturn)
    inputBox.focus()


def Validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if CheckCharactersCount(value_if_allowed) and CheckAlphabet(text):
        return True;
    else:
        return False;

InitData();
window.mainloop()

#대문자로 만드는 건 일단 중지
# def ConverToUppercase():
#     inputAlphabet.set(inputAlphabet.get().upper())  # 입력받은 알파벳 대문자로 변환

# canvas.coords(xxx, 0,0, 100, 200);  #위에서 그린 선 위치와 크기 수정
# canvas.itemconfigure(xxx, fill = "#000");   #위에서 그린 선의 옵션 수정

# 색 칠해주는 테스트 코드
# for item in range(len(canvas.find_all()), 0, -1):

#     if canvas.find_withtag("circle")[0] == item:
#         canvas.itemconfigure(item, outline = "#000");
#     else:
#         canvas.itemconfigure(item, fill = "#000");

