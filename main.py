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

# top panel
top_panel = Frame(app, bd=1, relief=FLAT) # bd = border
top_panel.pack(side=TOP) # place it on top

# title label
title_label = Label(top_panel, text="Facturation System", fg="azure4", font=("Dosis", 58), bg="burlywood", width=22)
title_label.grid(row=0, column=0)

# left panel
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# costs panel
costs_panel = Frame(left_panel, bd=1, relief=FLAT)
costs_panel.pack(side=BOTTOM)

# food panel
food_panel = LabelFrame(left_panel, text="Food", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
food_panel.pack(side=LEFT)

# drinks panel
drinks_panel = LabelFrame(left_panel, text="Drinks", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
drinks_panel.pack(side=LEFT)

# desserts panel
desserts_panel = LabelFrame(left_panel, text="Desserts", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4")
desserts_panel.pack(side=LEFT)

# right panel
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
calculator_panel.pack()

# receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
receipt_panel.pack()

# buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
buttons_panel.pack()

# food list
food_list = ["Chicken", "Lamb", "Salmon", "Bovine", "French Potatoes", "Sushi", "Casserole", "Carbonade"]

# drinks list
drinks_list = ["Water", "Coffee", "Tea", "Juice", "Soda", "Milk", "Beer", "Wine"]

# desserts list
desserts_list = ["Cake", "Ice Cream", "Pie", "Cookies", "Brownie", "Cupcake", "Donut", "Tiramisu"]


# add food list to checkbuttons
food_var = []
count = 0

for food in food_list:
    food_var.append("")
    food_var[count] = IntVar()
    food = Checkbutton(food_panel, text=food.title(),font=('Dosis', 19, 'bold',),onvalue=1,offvalue=0, variable=food_var[count])
    food.grid(row=count, column=0, sticky=W)
    count += 1

# add drinks list to checkbuttons
drinks_var = []
count = 0

for drink in drinks_list:
    drinks_var.append("")
    drinks_var[count] = IntVar()
    drink = Checkbutton(drinks_panel, text=drink.title(),font=('Dosis', 19, 'bold',),onvalue=1,offvalue=0, variable=drinks_var[count])
    drink.grid(row=count, column=0, sticky=W)
    count += 1

# add desserts list to checkbuttons
desserts_var = []
count = 0

for dessert in drinks_list:
    desserts_var.append("")
    desserts_var[count] = IntVar()
    dessert = Checkbutton(desserts_panel, text=dessert.title(),font=('Dosis', 19, 'bold',),onvalue=1,offvalue=0, variable=desserts_var[count])
    dessert.grid(row=count, column=0, sticky=W)
    count += 1

# avoid window to be closed
app.mainloop()
