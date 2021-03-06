class Word():
    def __init__(self, newWord, view1, view2, answer):
        self.newWord    = newWord;
        self.view1      = view1;
        self.view2      = view2;
        self.answer     = answer;
        
    def ShowQuestion(self):
        print("\"{0}\"의 뜻은?".format(self.newWord))
        print("1. {0}".format(self.view1))
        print("2. {0}".format(self.view2))
        self.tempFunc();
    
    def Check_Answer(self, playerAnswer):

        if self.answer == playerAnswer:
            print("정답입니다.")
        else:
            print("틀렸습니다.")

    def tempFunc(self):
        print("하하")
    




word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1);
word.ShowQuestion();
word.Check_Answer(int(input("=>")));