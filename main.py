import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox




def open_new_window():
# Create a new window
    window = tk.Toplevel(root)


    def insert_record():
        # Get the values from the input fields
        name = name_entry.get()
        age = age_entry.get()

        # Insert the record into the table
        sql = "INSERT INTO records (name, age) VALUES (%s, %s)"
        values = (name, age)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("insert Successful", "Data inserted successfully")



    def delete_record():
        # Get the record ID to delete
        record_id = id_entry.get()

        # Delete the record from the table
        sql = "DELETE FROM records WHERE id = %s"
        value = (record_id,)
        cursor.execute(sql, value)
        conn.commit()
        messagebox.showinfo("delete Successful", "Data deleted successfully")



    def search_record():
        # Get the record ID to search
        record_id = id_entry.get()

        # Search for the record in the table
        sql = "SELECT * FROM records WHERE id = %s"
        value = (record_id,)
        cursor.execute(sql, value)
        record = cursor.fetchone()

        if record:
            result_label.config(text=f"Name: {record[1]}, Age: {record[2]}")
        else:
            result_label.config(text="Record not found")



    def update_record():
        # Get the record ID and new values
        record_id = id_entry.get()
        new_name = name_entry.get()
        new_age = age_entry.get()

        # Update the record in the table
        sql = "UPDATE records SET name = %s, age = %s WHERE id = %s"
        values = (new_name, new_age, record_id)
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("update Successful", "Data updated successfully")

    id_label = Label(window, text="Record ID:")
    id_label.pack()
    id_entry = Entry(window)
    id_entry.pack()

    name_label = Label(window, text="Name:")
    name_label.pack()
    name_entry = Entry(window)
    name_entry.pack()

    age_label = Label(window, text="Age:")
    age_label.pack()
    age_entry = Entry(window)
    age_entry.pack()

    insert_button = Button(window, text="Insert", command=insert_record)
    insert_button.pack()

    delete_button = Button(window, text="Delete", command=delete_record)
    delete_button.pack()

    search_button = Button(window, text="Search", command=search_record)
    search_button.pack()

    update_button = Button(window, text="Update", command=update_record)
    update_button.pack()

    result_label = Label(window, text="")
    result_label.pack()

    # Start the main loop
    window.mainloop()

    # Close the database connection when the window is closed
    conn.close()



