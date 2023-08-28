from tkinter import *

# operator calculator
operator = ""

# price list
foods_prices = [1.23, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drinks_prices = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
desserts_prices = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

# click button
def click_button(number):
    global operator
    operator = operator + number
    calculator_visor.delete(0, END)
    calculator_visor.insert(END, operator)

# delete button
def delete():
    global operator
    operator = ""
    calculator_visor.delete(0, END)

# get result button
def get_result():
    global operator
    result = str(eval(operator))
    calculator_visor.delete(0, END)
    calculator_visor.insert(0, result)
    operator = ""

# check what checklist was clicked so you can write
def check_check():
    x = 0
    for f in food_box:
        if food_var[x].get() == 1:
            food_box[x].config(state=NORMAL)
            if food_box[x].get() == "0":
                food_box[x].delete(0, END)
            food_box[x].focus()
        else:
            food_box[x].config(state=DISABLED)
            food_text[x].set("0")
        x += 1

    x = 0
    for f in drinks_box:
        if drinks_var[x].get() == 1:
            drinks_box[x].config(state=NORMAL)
            if drinks_box[x].get() == "0":
                drinks_box[x].delete(0, END)
            drinks_box[x].focus()
        else:
            drinks_box[x].config(state=DISABLED)
            drinks_text[x].set("0")
        x += 1

    x = 0
    for f in desserts_box:
        if desserts_var[x].get() == 1:
            desserts_box[x].config(state=NORMAL)
            if desserts_box[x].get() == "0":
                desserts_box[x].delete(0, END)
            desserts_box[x].focus()
        else:
            desserts_box[x].config(state=DISABLED)
            desserts_text[x].set("0")
        x += 1

# total button function, equations
def total():
    subtotal_food = 0
    p = 0
    for quantity in food_text:
        subtotal_food = subtotal_food + (float(quantity.get()) * foods_prices[p])
        p += 1

    subtotal_drink = 0
    p = 0
    for quantity in drinks_text:
        subtotal_drink = subtotal_drink + (float(quantity.get()) * drinks_prices[p])
        p += 1

    subtotal_dessert = 0
    p = 0
    for quantity in desserts_text:
        subtotal_dessert = subtotal_dessert + (float(quantity.get()) * desserts_prices[p])
        p += 1

    sub_total = subtotal_food + subtotal_drink + subtotal_dessert
    tax = sub_total * 0.07
    total = sub_total + tax

    var_food_cost.set(f"$ {round(subtotal_food, 2)}")
    var_drink_cost.set(f"$ {round(subtotal_drink, 2)}")
    var_dessert_cost.set(f"$ {round(subtotal_dessert, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")

    var_tax.set(f"$ {round(tax, 2)}")
    var_total.set(f"$ {round(total, 2)}")

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
title_label = Label(top_panel,
                    text="Facturation System",
                    fg="white",
                    font=("Dosis", 58),
                    bg="green",
                    width=22)

title_label.grid(row=0,
                 column=0)

# left panel
left_panel = Frame(app,
                   bd=1,
                   relief=FLAT)

left_panel.pack(side=LEFT)

# costs panel
costs_panel = Frame(left_panel,
                    bd=1, relief=FLAT,
                    bg="azure4",
                    padx=50)

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
right_panel = Frame(app,
                    bd=1,
                    relief=FLAT)

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
                       variable=food_var[count],
                       command=check_check)

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
                        variable=drinks_var[count],
                        command=check_check)

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
                          variable=desserts_var[count],
                          command=check_check)

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
label_subtotal = Label(costs_panel,
                        text="Subtotal",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
label_subtotal.grid(row=0, column=2, padx=41)

subtotal_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_subtotal)

subtotal_text.grid(row=0, column=3, padx=41)

# tax
label_tax = Label(costs_panel,
                        text="Tax",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
label_tax.grid(row=1, column=2, padx=41)

tax_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_tax)

tax_text.grid(row=1, column=3, padx=41)

# total
label_total = Label(costs_panel,
                        text="Total",
                        font=("Dosis", 12 ,"bold"),
                        bg="azure4",
                        fg="white")
label_total.grid(row=2, column=2, padx=41)

total_text = Entry(costs_panel,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_total)

total_text.grid(row=2, column=3, padx=41)

# buttons
buttons = ["total", "receipt", "save", "reset"]
buttons_made = []

columns = 0
for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=("Dosis", 14, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=9)

    buttons_made.append(button)

    button.grid(row=0,
                column=columns)
    columns += 1

buttons_made[0].config(command=total)

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

saved_buttons = []

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

    saved_buttons.append(button)

    button.grid(row=row,
                column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

saved_buttons[0].config(command=lambda : click_button("7"))
saved_buttons[1].config(command=lambda : click_button("8"))
saved_buttons[2].config(command=lambda : click_button("9"))
saved_buttons[3].config(command=lambda : click_button("+"))
saved_buttons[4].config(command=lambda : click_button("4"))
saved_buttons[5].config(command=lambda : click_button("5"))
saved_buttons[6].config(command=lambda : click_button("6"))
saved_buttons[7].config(command=lambda : click_button("-"))
saved_buttons[8].config(command=lambda : click_button("1"))
saved_buttons[9].config(command=lambda : click_button("2"))
saved_buttons[10].config(command=lambda : click_button("3"))
saved_buttons[11].config(command=lambda : click_button("*"))
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=delete)
saved_buttons[14].config(command=lambda : click_button("0"))
saved_buttons[15].config(command=lambda : click_button("/"))


# avoid window to be closed
app.mainloop()
