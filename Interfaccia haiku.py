import tkinter as tk

window = tk.Tk()
window.geometry("540x400")
window.title("GENERATORE CASUALE DI HAIKU")
window.resizable(False, False)
window.configure(background="Light blue")



testo = tk.Label(text="Questo è un generatore randomico di haiku. Per visualizzare un haiku clicca su GENERA", fg="red", font=("Times", 12))
testo.grid()
first_button = tk.Button(text="GENERA", fg="blue", font=("Times",25))
first_button.grid(padx=100, pady=0)




if __name__ == "__main__":
    window.mainloop()
