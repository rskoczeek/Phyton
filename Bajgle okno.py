import tkinter
from Bajgle import *

okno=Tk()
oknoStartowe = tkinter.Label(text='Zagrajmy w BAJGLE!')
zacznijGre = tkinter.Button(text = "START", command = okno.Bajgle.main())
oknoStartowe.pack()
zacznijGre.pack()
okno.mainloop()
