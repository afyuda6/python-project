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


def calculate_discount():
    price_text = price_entry.get()
    discount_text = discount_entry.get()

    if not price_text and not discount_text:
        messagebox.showerror("Input Error", "Please fill in both original price and discount.")
        return

    if not price_text:
        messagebox.showerror("Input Error", "Please fill the original price.")
        return

    if not discount_text:
        messagebox.showerror("Input Error", "Please fill the discount.")
        return

    try:
        original_price = float(price_entry.get())
        discount = float(discount_entry.get())

        if original_price < 0:
            messagebox.showerror("Value Error", "Original price cannot be negative.")
            return
        if discount < 0:
            messagebox.showerror("Value Error", "Discount cannot be negative.")
            return
        if discount > 100:
            messagebox.showerror("Value Error", "Discount cannot be more than 100%.")
            return

        discount_amount = original_price * (discount / 100)
        final_price = original_price - discount_amount

        final_label.config(text=f"Final Price: Rp{final_price:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter numbers only.")


calculate_button = tk.Button(window, text="Calculate", command=calculate_discount)
calculate_button.pack(pady=15)

final_label = tk.Label(window, text="Final Price: Rp0.00")
final_label.pack()

window.mainloop()
