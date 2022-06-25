import tkinter
			tki = tkinter.Tk()
			tki.geometry('300x200')
			tki.title('ラジオボタン')
			
			rdo1 = tkinter.Radiobutton(tki, text='サンプル問題1')
			rdo1.place(x=70, y=40)
			
			rdo2 = tkinter.Radiobutton(tki, text='サンプル問題2')
			rdo2.place(x=70, y=70)
			
			rdo3 = tkinter.Radiobutton(tki, text='サンプル問題3')
			rdo3.place(x=70, y=100)
