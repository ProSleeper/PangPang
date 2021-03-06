import random

listHeight = list();

widthCount = 0;
for i in range(5):
    listWidth = list();
    for j in range(5):
        square = random.randrange(0,2);
        if square == 1:
            content = "□"
        else:
            content = "■"
            widthCount += 1;
        listWidth.append(content);
        
        # print("{0}".format(content), end = " ");
    listHeight.append(listWidth);
    # print("");


listHeightAnswer = list();
listWidthAnswer = list();

for i in range(5):
    listHeightAnswerWidth = list();
    listWidthAnswerWidth = list();
    count = 0;
    countWidth = 0;
    for j in range(5):
        if listHeight[i][j] == "■":
            count += 1;
        elif count > 0 and listHeight[i][j] == "□":
            listHeightAnswerWidth.append(count);
            count = 0;

        if j > 3 and count > 0:
            listHeightAnswerWidth.append(count);

        if listHeight[j][i] == "■":
            countWidth += 1;
        elif countWidth > 0 and listHeight[j][i] == "□":
            listWidthAnswerWidth.append(countWidth);
            countWidth = 0;
        if j > 3 and countWidth > 0:
            listWidthAnswerWidth.append(countWidth);
            
    listHeightAnswer.append(listHeightAnswerWidth)
    listWidthAnswer.append(listWidthAnswerWidth)


print(end = "     ");
for item in listWidthAnswer:
    for j in item:
        print(j, end = "")
    print(end = "    ");
    

print();

for idx ,i in enumerate(listHeightAnswer):
    print(i, end = " ")
    print(listHeight[idx])



            