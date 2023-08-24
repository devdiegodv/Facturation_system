from tkinter import *

# init tkinterrr
app = Tk()

# screen size
app.geometry("1250x630+0+0") #1020 width - 630height - 0x - 0y

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
title_label = Label(top_panel, text="Facturation System", fg="white", font=("Dosis", 58), bg="green", width=22)
title_label.grid(row=0, column=0)

# left panel
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# costs panel
costs_panel = Frame(left_panel, bd=1, relief=FLAT, bg="azure4", padx=50)
costs_panel.pack(side=BOTTOM)

# food panel
food_panel = LabelFrame(left_panel,
                        text="Food",
                        font=("Dosis", 19, "bold"),
                        bd=1,
                        relief=FLAT,
                        fg="goldenrod3")
food_panel.pack(side=LEFT)

# drinks panel
drinks_panel = LabelFrame(left_panel,
                          text="Drinks",
                          font=("Dosis", 19, "bold"),
                          bd=1,
                          relief=FLAT,
                          fg="goldenrod3")

drinks_panel.pack(side=LEFT)

# desserts panel
desserts_panel = LabelFrame(left_panel,
                            text="Desserts",
                            font=("Dosis", 19, "bold"),
                            bd=1,
                            relief=FLAT,
                            fg="goldenrod3")

desserts_panel.pack(side=LEFT)

# right panel
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg="gray")
calculator_panel.pack()

# receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg="gray")
receipt_panel.pack()

# buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg="gray")
buttons_panel.pack()

# food list
food_list = ["Chicken", "Lamb", "Salmon", "Bovine", "French Potatoes", "Sushi", "Casserole", "Carbonade"]

# drinks list
drinks_list = ["Sprite", "Coffee", "Tea", "Juice", "Soda", "Milk", "Beer", "Wine"]

# desserts list
desserts_list = ["Cake", "Ice Cream", "Pie", "Cookies", "Brownie", "Cupcake", "Donut", "Tiramisu"]


# add food list to checkbuttons
food_var = []
food_box = []
food_text = []
count = 0

for food in food_list:
    # create checkbutton
    food_var.append("")
    food_var[count] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       font=('Dosis', 19, 'bold',),
                       onvalue=1,
                       offvalue=0,
                       variable=food_var[count])
    food.grid(row=count,
              column=0,
              sticky=W)

    # create entry box
    food_box.append("")
    food_text.append("")
    food_text[count] = StringVar()
    food_text[count].set("0")
    food_box[count] = Entry(food_panel,
                            font=("Dosis", 18, "bold"),
                            bd=1,
                            width=6,
                            state=DISABLED,
                            textvariable=food_text[count])
    food_box[count].grid(row=count,
                         column=1)
    count += 1

# add drinks list to checkbuttons
drinks_var = []
drinks_box = []
drinks_text = []
count = 0

for drink in drinks_list:
    # create checkbutton
    drinks_var.append("")
    drinks_var[count] = IntVar()
    drink = Checkbutton(drinks_panel,
                        text=drink.title(),
                        font=('Dosis', 19, 'bold',),
                        onvalue=1,
                        offvalue=0,
                        variable=drinks_var[count])
    drink.grid(row=count,
               column=0,
               sticky=W)

    # create entry box
    drinks_box.append("")
    drinks_text.append("")
    drinks_text[count] = StringVar()
    drinks_text[count].set("0")
    drinks_box[count] = Entry(drinks_panel,
                            font=("Dosis", 18, "bold"),
                            bd=1,
                            width=6,
                            state=DISABLED,
                            textvariable=drinks_text[count])
    drinks_box[count].grid(row=count,
                         column=1)
    count += 1

# add desserts list to checkbuttons
desserts_var = []
desserts_box = []
desserts_text = []
count = 0

for dessert in desserts_list:
    # create checkbutton
    desserts_var.append("")
    desserts_var[count] = IntVar()
    dessert = Checkbutton(desserts_panel,
                          text=dessert.title(),
                          font=('Dosis', 19, 'bold',),
                          onvalue=1,
                          offvalue=0,
                          variable=desserts_var[count])
    dessert.grid(row=count,
                 column=0,
                 sticky=W)

    # create entry box
    desserts_box.append("")
    desserts_text.append("")
    desserts_text[count] = StringVar()
    desserts_text[count].set("0")
    desserts_box[count] = Entry(desserts_panel,
                            font=("Dosis", 18, "bold"),
                            bd=1,
                            width=6,
                            state=DISABLED,
                            textvariable=desserts_text[count])
    desserts_box[count].grid(row=count,
                         column=1)
    count += 1

# label costs and entries products
var_food_cost = StringVar()
var_drink_cost = StringVar()
var_dessert_cost = StringVar()
var_subtotal = StringVar()
var_total = StringVar()
var_tax = StringVar()

cost_label_food = Label(costs_panel,
                        text="Food Cost",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
cost_label_food.grid(row=0, column=0, padx=41)

food_cost_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_food_cost)

food_cost_text.grid(row=0, column=1, padx=41)

# drinks
cost_label_drink = Label(costs_panel,
                        text="Drink Cost",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
cost_label_drink.grid(row=1, column=0, padx=41)

drink_cost_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_drink_cost)

drink_cost_text.grid(row=1, column=1, padx=41)

# dessert
cost_label_dessert = Label(costs_panel,
                        text="Dessert Cost",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
cost_label_dessert.grid(row=2, column=0, padx=41)

dessert_cost_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_dessert_cost)

dessert_cost_text.grid(row=2, column=1, padx=41)

# subtotal
var_subtotal = Label(costs_panel,
                        text="Subtotal",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
var_subtotal.grid(row=0, column=2, padx=41)

subtotal_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_subtotal)

subtotal_text.grid(row=0, column=3, padx=41)

# tax
var_tax = Label(costs_panel,
                        text="Tax",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
var_tax.grid(row=1, column=2, padx=41)

tax_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_tax)

tax_text.grid(row=1, column=3, padx=41)

# total
var_total = Label(costs_panel,
                        text="Total",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
var_total.grid(row=2, column=2, padx=41)

total_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_total)

total_text.grid(row=2, column=3, padx=41)

# buttons
buttons = ["total", "receipt", "save", "reset"]
columns = 0
for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=("Dosis", 14, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=9)

    button.grid(row=0,
                column=columns)
    columns += 1

# receipt area
receipt_text = Text(receipt_panel,
                    font=("Dosis", 19, "bold"),
                    bd=1,
                    width=42,
                    height=10)

receipt_text.grid(row=0,
                  column= 0)

# calculator
calculator_visor = Entry(calculator_panel,
                         font=("Dosis", 16, "bold"),
                         width=32,
                         bd=1)

calculator_visor.grid(row=0,
                      column=0,
                      columnspan=4)

buttons_calculator = ["7", "8", "9", "+", "4", "5", "6", "-",
                      "1", "2", "3", "x", "R", "B", "0", "/"]

row = 1
column = 0

for button in buttons_calculator:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=("Dosis", 16, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=8)

    button.grid(row=row,
                column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

# avoid window to be closed
app.mainloop()
