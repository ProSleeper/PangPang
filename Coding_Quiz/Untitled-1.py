from tkinter import *
import re
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
inputBox        = None;

def CreateInputBox():
    global inputBox;
    vcmd = (window.register(Validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    inputBox = Entry(window, font=("Calibri 30 bold"), validate = 'key', validatecommand = vcmd)
    inputBox.place(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, width = 35, height = 40, anchor = "center")
    inputBox.focus()


def Validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if CheckCharactersCount(value_if_allowed) and CheckAlphabet(text):
        return True;
    else:
        return False;
        
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

CreateInputBox()

window.mainloop()