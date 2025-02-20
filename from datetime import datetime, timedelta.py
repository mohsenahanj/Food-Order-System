import tkinter as tk
from tkinter import messagebox, StringVar
from datetime import datetime
import os
import webbrowser

class FoodOrderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Food Order System")
        self.master.geometry("500x800")

        self.food_options = ['Pizza', 'Burger', 'Sushi', 'Pasta', 'Salad']
        self.drink_options = ['Coke', 'Water', 'Juice', 'Tea', 'Coffee']
        self.payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Cash']

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Membership Code").grid(row=0)
        self.membership_entry = tk.Entry(self.master)
        self.membership_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Customer Name").grid(row=1)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Phone Number (11 digits)").grid(row=2)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=2, column=1)

        tk.Label(self.master, text="Address").grid(row=3)
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1)
        self.address_entry.bind('<KeyRelease>', self.update_map_link)

        tk.Label(self.master, text="Zip Code").grid(row=4)
        self.zip_entry = tk.Entry(self.master)
        self.zip_entry.grid(row=4, column=1)

        tk.Label(self.master, text="Select Food Item").grid(row=5)
        self.food_var = StringVar(value=self.food_options[0])
        self.food_menu = tk.OptionMenu(self.master, self.food_var, *self.food_options)
        self.food_menu.grid(row=5, column=1)

        tk.Label(self.master, text="Food Description").grid(row=6)
        self.food_description_entry = tk.Entry(self.master)
        self.food_description_entry.grid(row=6, column=1)

        tk.Label(self.master, text="Select Drink").grid(row=7)
        self.drink_var = StringVar(value=self.drink_options[0])
        self.drink_menu = tk.OptionMenu(self.master, self.drink_var, *self.drink_options)
        self.drink_menu.grid(row=7, column=1)

        tk.Label(self.master, text="Quantity").grid(row=8)
        self.quantity_entry = tk.Entry(self.master)
        self.quantity_entry.grid(row=8, column=1)

        tk.Label(self.master, text="Select Payment Method").grid(row=9)
        self.payment_var = StringVar(value=self.payment_methods[0])
        self.payment_menu = tk.OptionMenu(self.master, self.payment_var, *self.payment_methods)
        self.payment_menu.grid(row=9, column=1)

        tk.Button(self.master, text='Add Order Item', command=self.add_order_item).grid(row=10, column=0)
        tk.Button(self.master, text='Submit Order', command=self.submit_order).grid(row=10, column=1)

        self.order_items = []
        self.order_table = tk.Text(self.master, height=10, width=50)
        self.order_table.grid(row=11, columnspan=2)

        self.map_label = tk.Label(self.master, text="")
        self.map_label.grid(row=12, columnspan=2)

        tk.Button(self.master, text='Select Location on Map', command=self.open_google_maps).grid(row=13, columnspan=2)

    def add_order_item(self):
        food_name = self.food_var.get()
        food_description = self.food_description_entry.get()
        drink_name = self.drink_var.get()
        quantity = self.quantity_entry.get()

        if quantity.isdigit() and int(quantity) > 0:
            self.order_items.append((food_name, food_description, drink_name, int(quantity)))
            self.order_table.insert(tk.END, f"{food_name} ({food_description}) + {drink_name} x{quantity}\n")
            self.quantity_entry.delete(0, tk.END)
            self.food_description_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added {quantity} of {food_name} and {drink_name} to your order.")
        else:
            messagebox.showerror("Input Error", "Please enter a valid quantity.")

    def submit_order(self):
        membership_code = self.membership_entry.get()
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        zip_code = self.zip_entry.get()
        
        if not name or not phone or not address or not zip_code or not self.order_items:
            messagebox.showerror("Input Error", "Please fill out all fields and add at least one order item.")
            return
        if len(phone) != 11 or not phone.isdigit():
            messagebox.showerror("Input Error", "Phone number must be exactly 11 digits.")
            return

        order_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.save_order_to_txt(membership_code, name, phone, address, zip_code, order_time)

        messagebox.showinfo("Order Submitted", "Your order has been submitted successfully!")
        self.clear_fields()

    def save_order_to_txt(self, membership_code, name, phone, address, zip_code, order_time):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop, "food_order.txt")
        
        order_items_str = '\n'.join([f"{food} ({description}) + {drink} x{qty}" for food, description, drink, qty in self.order_items])
        order_content = f"""
        Order Summary
        Membership Code: {membership_code}
        Name: {name}
        Phone: {phone}
        Address: {address}
        Zip Code: {zip_code}
        Order Time: {order_time}
        Order Items:
        {order_items_str}
        """
        with open(file_path, 'w') as f:
            f.write(order_content.strip())

    def clear_fields(self):
        self.membership_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.zip_entry.delete(0, tk.END)
        self.order_items.clear()
        self.order_table.delete('1.0', tk.END)
        self.map_label.config(text="")

    def update_map_link(self, event):
        address = self.address_entry.get().strip()
        zip_code = self.zip_entry.get().strip()

        if address and zip_code:
            self.map_label.config(text=f"View on map: https://www.google.com/maps/search/?api=1&query={address},+{zip_code}")
        else:
            self.map_label.config(text="")

    def open_google_maps(self):
        address = self.address_entry.get()
        zip_code = self.zip_entry.get()
        if address and zip_code:
            webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={address},+{zip_code}")
        else:
            messagebox.showerror("Input Error", "Please enter both address and zip code to open Google Maps.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodOrderApp(root)
    root.mainloop()
