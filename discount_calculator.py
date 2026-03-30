import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Discount Calculator")
window.geometry("420x360")
window.resizable(False, False)

price_label = tk.Label(window, text="Original Price:")
price_label.pack()

price_entry = tk.Entry(window, width=20)
price_entry.pack()

discount_label = tk.Label(window, text="Discount (%):")
discount_label.pack()

discount_entry = tk.Entry(window, width=20)
discount_entry.pack()

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()

quantity_entry = tk.Entry(window, width=20)
quantity_entry.pack()


def calculate_discount():
    price_text = price_entry.get()
    discount_text = discount_entry.get()
    quantity_text = quantity_entry.get()

    if not price_text or not discount_text or not quantity_text:
        messagebox.showerror("Input Error", "Please fill all the input.")
        return

    try:
        original_price = float(price_text)
        discount = float(discount_text)
    except ValueError:
        messagebox.showerror("Input Error", "Price and discount must be numbers.")
        return

    try:
        quantity = int(quantity_text)
    except ValueError:
        messagebox.showerror("Input Error", "Quantity must be a whole number.")
        return

    if original_price < 0:
        messagebox.showerror("Value Error", "Original price cannot be negative.")
        return
    if discount < 0:
        messagebox.showerror("Value Error", "Discount cannot be negative.")
        return
    if discount > 100:
        messagebox.showerror("Value Error", "Discount cannot be more than 100%.")
        return
    if quantity <= 0:
        messagebox.showerror("Value Error", "Quantity must be more than 0.")
        return

    discount_amount = original_price * quantity * (discount / 100)
    final_price = original_price * quantity - discount_amount

    final_label.config(text=f"Final Price: Rp{final_price:,.2f}")


calculate_button = tk.Button(window, text="Calculate", command=calculate_discount)
calculate_button.pack(pady=15)

final_label = tk.Label(window, text="Final Price: Rp0.00")
final_label.pack()

window.mainloop()