# Create a database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rohtash#503",
    database="yummy"
)
cursor = conn.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS records (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    age INT
                )''')


# Create input fields and buttons






root = Tk()

root.title("Yummy Pizza Shop")

# ------------------------------------FUNCTIONS--------------------------------------------- #
#region Generating a random Order ID when starting a new order
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "YP_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id
#endregion

# Category Button Function
def displayPizzaMenu():
    pizzaCategoryFrame.configure(style = "selected.TFrame")
    sideCategoryFrame.configure(style= 'sideCategoryFrame.TFrame')
    drinkCategoryFrame .configure(style= 'drinkCategoryFrame.TFrame')
    #diplayPizzaMenu
    displayFrame = ttk.Frame(mainFrame, style='displayFrame.TFrame')
    displayFrame.grid(row=2, column=0, padx=3, pady=3, sticky="NSEW")
    # Display supreme pizza
    image1 = Image.open("images/supremePizza.png").resize((100, 100))
    supremeImage = ImageTk.PhotoImage(image1)
    supremeLabel = ttk.Label(displayFrame, image=supremeImage, background="#FFFFFF")
    supremeLabel.grid(row=0, column=0, sticky="NSEW")
    supremeLabel.image = supremeImage
    supremePizzaButton = ttk.Button(displayFrame, text="Supreme", compound="top",command= addSupreme)
    supremePizzaButton.grid(row=1, column=0, padx=0, sticky="NSEW")

    # Display sausage pizza
    image2 = Image.open("images/sausageSizzlePizza.png").resize((100, 100))
    sausageSizzleImage = ImageTk.PhotoImage(image2)
    sausageSizzleLabel = ttk.Label(displayFrame, image=sausageSizzleImage, background="#FFFFFF")
    sausageSizzleLabel.grid(row=0, column=1, sticky="NSEW")
    sausageSizzleLabel.image = sausageSizzleImage
    sausageSizzlePizzaButton = ttk.Button(displayFrame, text="Sausage Sizzle", compound="top",command=addSausagePizza)
    sausageSizzlePizzaButton.grid(row=1, column=1, padx=0, sticky="NSEW")

    # Display sausage pizza
    image3 = Image.open("images/hawaiianPizza.png").resize((100, 100))
    hawaiianImage = ImageTk.PhotoImage(image3)
    hawaiianLabel = ttk.Label(displayFrame, image=hawaiianImage, background="#FFFFFF")
    hawaiianLabel.grid(row=0, column=2, sticky="NSEW")
    hawaiianLabel.image = hawaiianImage
    hawaiianPizzaButton = ttk.Button(displayFrame, text="Hawaiian", compound="top",command=addHawaiianPizza)
    hawaiianPizzaButton.grid(row=1, column=2, padx=0, sticky="NSEW")

    # Display Sweet Chilli Chicken pizza
    image4 = Image.open("images/sweetChilliChicken.png").resize((100, 100))
    sweetChilliChickenImage = ImageTk.PhotoImage(image4)
    sweetChilliChickenLabel = ttk.Label(displayFrame, image=sweetChilliChickenImage, background="#FFFFFF")
    sweetChilliChickenLabel.grid(row=0, column=3, sticky="NSEW")
    sweetChilliChickenLabel.image = sweetChilliChickenImage
    sweetChilliChickenButton = ttk.Button(displayFrame, text="Sweet Chilli Chicken", compound="top",command=addSweetChilliChickenPizza)
    sweetChilliChickenButton.grid(row=1, column=3, padx=0, sticky="NSEW")

    # Display Peri Peri Chicken  pizza
    image5 = Image.open("images/periPeriChicken.png").resize((100, 100))
    perPeriChickenImage = ImageTk.PhotoImage(image5)
    perPeriChickenLabel = ttk.Label(displayFrame, image=perPeriChickenImage, background="#FFFFFF")
    perPeriChickenLabel.grid(row=0, column=4, sticky="NSEW")
    perPeriChickenLabel.image = perPeriChickenImage
    perPeriChickenButton = ttk.Button(displayFrame, text="Peri Peri Chicken", compound="top",command=addPeriPeriChickenPizza)
    perPeriChickenButton.grid(row=1, column=4, padx=0, sticky="NSEW")

    # Display Meat Lover pizza
    imageML = Image.open("images/meatLoverPizza.png").resize((100, 100))
    meatLoverImage = ImageTk.PhotoImage(imageML)
    meatLoverLabel = ttk.Label(displayFrame, image=meatLoverImage, background="#FFFFFF")
    meatLoverLabel.grid(row=0, column=5, sticky="NSEW")
    meatLoverLabel.image = meatLoverImage
    meatLoverButton = ttk.Button(displayFrame, text="Meat Lover", compound="top",command=addMeatLoverPizza)
    meatLoverButton.grid(row=1, column=5, padx=0, sticky="NSEW")

    # Display Garden Goodness pizza
    imageGg = Image.open("images/gardenGoodness.png").resize((100, 100))
    gardenGoodnessImage = ImageTk.PhotoImage(imageGg)
    gardenGoodnessLabel = ttk.Label(displayFrame, image=gardenGoodnessImage, background="#FFFFFF")
    gardenGoodnessLabel.grid(row=2, column=0, sticky="NSEW")
    gardenGoodnessLabel.image = gardenGoodnessImage
    gardenGoodnessButton = ttk.Button(displayFrame, text="Garden Goodness", compound="top",command=addGardenGoodnessPizza)
    gardenGoodnessButton.grid(row=3, column=0, padx=0, sticky="NSEW")

    # Display Veggie Lovers  pizza
    imageVC = Image.open("images/veganCheese.png").resize((100, 100))
    veganCheeseImage = ImageTk.PhotoImage(imageVC)
    veganCheeseLabel = ttk.Label(displayFrame, image=  veganCheeseImage, background="#FFFFFF")
    veganCheeseLabel.grid(row=2, column=1, sticky="NSEW")
    veganCheeseLabel.image =  veganCheeseImage
    veganCheeseButton = ttk.Button(displayFrame, text="Vegan Cheese", compound="top",command=addVeganCheesePizza)
    veganCheeseButton.grid(row=3, column=1, padx=0, sticky="NSEW")

    # Display pizza options
    # Size
    sizeOptionLabel = ttk.Label(displayFrame, text="SIZE", style="sizeLabel.TLabel")
    sizeOptionLabel.grid(row=5, column=0, sticky="WE")
    sizeOptionLabel.configure(
        anchor="w",
        font=("Helvetica", 12)
    )
    smallSizeButton = ttk.Button(displayFrame, text="Small(8 Inch)",command= addSmallSize)
    smallSizeButton.grid(row=6, column=0, padx=0, sticky="NSEW")
    largeSizeButton = ttk.Button(displayFrame, text="Large(11 Inch)",command=addLargeSize)
    largeSizeButton.grid(row=7, column=0, padx=0, sticky="NSEW")
    xLargeSizeButton = ttk.Button(displayFrame, text="Extra Large(12 Inch)",command=addXLargeSize)
    xLargeSizeButton.grid(row=8, column=0, padx=0, sticky="NSEW")
    # Base
    baseOptionLabel = ttk.Label(displayFrame, text="BASE", style="baseLabel.TLabel")
    baseOptionLabel.grid(row=9, column=0, sticky="WE")
    baseOptionLabel.configure(
        anchor="w",
        font=("Helvetica", 12)
    )
    traditionalBaseButton = ttk.Button(displayFrame, text="Traditional Base",command=addTraditionalBase)
    traditionalBaseButton.grid(row=10, column=0, padx=0, sticky="NSEW")
    wholemealBaseButton = ttk.Button(displayFrame, text="Wholemeal Base",command=addWholemealBase)
    wholemealBaseButton.grid(row=11, column=0, padx=0, sticky="NSEW")
    glutenFreeBaseButton = ttk.Button(displayFrame, text="Gluten Free ",command=addGlutenFreeBase)
    glutenFreeBaseButton.grid(row=12, column=0, padx=0, sticky="NSEW")
    # Sauce
    sauceOptionLabel = ttk.Label(displayFrame, text="SAUCE", style="sauceLabel.TLabel")
    sauceOptionLabel.grid(row=13, column=0, sticky="WE")
    sauceOptionLabel.configure(
        anchor="w",
        font=("Helvetica", 12)
    )
    tomatoSauceButton = ttk.Button(displayFrame, text="Tomato Sauce",command=addTomatoSauce)
    tomatoSauceButton.grid(row=14, column=0, padx=0, sticky="NSEW")
    bbqSauceButton = ttk.Button(displayFrame, text="BBQ Sauce",command=addBBQSauce)
    bbqSauceButton.grid(row=15, column=0, padx=0, sticky="NSEW")


def displaySidesMenu():
    sideCategoryFrame.configure(
        style="selected.TFrame"
    )
    pizzaCategoryFrame.configure(style='pizzaCategoryFrame.TFrame')
    drinkCategoryFrame.configure(style='drinkCategoryFrame.TFrame')

    sidesDisplayFrame = ttk.Frame(mainFrame, style='displayFrame.TFrame')
    sidesDisplayFrame.grid(row=2, column=0, padx=3, pady=3, sticky="NSEW")

    # Display Creamy Mushroom pasta
    image6 = Image.open("images/Creamy Mushroom Pasta.png").resize((100, 100))
    CreamyMushroomPastaImage = ImageTk.PhotoImage(image6)
    CreamyMushroomPastaLabel = ttk.Label(sidesDisplayFrame, image=CreamyMushroomPastaImage, background="#FFFFFF")
    CreamyMushroomPastaLabel.grid(row=0, column=0, sticky="W")
    CreamyMushroomPastaLabel.image = CreamyMushroomPastaImage
    CreamyMushroomPastaButton = ttk.Button(sidesDisplayFrame, text="Mushroom Pasta", compound="top",command=addMushroomPasta)
    CreamyMushroomPastaButton.grid(row=1, column=0, padx=0, sticky="NSEW")

    # Display Bolognese pasta
    image7 = Image.open("images/Bolognese Pasta.png").resize((100, 100))
    BolognesePastaImage = ImageTk.PhotoImage(image7)
    BolognesePastaLabel = ttk.Label(sidesDisplayFrame, image=BolognesePastaImage, background="#FFFFFF")
    BolognesePastaLabel.grid(row=0, column=1, sticky="W")
    BolognesePastaLabel.image = BolognesePastaImage
    BolognesePastaButton = ttk.Button(sidesDisplayFrame, text="Bolognese Pasta", compound="top",command=addBolognesePasta)
    BolognesePastaButton.grid(row=1, column=1, padx=0, sticky="NSEW")


    # Display chicken wings
    image11 = Image.open("images/chicken wings.png").resize((100, 100))
    chickenwingsImage = ImageTk.PhotoImage(image11)
    chickenwingsLabel = ttk.Label(sidesDisplayFrame, image=chickenwingsImage, background="#FFFFFF")
    chickenwingsLabel.grid(row=0, column=2, sticky="W")
    chickenwingsLabel.image = chickenwingsImage
    chickenwingsButton = ttk.Button(sidesDisplayFrame, text="Chicken Wings", compound="top",command=addChickenWings)
    chickenwingsButton.grid(row=1, column=2, padx=0, sticky="NSEW")

    # Display garlic bread
    image12 = Image.open("images/garlic bread.png").resize((100, 100))
    garlicbreadImage = ImageTk.PhotoImage(image12)
    garlicbreadLabel = ttk.Label(sidesDisplayFrame, image= garlicbreadImage, background="#FFFFFF")
    garlicbreadLabel.grid(row=0, column=3, sticky="W")
    garlicbreadLabel.image = garlicbreadImage
    garlicbreadButton = ttk.Button(sidesDisplayFrame, text="Garlic Bread", compound="top",command=addGarlicBread)
    garlicbreadButton.grid(row=1, column=3, padx=0, sticky="NSEW")

    #Cover the pizza option
    blankLabel = ttk.Label(sidesDisplayFrame, text = " ",style="blankLabel.TLabel")
    blankLabel.grid(row=5, column=0, sticky="WE")
    blankLabel = ttk.Label(sidesDisplayFrame, text = " ",style="blankLabel.TLabel")
    blankLabel.grid(row=6, column=0, sticky="WE")
    blankLabel = ttk.Label(sidesDisplayFrame, text = " ", style="blankLabel.TLabel")
    blankLabel.grid(row=7, column=0, sticky="WE")

def displayDrinkMenu():
    drinkCategoryFrame.configure(
        style="selected.TFrame"
    )
    sideCategoryFrame.configure(style='sideCategoryFrame.TFrame')
    pizzaCategoryFrame.configure(style='pizzaCategoryFrame.TFrame')

    drinkDisplayFrame = ttk.Frame(mainFrame, style='displayFrame.TFrame')
    drinkDisplayFrame.grid(row=2, column=0, padx=3, pady=3, sticky="NSEW")
#Display sprite
    image8 = Image.open("images/sprite.png").resize((100,100))
    spriteImage = ImageTk.PhotoImage(image8)
    spriteLabel = ttk.Label(drinkDisplayFrame, image = spriteImage, background="#FFFFFF")
    spriteLabel.grid(row = 0, column = 0, sticky = "W")
    spriteLabel.image = spriteImage
    spriteButton = ttk.Button(drinkDisplayFrame,text= "Sprite", compound="top",command=addSprite)
    spriteButton.grid(row = 1, column= 0, padx= 0,sticky = "NSEW")

    # Display Coke
    image9 = Image.open("images/Coke.png").resize((100, 100))
    CokeImage = ImageTk.PhotoImage(image9)
    CokeLabel = ttk.Label(drinkDisplayFrame, image=CokeImage, background="#FFFFFF")
    CokeLabel.grid(row=0, column=1, sticky="W")
    CokeLabel.image = CokeImage
    CokeButton = ttk.Button(drinkDisplayFrame, text="Coke", compound="top",command=addCoke)
    CokeButton.grid(row=1, column=1, padx=0, sticky="NSEW")
    # Display fanta
    image10 = Image.open("images/fanta.png").resize((100, 100))
    fantaImage = ImageTk.PhotoImage(image10)
    fantaLabel = ttk.Label(drinkDisplayFrame, image=fantaImage, background="#FFFFFF")
    fantaLabel.grid(row=0, column=2, sticky="W")
    fantaLabel.image = fantaImage
    fantaButton = ttk.Button(drinkDisplayFrame, text="Fanta", compound="top",command=addFanta)
    fantaButton.grid(row=1, column=2, padx=0, sticky="NSEW")
    # Display juice
    image13 = Image.open("images/juice.png").resize((100, 100))
    juiceImage = ImageTk.PhotoImage(image13)
    juiceLabel = ttk.Label(drinkDisplayFrame, image=juiceImage, background="#FFFFFF")
    juiceLabel.grid(row=0, column=3, sticky="W")
    juiceLabel.image = juiceImage
    juiceButton = ttk.Button(drinkDisplayFrame, text="Juice", compound="top",command=addJuice)
    juiceButton.grid(row=1, column=3, padx=0, sticky="NSEW")

#Add item to order
def addSupreme():
    itemCost = 24
    orderTransaction.insert("", tk.END, values=("Supreme Pizza", "1", "24"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child,"value")[2])
        Total_Input.set("{:.2f}".format(itemCost-24))

def addSausagePizza():
    itemCost = 24
    orderTransaction.insert("", tk.END, values=("Sausage Sizzle Pizza", "1", "24"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 24))

def addHawaiianPizza():
    itemCost = 18
    orderTransaction.insert("", tk.END, values=("Hawaiian Pizza", "1", "18"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 18))

def addSweetChilliChickenPizza():
    itemCost = 24
    orderTransaction.insert("", tk.END, values=("Sweet Chilli Chicken Pizza", "1", "24"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 24))

def addPeriPeriChickenPizza():
    itemCost = 24
    orderTransaction.insert("", tk.END, values=("Peri Peri Chicken Pizza", "1", "24"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 24))

def addMeatLoverPizza():
    itemCost = 24
    orderTransaction.insert("", tk.END, values=("Meat Lover Pizza", "1", "24"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 24))

def addGardenGoodnessPizza():
    itemCost = 18
    orderTransaction.insert("", tk.END, values=("Garden Goodness Pizza", "1", "18"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 18))

def addVeganCheesePizza():
    itemCost = 18
    orderTransaction.insert("", tk.END, values=("Vegan Cheese Pizza", "1", "18"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 18))

def addSmallSize():
    itemCost = 0
    orderTransaction.insert("", tk.END, values=("---Small Size", "1", "0"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 0))

def addLargeSize():
    itemCost = 5
    orderTransaction.insert("", tk.END, values=("---Large Size", "1", "5"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 5))

def addXLargeSize():
    itemCost = 10
    orderTransaction.insert("", tk.END, values=("---X Large Size", "1", "10"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 10))

def addTraditionalBase():
    itemCost = 0
    orderTransaction.insert("", tk.END, values=("---Traditional Base", "1", "0"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 0))

def addWholemealBase():
    itemCost = 0
    orderTransaction.insert("", tk.END, values=("---Wholemeal Base", "1", "0"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 0))

def addGlutenFreeBase():
    itemCost = 0
    orderTransaction.insert("", tk.END, values=("---Gluten Free Base", "1", "0"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 0))

def addTomatoSauce():
    itemCost = 0
    orderTransaction.insert("", tk.END, values=("---Tomato Sauce", "1", "0"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 0))

def addBBQSauce():
    itemCost = 0
    orderTransaction.insert("", tk.END, values=("---BBQ Sauce", "1", "0"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 0))

def addMushroomPasta():
    itemCost = 18
    orderTransaction.insert("", tk.END, values=("Mushroom Pasta", "1", "18"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 18))

def addBolognesePasta():
    itemCost = 10
    orderTransaction.insert("", tk.END, values=("Bolognese Pasta", "1", "10"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 10))

def addChickenWings():
    itemCost = 20
    orderTransaction.insert("", tk.END, values=("Chicken Wings", "1", "20"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 20))

def addGarlicBread():
    itemCost = 20
    orderTransaction.insert("", tk.END, values=("Garlic Bread", "1", "20"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 20))

def addSprite():
    itemCost = 4
    orderTransaction.insert("", tk.END, values=("Sprite", "1", "4"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 4))

def addCoke():
    itemCost = 4
    orderTransaction.insert("", tk.END, values=("Coke", "1", "4"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 4))

def addFanta():
    itemCost = 4
    orderTransaction.insert("", tk.END, values=("Fanta", "1", "4"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 4))

def addJuice():
    itemCost = 4
    orderTransaction.insert("", tk.END, values=("Juice", "1", "4"))
    for child in orderTransaction.get_children():
        itemCost += float(orderTransaction.item(child, "value")[2])
        Total_Input.set("{:.2f}".format(itemCost - 4))






#Other button function
def studentDiscount():
    original_total = float(Total_Input.get())
    discounted_total = original_total * 0.9
    Total_Input.set("{:.2f}".format(discounted_total))

def deleteItem():
    selected_item = orderTransaction.selection()[0]
    item_cost = float(orderTransaction.item(selected_item, "values")[2])
    orderTransaction.delete(selected_item)
    new_item_cost = 0.0
    for child in orderTransaction.get_children():
        new_item_cost += float(orderTransaction.item(child, "values")[2])
    Total_Input.set("{:.2f}".format(new_item_cost))

def cardPayment():
    orderTransaction.delete(*orderTransaction.get_children())
    orderIDLabel.configure(text = "ORDER ID: "+ ORDER_ID())
    new_item_cost = 0.0
    for child in orderTransaction.get_children():
        new_item_cost += float(orderTransaction.item(child, "values")[2])
    Total_Input.set("{:.2f}".format(new_item_cost))




# ---------------------------------- STYLING AND IMAGES ------------------------------------ #
#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#FFFFFF")
s.configure('MenuFrame.TFrame', background = "#F8F8F8")

s.configure('pizzaCategoryFrame.TFrame', background = "#F8F8F8")
s.configure('sideCategoryFrame.TFrame', background = "#F8F8F8")
s.configure('drinkCategoryFrame.TFrame', background = "#F8F8F8")
s.configure('selected.TFrame', background = "#DC0602")
s.configure('displayFrame.TFrame', background = "#FFFFFF")
root.configure(background ='#FFFFFF')

s.configure('MenuLabel.TLabel',
            background = "#F8F8F8",
            font = ("Arial", 50, "italic"),
            foreground = "black",
            padding = (5, 5, 5, 5),
            anchor = "center",
            )

s.configure('sizeLabel.TLabel',background ="#FFFFFF")
s.configure('baseLabel.TLabel',background ="#FFFFFF")
s.configure('sauceLabel.TLabel',background ="#FFFFFF")
s.configure('blankLabel.TLabel',background ="#FFFFFF")
s.configure('OrderFrame.TFrame', background = "#F8F8F8")
s.configure('orderTotalLabel.TLabel',background ="#F8F8F8")
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )
# region Images
# Top Banner images
LogoImageObject = Image.open("images/logo.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("images/banner.jpeg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)
#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style='MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 2)

menuFrame = ttk.Frame(mainFrame, style='MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW",rowspan = 2)

displayFrame = ttk.Frame(mainFrame, style='displayFrame.TFrame')
displayFrame.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = "NSEW")



# Category Frames
pizzaCategoryFrame = ttk.Frame(menuFrame,style = "pizzaCategoryFrame.TFrame")
pizzaCategoryFrame.grid(row = 1, column = 0, sticky = "NSEW")

sideCategoryFrame = ttk.Frame(menuFrame, style ="sideCategoryFrame.TFrame")
sideCategoryFrame.grid(row = 1, column = 1, sticky ="NSEW")

drinkCategoryFrame = ttk.Frame(menuFrame, style ="drinkCategoryFrame.TFrame")
drinkCategoryFrame.grid(row = 1, column = 2, sticky ="NSEW")

#endregion

#Display pizza menu by default
#Display supreme pizza
image1 = Image.open("images/supremePizza.png").resize((100,100))
supremeImage = ImageTk.PhotoImage(image1)
supremeLabel = ttk.Label(displayFrame, image = supremeImage, background="#FFFFFF")
supremeLabel.grid(row = 0, column = 0, sticky = "NSEW")
supremeLabel.image = supremeImage
supremePizzaButton = ttk.Button(displayFrame,text= "Supreme", compound="top",command= addSupreme)
supremePizzaButton.grid(row = 1, column= 0, padx= 0,sticky = "NSEW")

#Display sausage pizza
image2 = Image.open("images/sausageSizzlePizza.png").resize((100,100))
sausageSizzleImage = ImageTk.PhotoImage(image2)
sausageSizzleLabel = ttk.Label(displayFrame, image = sausageSizzleImage, background="#FFFFFF")
sausageSizzleLabel.grid(row = 0, column = 1, sticky = "NSEW")
sausageSizzleLabel.image = sausageSizzleImage
sausageSizzlePizzaButton = ttk.Button(displayFrame, text="Sausage Sizzle",compound="top",command=addSausagePizza)
sausageSizzlePizzaButton.grid(row=1, column=1, padx=0, sticky="NSEW")

# Display sausage pizza
image3 = Image.open("images/hawaiianPizza.png").resize((100, 100))
hawaiianImage = ImageTk.PhotoImage(image3)
hawaiianLabel = ttk.Label(displayFrame, image=hawaiianImage, background="#FFFFFF")
hawaiianLabel.grid(row=0, column=2, sticky="NSEW")
hawaiianLabel.image = hawaiianImage
hawaiianPizzaButton = ttk.Button(displayFrame, text="Hawaiian", compound="top",command=addHawaiianPizza)
hawaiianPizzaButton.grid(row=1, column=2, padx=0, sticky="NSEW")

# Display Sweet Chilli Chicken  pizza
image4 = Image.open("images/sweetChilliChicken.png").resize((100, 100))
sweetChilliChickenImage = ImageTk.PhotoImage(image4)
sweetChilliChickenLabel = ttk.Label(displayFrame, image=sweetChilliChickenImage, background="#FFFFFF")
sweetChilliChickenLabel.grid(row=0, column=3, sticky="NSEW")
sweetChilliChickenLabel.image = sweetChilliChickenImage
sweetChilliChickenButton = ttk.Button(displayFrame, text="Sweet Chilli Chicken", compound="top",command=addSweetChilliChickenPizza)
sweetChilliChickenButton.grid(row=1, column=3, padx=0, sticky="NSEW")

# Display Peri Peri Chicken  pizza
image5 = Image.open("images/periPeriChicken.png").resize((100, 100))
perPeriChickenImage = ImageTk.PhotoImage(image5)
perPeriChickenLabel = ttk.Label(displayFrame, image=perPeriChickenImage, background="#FFFFFF")
perPeriChickenLabel.grid(row=0, column=4, sticky="NSEW")
perPeriChickenLabel.image = perPeriChickenImage
perPeriChickenButton = ttk.Button(displayFrame, text="Peri Peri Chicken", compound="top",command=addPeriPeriChickenPizza)
perPeriChickenButton.grid(row=1, column=4, padx=0, sticky="NSEW")

# Display Meat Lover pizza
imageML = Image.open("images/meatLoverPizza.png").resize((100, 100))
meatLoverImage = ImageTk.PhotoImage(imageML)
meatLoverLabel = ttk.Label(displayFrame, image=meatLoverImage, background="#FFFFFF")
meatLoverLabel.grid(row=0, column=5, sticky="NSEW")
meatLoverLabel.image = meatLoverImage
meatLoverButton = ttk.Button(displayFrame, text="Meat Lover", compound="top",command=addMeatLoverPizza)
meatLoverButton.grid(row=1, column=5, padx=0, sticky="NSEW")

# Display Garden Goodness pizza
imageGg = Image.open("images/gardenGoodness.png").resize((100, 100))
gardenGoodnessImage = ImageTk.PhotoImage(imageGg)
gardenGoodnessLabel = ttk.Label(displayFrame, image=gardenGoodnessImage, background="#FFFFFF")
gardenGoodnessLabel.grid(row=2, column=0, sticky="NSEW")
gardenGoodnessLabel.image = gardenGoodnessImage
gardenGoodnessButton = ttk.Button(displayFrame, text="Garden Goodness", compound="top",command=addGardenGoodnessPizza)
gardenGoodnessButton.grid(row=3, column=0, padx=0, sticky="NSEW")

# Display Veggie Lovers  pizza
imageVC = Image.open("images/veganCheese.png").resize((100, 100))
veganCheeseImage = ImageTk.PhotoImage(imageVC)
veganCheeseLabel = ttk.Label(displayFrame, image=veganCheeseImage, background="#FFFFFF")
veganCheeseLabel.grid(row=2, column=1, sticky="NSEW")
veganCheeseLabel.image = veganCheeseImage
veganCheeseButton = ttk.Button(displayFrame, text="Vegan Cheese", compound="top",command=addVeganCheesePizza)
veganCheeseButton.grid(row=3, column=1, padx=0, sticky="NSEW")

#Display pizza options
#Size
sizeOptionLabel = ttk.Label(displayFrame, text="SIZE", style="sizeLabel.TLabel")
sizeOptionLabel.grid(row=5, column=0, sticky="WE")
sizeOptionLabel.configure(
    anchor="w",
    font=("Helvetica", 12)
    )
smallSizeButton = ttk.Button(displayFrame, text="Small(8 Inch)",command= addSmallSize)
smallSizeButton.grid(row=6, column=0, padx=0, sticky="NSEW")
largeSizeButton = ttk.Button(displayFrame, text="Large(11 Inch)",command= addLargeSize)
largeSizeButton.grid(row=7, column=0, padx=0, sticky="NSEW")
xLargeSizeButton = ttk.Button(displayFrame, text="Extra Large(12 Inch)",command= addXLargeSize)
xLargeSizeButton.grid(row=8, column=0, padx=0, sticky="NSEW")
#Base
baseOptionLabel = ttk.Label(displayFrame, text="BASE", style="baseLabel.TLabel")
baseOptionLabel.grid(row=9, column=0, sticky="WE")
baseOptionLabel.configure(
        anchor="w",
        font=("Helvetica", 12)
)
traditionalBaseButton = ttk.Button(displayFrame, text="Traditional Base",command=addTraditionalBase)
traditionalBaseButton.grid(row=10, column=0, padx=0, sticky="NSEW")
wholemealBaseButton = ttk.Button(displayFrame, text="Wholemeal Base",command=addWholemealBase)
wholemealBaseButton.grid(row=11, column=0, padx=0, sticky="NSEW")
glutenFreeBaseButton = ttk.Button(displayFrame, text="Gluten Free ",command=addGlutenFreeBase)
glutenFreeBaseButton.grid(row=12, column=0, padx=0, sticky="NSEW")
#Sauce
sauceOptionLabel = ttk.Label(displayFrame, text="SAUCE", style="sauceLabel.TLabel")
sauceOptionLabel.grid(row=13, column=0, sticky="WE")
sauceOptionLabel.configure(
        anchor="w",
        font=("Helvetica", 12)
)
tomatoSauceButton = ttk.Button(displayFrame, text="Tomato Sauce",command=addTomatoSauce)
tomatoSauceButton.grid(row=14, column=0, padx=0, sticky="NSEW")
bbqSauceButton = ttk.Button(displayFrame, text="BBQ Sauce",command=addBBQSauce)
bbqSauceButton.grid(row=15, column=0, padx=0, sticky="NSEW")






# region Top Banner Section
LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background="#FFFFFF")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background="#FFFFFF")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")
# endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE", columnspan = 3)
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

# endregion

#Category Buttons
pizzaCategoryButton = ttk.Button(pizzaCategoryFrame, text = "Pizza", command =displayPizzaMenu)
pizzaCategoryButton.grid(row = 0, column= 0, padx= 2, pady= 2, sticky = "NSEW",columnspan = 3)

sideCategoryButton = ttk.Button(sideCategoryFrame, text = "Sides",command =displaySidesMenu)
sideCategoryButton.grid(row = 0, column= 1, padx= 2, pady=2,sticky = "NSEW")

drinkCategoryButton = ttk.Button(drinkCategoryFrame, text = "Drink", command =displayDrinkMenu)
drinkCategoryButton.grid(row = 0, column= 2, padx= 2, pady= 2,sticky = "NSEW")

# endregion



#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="black", background="#D6D6D6",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding=(5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW",columnspan = 2)

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID: "+ ORDER_ID())
orderIDLabel.configure(
    background = "#D6D6D6",
    foreground = "black",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady =1,columnspan = 2)

customerIDLabel = ttk.Label(orderFrame, text = "Customer ID : ")
customerIDLabel.configure(
    background = "#D6D6D6",
    foreground = "black",
    font = ("Helvetica", 11, "italic"),
    anchor="w",
)
customerIDLabel.grid(row = 2, column = 0, sticky = "EW")

newCustomerButton=ttk.Button(orderFrame, text = "NEW",command=open_new_window)
newCustomerButton.grid(row = 2, column= 1, padx= 1,sticky = "E")

#===Order transaction Treeview===
orderTransactionFrame = ttk.Frame(orderFrame, style = 'orderTransaction.TLabel')
orderTransactionFrame.grid(row = 3, column = 0, sticky = "NSEW",columnspan = 2)


scroll_x = Scrollbar(orderTransactionFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(orderTransactionFrame,orient=VERTICAL)

orderTransaction=ttk.Treeview(orderTransactionFrame, columns=("Item","Qty","Amount"),xscrollcommand=scroll_x.set,yscrollcommand= scroll_y.set,style = 'orderTransaction.TLabel',selectmode="extended")
orderTransaction.grid(row=0, column=0, sticky="NSEW")

orderTransaction.heading("Item",text="Item")
orderTransaction.heading("Qty",text="Qty")
orderTransaction.heading("Amount",text="Amount")

orderTransaction['show']='headings'

orderTransaction.column("Item",width= 200)
orderTransaction.column("Qty",width= 30)
orderTransaction.column("Amount",width= 70)

scroll_x.grid(row=1, column=0, sticky="EW")
scroll_y.grid(row=0, column=1, sticky="NS")
orderTransaction.grid(row=0, column=0, sticky="NSEW")

#order Total
Total_Input = StringVar()
orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : $", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 4, column = 0, sticky = "E")
orderTotal=Entry(orderFrame, textvariable= Total_Input,width=20)
orderTotal.grid(row=4,column= 1,sticky= "W",columnspan = 2)

#Other Buttons
studentDiscountButton = ttk.Button(orderFrame,text= "Student Discount",command=studentDiscount)
studentDiscountButton.grid(row=5,column= 0, sticky="EW")
deleteItemButton = ttk.Button(orderFrame,text= "Delete Item",command= deleteItem)
deleteItemButton.grid(row=5,column= 1, sticky="EW")
cashPaymentButton = ttk.Button(orderFrame, text = "CASH")
cashPaymentButton.grid(row = 6, column = 0, sticky = "EW")
cardPaymentButton = ttk.Button(orderFrame, text = "CARD",command=cardPayment)
cardPaymentButton.grid(row = 6, column = 1, sticky = "EW")

# endregion
#----------------------------- GRID CONFIGURATIONS -------------------------------------------#
mainFrame.columnconfigure(0, weight = 1)
mainFrame.columnconfigure(1, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.columnconfigure(1, weight = 1)
menuFrame.columnconfigure(2, weight = 1)
pizzaCategoryFrame.columnconfigure(0, weight=1)
sideCategoryFrame.columnconfigure(1, weight=1)
drinkCategoryFrame.columnconfigure(2, weight=1)
orderFrame.columnconfigure(0, weight= 1)
orderFrame.rowconfigure(3,weight= 1)
orderTransactionFrame.grid_rowconfigure(0, weight=1)
orderTransactionFrame.grid_columnconfigure(0, weight=1)




root.mainloop()
