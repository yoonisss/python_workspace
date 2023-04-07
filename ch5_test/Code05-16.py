from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    print("사진의 크기 가로 세로 크기 : %d x %d" %(photo.width(), photo.height()))
    #print("사진의 0,0 의 좌표의 RGB값을 튜플로 보자. %s :" % photo.get(0,0))
    print(photo.get(0,0))
    a = (photo.get(0,0))
    
    # for i in range(0,photo.width()) :
    #     imgList = []
    #     for k in range(0,photo.height()) :
    #         tmpList=[]
    #         a = photo.get(i.k)
    #         tmpList.append(a)
    #     imgList.append(tmpList)
    
    
    # width = photo.width()
    # height = photo.height()

    # for i in range(height) :
    #     for k in range(width) :
    #         r, g, b = photo.get(k, i)
    #         grey = int((r+g+b)/3)
    #         photo.put("#%02x%02x%02x" % (grey, grey, grey), (k, i))

    # pLabel.configure(image = photo)
    # pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()

## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()
