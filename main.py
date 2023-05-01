from datetime import *
from tkinter.font import BOLD
from xulyanh import *
from tkinter import *
import os
import tkinter as tk
from tkinter import messagebox
from billap import Bill_App


def register():
    global register_screen
    global username
    global password
    global username_entry
    global password_entry
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.resizable(width=False, height=False)
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.resizable(width=False, height=False)
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    messagebox.showinfo("Account", "Registration Success")
    register_screen.destroy()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_screen.destroy()
            messagebox.showinfo("Account", "Login Success")
            main_screen.destroy()
            main()
        else:
            password_not_recognised()
    else:
        user_not_found()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen.resizable(width=False, height=False)
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    user_not_found_screen.resizable(width=False, height=False)
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("850x690")
    main_screen.title("Account Login")
    main_screen.resizable(width=False, height=False)
    Label(text="Select Your Choice", fg="white", bg="#252d35", width="300", height="1",
          font=("Comic Sans MS", 13, BOLD)).pack()
    login_frame = LabelFrame(main_screen, bd=2, relief="groove")
    login_frame.pack()
    image_cover = xuly_image("https://ik.imagekit.io/nhom2/Cover.png?updatedAt=1682768752412", 850, 650)
    img1 = tk.Label(login_frame, image=image_cover)
    img1.pack(side="top", fill=BOTH)

    Button(login_frame, text="Login", height="2", width="15", command=login, font=("Comic Sans MS", 10, BOLD)).place(x=360, y=265)
    Button(login_frame, text="Register", height="2", width="15", command=register, font=("Comic Sans MS", 10, BOLD)).place(x=360, y=320)
    Button(login_frame, text="Admin", height="1", width="7", command=admin, font=("Comic Sans MS", 10, BOLD)).place(x=775, y=10)

    main_screen.mainloop()


def admin():
    main_screen.destroy()
    Bill_App()


class Product:
    def __init__(self, code, name, price, image, description, type):
        self.name = name
        self.price = price
        self.image = image
        self.description = description
        self.type = type
        self.code = code

    @classmethod
    def get_data(cls):
        file = open("Products.txt", "r", encoding="UTF-8")
        data = file.readlines()
        file.close()
        data = [i.strip("\n") for i in data]
        data = [i.split(",") for i in data]
        return data

    def append_data(self):
        file = open("Products.txt", "a", encoding="UTF-8")
        file.write("{},{},{},{},{}\n".format(self.name, self.price, self.image, self.description, self.type, self.code))
        file.close()


