# cook your dish here
noOfTestCases=int(input())
outputLst=[]
for testCaseNo in range(noOfTestCases):
    inp_secondLine=input().split(' ')
    inp_thirdLine=input().split(' ')
    
    quesDays=inp_secondLine[0]
    dailyLimit=int(inp_secondLine[1])
    
    remainderQues=0
    dayCount=0
    withinFlg=True
    
    for dailyQues in inp_thirdLine:
        dayCount+=1
        quesForDay=int(dailyQues)+remainderQues
        if(dailyLimit<=quesForDay):
            remainderQues=quesForDay-dailyLimit
            continue
        elif(dailyLimit>quesForDay):
            remainderQues=0
            outputLst.append(dayCount)
            withinFlg=False
            break
            
    if(withinFlg):
        outputLst.append(dayCount+remainderQues//dailyLimit+1)
            
for i in outputLst:
    print(i)