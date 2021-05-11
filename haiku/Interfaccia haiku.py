from tkinter import *
from tkinter import messagebox

top = Tk()

C = Canvas(top, bg="blue", height=320, width=330)
filename = PhotoImage(file = "C:\\Users\\Todino Family\\Desktop\\haiku\\cornice.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
def toggle_color(last=[0]):       
    colors = ['red', 'blue', 'green', 'purple', 'yellow']
    color = colors[last[0]]
    last[0] = (last[0] + 1) % 5    
    first_button.config(fg=color)         
first_button = Button(text="GENERA", command=toggle_color, font=("Times",30))
first_button.place(x=70, y=50)


top.mainloop()
