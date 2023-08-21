from tkinter import *

# init tkinterrr
app = Tk()

# screen size
app.geometry("1020x630+0+0") #1020 width - 630height - 0x - 0y

# avoid max screen
app.resizable(False, False) # X and Y position can't be modified

# window tittle
app.title("Facturation System ®")

# background color screen
app.config(bg='Gray')

# avoid window to be closed
app.mainloop()
