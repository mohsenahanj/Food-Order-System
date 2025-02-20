# Food Order System

![Screenshot 2025-02-21 024217](https://github.com/user-attachments/assets/2a64ec8f-739c-4470-a2ee-95ef75085a89)


## Description

**Food Order System** is a desktop application built using Python's Tkinter library that allows users to place food orders easily. The application provides a user-friendly interface for selecting food items, drinks, quantity, and payment methods. It also validates user inputs, generates an order summary, and saves the order details to a text file on the user's desktop. Additionally, it integrates with Google Maps for location-based services.

---

## Features

- **User-Friendly Interface:** A simple and intuitive GUI for placing food orders.
- **Order Management:** Users can add multiple food items and drinks to their order.
- **Input Validation:** Ensures all fields are filled out correctly (e.g., phone number format, quantity validation).
- **Order Summary:** Generates a detailed summary of the order, including membership code, customer details, and ordered items.
- **Text File Export:** Saves the order summary to a `.txt` file on the user's desktop.
- **Google Maps Integration:** Provides a link to view the delivery address on Google Maps.
- **Cross-Platform Compatibility:** Works on Windows, macOS, and Linux.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/food-order-system.git
   cd food-order-system

---

## Usage

- **After running the application, the main window will appear.
- **Fill in the required fields:
- **Membership Code: Enter your membership code (optional).
- **Customer Name: Enter your full name.
- **Phone Number: Enter an 11-digit phone number.
- **Address: Enter your delivery address.
- **Zip Code: Enter your postal/zip code.
- **Select food items and drinks from the dropdown menus.
- **Add a description for the food item if needed.
- **Enter the quantity of each item.
- **Click the "Add Order Item" button to add items to your order.
- **Once you've added all desired items, click the "Submit Order" button.
- **The application will validate your inputs, save the order details to a .txt file on your desktop, and display a success message.
- **You can also click the "Select Location on Map" button to open the delivery address in Google Maps.

---

## Folder Structure

 ```bash
/food-order-system
    food_order_app.py
    /assets
        screenshot.png
        example_output.png
    README.md
```

food_order_app.py: The main application code.
/assets: Directory for storing static assets like screenshots.
README.md: This file!

---

## Input Validation
The application performs the following validations:

- **Phone Number: Must be exactly 11 digits.
- **Quantity: Must be a positive integer.
- **Required Fields: All fields (name, phone, address, zip code) must be filled out before submitting the order.
- **At Least One Order Item: Users must add at least one item to their order before submission.
---

### Saving Orders

When the user submits an order, the application saves the order details to a .txt file on the user's desktop. The file includes the following information:

- **Membership Code
- **Customer Name
- **Phone Number
- **Address
- **Zip Code
- **Order Time
- **Ordered Items (with descriptions and quantities)

Example of the saved .txt file:
 ```bash
Order Summary
Membership Code: 123456
Name: John Doe
Phone: 12345678901
Address: 123 Main Street
Zip Code: 10001
Order Time: 2023-03-15 14:30
Order Items:
Pizza (Pepperoni) + Coke x2
Burger (Cheeseburger) + Water x1
```
---
## Contact
If you have any questions or feedback, feel free to reach out:

Email: ahanjm@gmail.com
GitHub: @mohsenahanj

