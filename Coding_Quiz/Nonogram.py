import random


# 심심해서 해본 아주 막가파식 노노그램 알고리즘 및 출력

content = "";
listHeight = list();

listHeightNumber = list();
listWidthNumber = list();

widthCount = 0;
for i in range(5):
    listWidth = list();
    listWidthNumber.append(0);
    for j in range(5):
        square = random.randrange(0,2);
        if square == 1:
            content = "□"
        else:
            content = "■"
            widthCount += 1;
        listWidth.append(content);
        
     #   print("{0}".format(content), end = " ");
    listHeight.append(listWidth);
    listHeightNumber.append(widthCount);
    widthCount = 0;
    #print("");
    

for item in listHeight:
    
    for idx, wtem in enumerate(item):
        if wtem == "■" :
            listWidthNumber[idx] += 1;
            

listHeightNumber.reverse()

print(end = "    ")
for item in listWidthNumber:
    print(item,  end = "    ")
print()

for item in listHeight:
    print(listHeightNumber.pop(), end = " ");
    print(item);