import pymysql
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분
def insertData() :
    con, cur = None, None
    data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
    sql=""

    con = pymysql.connect(host='127.0.0.1', user='root', password='k404', database='HTitemDB', charset='utf8')
    cur = con.cursor()

    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get(); data5 = edt5.get(); data6 = edt6.get()
    try :
        sql = "INSERT INTO itemsTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + "'," +data5 + "'," + data6 + ")"
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()

def selectData() :
    strData1, strData2, strData3, strData4, strData5, strData6 = [], [], [], [], [], []
    con = pymysql.connect(host='127.0.0.1', user='root', password='k404', database='HTitemDB', charset='utf8')
    cur = con.cursor()
    cur.execute("SELECT * FROM itemsTable")
    strData1.append("제품명"); strData2.append("회사명")
    strData3.append("최종가격"); strData4.append("할인율")
    strData5.append("원가격"); strData6.append("제품이미지")
    strData1.append("-----------"); strData2.append("-----------")
    strData3.append("-----------"); strData4.append("-----------")
    strData5.append("-----------"); strData6.append("-----------")
    while (True) :
        row = cur.fetchone()
        if row== None :
            break;
        strData1.append(row[0]); strData2.append(row[1])
        strData3.append(row[2]); strData4.append(row[3])
        strData5.append(row[4]); strData6.append(row[5])

    listData1.delete(0, listData1.size() - 1); listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1); listData4.delete(0, listData4.size() - 1)
    listData5.delete(0, listData5.size() - 1); listData6.delete(0, listData6.size() - 1)
    for item1, item2, item3, item4 , item5, item6 in zip(strData1, strData2, strData3, strData4, strData5, strData6):
        listData1.insert(END, item1); listData2.insert(END, item2)
        listData3.insert(END, item3); listData4.insert(END, item4)
        listData5.insert(END, item5); listData6.insert(END, item6)
    con.close()    

## 메인 코드 부분 ## 
window = Tk()
window.geometry("600x300")
window.title("GUI 데이터 입력")

edtFrame = Frame(window);
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side = BOTTOM,fill=BOTH, expand=1)

edt1= Entry(edtFrame, width = 10); edt1.pack(side = LEFT, padx = 10, pady = 10)
edt2= Entry(edtFrame, width = 10); edt2.pack(side = LEFT, padx = 10, pady = 10)
edt3= Entry(edtFrame, width = 10); edt3.pack(side = LEFT, padx = 10, pady = 10)
edt4= Entry(edtFrame, width = 10); edt4.pack(side = LEFT, padx = 10, pady = 10)
edt5= Entry(edtFrame, width = 10); edt3.pack(side = LEFT, padx = 10, pady = 10)
edt6= Entry(edtFrame, width = 10); edt4.pack(side = LEFT, padx = 10, pady = 10)

btnInsert = Button(edtFrame, text = "입력", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)
btnSelect = Button(edtFrame, text = "조회", command = selectData)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg = 'yellow')
listData1.pack(side = LEFT, fill = BOTH, expand = 1)
listData2 = Listbox(listFrame, bg = 'yellow')
listData2.pack(side = LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg = 'yellow')
listData3.pack(side = LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg = 'yellow')
listData4.pack(side = LEFT, fill = BOTH, expand = 1)
listData5 = Listbox(listFrame, bg = 'yellow')
listData5.pack(side = LEFT, fill = BOTH, expand = 1)
listData6 = Listbox(listFrame, bg = 'yellow')
listData6.pack(side = LEFT, fill = BOTH, expand = 1)


window.mainloop()
