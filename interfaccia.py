from tkinter import *
from tkinter import filedialog

base = Tk()

base.geometry('150x150')

def file_opener():
    input = filedialog.askopenfile(initialdir="/")


    data=list(input)
    datal = [x[:-1] for x in data]
    our_list=[]
    print(datal)
    for i in list(range(0,len(data1))) :
        print(i)
        our_list.appened(datal[i])
        print(our_list)

x = Button(base, text ='Seleziona un file .txt/.csv', command = lambda:file_opener())
x.pack()
mainloop()



