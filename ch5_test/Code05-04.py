from tkinter import *
window = Tk()
#gif, png 파일 이미지 확인해보기.
photo = PhotoImage(file = "GIF/dog13.gif")
label1 = Label(window, image = photo)

label1.pack();

window.mainloop()
