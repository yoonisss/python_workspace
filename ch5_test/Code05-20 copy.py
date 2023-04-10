inFp = None 
inList, inStr = [], ""

inFp = open("test.txt", "r", encoding="utf-8")
# inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")
lineNum = 1
inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")
    print("%d : %s" %(lineNum, inStr), end="")
    lineNum += 1

inFp.close()