class Mainmenu(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.products_frame = LabelFrame(self.master, bd=3, relief="raised", text="PRODUCTS", font=("Comic Sans MS", 16, BOLD), fg="white", bg="#252d35", labelanchor=N)
        self.button_frame = LabelFrame(self.master, bd=3, relief="raised", text="CATEGORY", font=("Comic Sans MS", 16, BOLD), fg="white", bg="#252d35", labelanchor=N)
        self.heading = LabelFrame(self.master, bd=3, relief="raised", bg="#080a0d")
        self.image_logo = xuly_image("https://ik.imagekit.io/nhom2/Logo.png?updatedAt=1682769745947", 100, 40)
        self.lf = []
        self.button_add = []
        self.lf1 = []
        self.image_products = []
        self.pack()
        self.master.geometry("1360x740")
        self.master.title("TECH HUB SHOP")
        self.master.resizable(width=False, height=False)
        self.products = Product.get_data()
        self.cart_list = []
        self.create_widgets()

    def create_widgets(self):
        self.heading.place(x=0, y=0, width=1360, height=60)

        Label(self.heading, image=self.image_logo).grid(row=0, column=0, padx=10, pady=5)

        Label(self.heading, text="Empowering Your Tech Lifestyle", font=("Comic Sans MS", 16, BOLD), fg="white", bg="#080a0d").grid(row=0, column=2, padx=375, pady=5)

        Button(self.heading, text="Shopping Cart", font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=SOLID, activebackground="#252d35", activeforeground="#F6F5EC", command=self.show_cart).grid(row=0, column=3, padx=10, pady=5)

        self.button_frame.place(x=0, y=60, width=130, height=680)
        self.products_frame.place(x=130, y=60, width=1230, height=680)

        Button(self.button_frame, text="Laptop", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("face")).grid(row=0, column=0, padx=10)

        Button(self.button_frame, text="PC", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("body")).grid(row=1, column=0, padx=10)

        Button(self.button_frame, text="Apple", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("Cleanser")).grid(row=2, column=0, padx=10)

        Button(self.button_frame, text="Screen", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("Toner")).grid(row=3, column=0, padx=10)

        Button(self.button_frame, text="Keyboard", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("Serum")).grid(row=4, column=0, padx=10)

        Button(self.button_frame, text="Mouse", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("Whitening")).grid(row=5, column=0, padx=10)

        Button(self.button_frame, text="Headphones", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("Lotion")).grid(row=6, column=0, padx=10)

        Button(self.button_frame, text="Accessories", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("Exfoliate")).grid(row=7, column=0, padx=10)

        Button(self.button_frame, text="Others", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC", command=lambda: self.ShowFrames("Others")).grid(row=8, column=0, padx=10)

    def buy_product(self, product):
        self.cart_list.append(product)

    def HideAllFrame(self):
        for widget in self.products_frame.winfo_children():
            widget.destroy()

    def ShowFrames(self, phanloai):
        self.HideAllFrame()
        self.image_products = []
        self.button_add = []
        count = 0

        for product in self.products:
            if product[4] != phanloai:
                continue

            lf = LabelFrame(self.products_frame, bd=1, relief="solid", fg="white", bg="#252d35", text=product[0],
                            font=("Comic Sans MS", 12, "bold"), labelanchor=N)
            lf.grid(row=count // 4, column=count % 4, padx=10, pady=10)

            self.image_products.append(xuly_image(product[2], 70, 50))
            label_image = Label(lf, image=self.image_products[count])
            label_image.grid(row=2, column=0, padx=60, pady=5)

            Label(lf, text=product[3], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=1, column=0, padx=60, pady=5)
            Label(lf, text=product[1], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=3, column=0, padx=60, pady=5)

            button_add = Button(lf, command=lambda prod=product: self.buy_product(prod), text="Add to Cart", font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35", relief=SOLID)
            button_add.grid(row=4, column=0, padx=60, pady=5)
            self.button_add.append(button_add)

            count += 1

    def show_cart(self):
        self.HideAllFrame()
        self.image_products = []  # Xóa list hình ảnh sản phẩm
        self.lf1 = []  # Xóa list label frames
        count = 0  # Khởi tạo biến đếm để định vị vị trí

        for i in range(len(self.cart_list)):
            lf = LabelFrame(self.products_frame, bd=2, relief="solid", fg="white", bg="#252d35", text=self.cart_list[i][5], font=("Comic Sans MS", 12, BOLD), labelanchor=N)
            lf.grid(row=count//4, column=count % 4, padx=10, pady=5)
            self.lf1.append(lf)  # Thêm label frame vào list
            product_name = self.cart_list[i][0]
            product_image = self.cart_list[i][2]
            product_price = self.cart_list[i][1]
            self.image_products.append(xuly_image(product_image, 70, 50))
            label_image = Label(lf, image=self.image_products[count])
            label_image.grid(row=2, column=0, padx=10)
            Label(lf, text=product_name, font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=1, column=0, padx=60, pady=5)
            Label(lf, text=product_price, font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=3, column=0, padx=60, pady=5)
            Button(lf, command=lambda idx=i: self.remove_item(idx), text="Remove",
                   font=("Comic Sans MS", 12, "bold"), fg="white", bg="red").grid(row=4, column=0, padx=60, pady=5)
            count += 1  # Tăng biến đếm

        self.total_label = Label(self.products_frame, text="Total: 0 VNĐ", font=("Comic Sans MS", 12, BOLD), fg="#F6F5EC", bg="#252d35")
        self.total_label.place(x=5, y=605)
        self.total_label.config(text="Total: {:,} VNĐ".format(self.tong()).replace(".0", "").replace(",", "."))

        payment_button = Button(self.products_frame, text="Payment", font=("Comic Sans MS", 12, BOLD), fg="#F6F5EC",
                                bg="green", relief=SOLID, activebackground="green", activeforeground="#F6F5EC", command=self.show_order)
        payment_button.place(x=1140, y=600)

    def remove_item(self, idx):
        if 0 <= idx < len(self.cart_list):
            self.lf1[idx].destroy()
            del self.lf1[idx]  # Xóa label frame khỏi list
            self.cart_list.pop(idx)
        self.show_cart()  # Load lại giao diện cart

    def tong(self):
        return sum([float(product[1].replace(' VND', '').replace('.', '')) for product in self.cart_list])

    def show_bill(self):
        product_quantity = {}
        receipt = f"{'-' * 50}\n{'PAYMENT RECEIPT':^50}\n{'Time: '}{datetime.now():%d-%m-%Y %H:%M:%S}\n{'-' * 50}"
        total_amount = 0  # Initialize the total amount variable

        for product in self.cart_list:
            product_id = product[0]
            product_details = next((p for p in self.products if p[0] == product_id), None)
            if product_details:
                product_code = product_details[5]
                product_name = product_details[0]
                product_price = product_details[1]
                quantity = product_quantity.get(product_code, 0) + 1
                product_quantity[product_code] = quantity
                total_price = int(product_price.replace(",", "").replace("VND", "").replace(".", "")) * quantity
                total_amount += total_price  # Update the total amount
                receipt += f"\nCode: {product_code}\nProduct: {product_name}\nQuantity: {quantity}\nPrice: {product_price}\n{'-' * 20}"
        receipt += "\nTotal: {:,} VND".format(total_amount).replace(",", ".")
        bill_window.destroy()
        self.cart_list.clear()
        messagebox.showinfo("Order Confirmed", receipt)
        self.show_cart()

    def show_order(self):
        if len(self.cart_list) != 0:
            global bill_window
            bill_window = Toplevel(self.master)
            bill_window.title("Order")

            # Add label for "Payment Receipt"
            receipt_label = Label(bill_window, text="Phiếu thanh toán ", font=("Times New Roman", 16, "bold"))
            receipt_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

            # Add label for "Tech Hub"
            title_label = Label(bill_window, text="Tech Hub", font=("Times New Roman", 16, "bold"))
            title_label.grid(row=1, column=0, columnspan=4, padx=10, pady=3)

            # Add label for current date and time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            time_label = Label(bill_window, text=current_time, font=("Times New Roman", 12))
            time_label.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

            # Add dashed line separator
            line_label = Label(bill_window, text="-" * 80, font=("Times New Roman", 12, "bold"))
            line_label.grid(row=3, column=0, columnspan=5, padx=10, pady=5)

            # Create the table headers
            headers = ["Code", "Product", "Quantity", "Price", "Total"]
            for col, header in enumerate(headers):
                header_label = Label(bill_window, text=header, font=("Times New Roman", 14, "bold"))
                header_label.grid(row=4, column=col, padx=10, pady=5)

            # Create a dictionary to store the quantity of each product
            product_quantity = {}

            # Create the bill details
            row = 5  # Initialize the row variable
            total_amount = 0  # Initialize the total amount variable
            for product in self.cart_list:
                product_id = product[0]
                product_details = next((p for p in self.products if p[0] == product_id), None)
                if product_details:
                    product_code = product_details[5]
                    product_name = product_details[0]
                    product_price = product_details[1]
                    quantity = product_quantity.get(product_code, 0) + 1
                    product_quantity[product_code] = quantity

                    code_label = Label(bill_window, text=product_code, font=("Times New Roman", 12))
                    code_label.grid(row=row, column=0, padx=10, pady=5)

                    name_label = Label(bill_window, text=product_name, font=("Times New Roman", 12))
                    name_label.grid(row=row, column=1, padx=10, pady=5)

                    quantity_label = Label(bill_window, text=quantity, font=("Times New Roman", 12))
                    quantity_label.grid(row=row, column=2, padx=10, pady=5)

                    price_label = Label(bill_window, text=product_price, font=("Times New Roman", 12))
                    price_label.grid(row=row, column=3, padx=10, pady=5)

                    # Handle decimal point and space character in product_price
                    product_price = product_price.replace(",", "").replace("VND", "").replace(".", "").strip()
                    total_price = int(product_price) * quantity
                    total_amount += total_price  # Update the total amount
                    total_label = Label(bill_window, text="{:,} VNĐ".format(total_price), font=("Times New Roman", 12))
                    total_label.grid(row=row, column=4, padx=10, pady=5)

                    row += 1  # Increment the row variable

            # Add dashed line separator
            line_label = Label(bill_window, text="-" * 80, font=("Times New Roman", 12, "bold"))
            line_label.grid(row=row, column=0, columnspan=5, padx=10, pady=5)

            # Display the total amount
            row += 1  # Increment the row variable
            total_label = Label(bill_window, text="Total Amount: {:,} VNĐ".format(self.tong()),
                                font=("Times New Roman", 14, "bold"))
            total_label.grid(row=row, column=0, columnspan=3, padx=10, pady=10)
            # Add Confirm button
            confirm_button = Button(bill_window, text="Confirm", font=("Times New Roman", 12), command=self.show_bill)
            confirm_button.grid(row=row, column=2, sticky=E, padx=10, pady=5)

            # Add Cancel button
            cancel_button = Button(bill_window, text="Cancel", font=("Times New Roman", 12), command=bill_window.destroy)
            cancel_button.grid(row=row, column=3, sticky=E, padx=10, pady=5)
        else:
            messagebox.showinfo("Cart", "There are no products in the cart")


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main():
    root = Tk()
    app = Mainmenu(master=root)
    app.mainloop()


main_account_screen()
