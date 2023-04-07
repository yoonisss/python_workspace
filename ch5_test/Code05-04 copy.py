from tkinter import *
window = Tk()
#gif, png 파일 이미지 확인해보기.
photo = PhotoImage(file = "GIF/cat.gif")
photo2 = PhotoImage(file = "GIF/cat2.gif")

label1 = Label(window, image = photo)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT);
label2.pack(side=LEFT);

window.mainloop()
