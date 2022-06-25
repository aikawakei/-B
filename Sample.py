import tkinter, tkinter.messagebox
tki = tkinter.Tk()
tki.geometry('300x200')
tki.title('ラジオボタン')

rdo_txt = ['チェック1','チェック2','チェック3']
rdo_var = tkinter.IntVar()

for i in range(len(rdo_txt)):
    rdo = tkinter.Radiobutton(tki, value=i, variable=rdo_var, text=rdo_txt[i])
    rdo.place(x=50, y=30 + (i * 24))

    def btn_click():
        num = rdo_var.get()
        tkinter.messagebox.showinfo('チェックされた項目', rdo_txt[num])

btn = tkinter.Button(tki, text='ラジオボタン取得', command=btn_click)
btn.place(x=100, y=170) 
