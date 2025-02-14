import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class FlightBookingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Ticket Booking System")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButtonBlack.TButton", foreground="black", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TText", background="#e0e0e0", font=("Arial", 12))
        self.style.configure("TEntry.TEntry", fieldbackground="black", foreground="white", bordercolor="black", font=("Arial", 12))

        self.frame = ttk.Frame(root, style="TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.available_seats_label = ttk.Label(self.frame, text="Available Seats:", style="TLabel")
        self.available_seats_label.pack()

        self.available_seats_text = tk.Text(self.frame, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="#c2f0c2", font=("Arial", 12))
        self.available_seats_text.pack()

        self.destinations_label = ttk.Label(self.frame, text="Available Destinations:", style="TLabel")
        self.destinations_label.pack()

        self.destinations_text = tk.Text(self.frame, height=5, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="#c2f0c2", font=("Arial", 12))
        self.destinations_text.pack()

        self.payment_methods_label = ttk.Label(self.frame, text="Available Payment Methods:", style="TLabel")
        self.payment_methods_label.pack()

        self.payment_methods_text = tk.Text(self.frame, height=2, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="#c2f0c2", font=("Arial", 12))
        self.payment_methods_text.pack()

        self.choice_label = ttk.Label(self.frame, text="Enter your choice:", style="TLabel")
        self.choice_label.pack()

        self.choice_entry = ttk.Entry(self.frame, style="TEntry")
        self.choice_entry.pack()

        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.handle_choice, style="TButtonBlack.TButton")
        self.submit_button.pack()

        self.output_text = tk.Text(self.frame, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="#ffc2b3", font=("Arial", 12))
        self.output_text.pack()

        # Initialize the GUI with available information
        self.update_available_seats()
        self.update_destinations()
        self.update_payment_methods()

    def update_available_seats(self):
        seats_text = "Available Seats:\n"
        for class_name, seats in available_seats.items():
            seats_text += f"{class_name}: {seats} seats\n"
        self.available_seats_text.config(state=tk.NORMAL)
        self.available_seats_text.delete(1.0, tk.END)
        self.available_seats_text.insert(tk.END, seats_text)
        self.available_seats_text.config(state=tk.DISABLED)

    def update_destinations(self):
        destinations_text = ""
        for city, code in destinations.items():
            destinations_text += f"{city} ({code})\n"
        self.destinations_text.config(state=tk.NORMAL)
        self.destinations_text.delete(1.0, tk.END)
        self.destinations_text.insert(tk.END, destinations_text)
        self.destinations_text.config(state=tk.DISABLED)

    def update_payment_methods(self):
        methods_text = "\n".join(payment_methods)
        self.payment_methods_text.config(state=tk.NORMAL)
        self.payment_methods_text.delete(1.0, tk.END)
        self.payment_methods_text.insert(tk.END, methods_text)
        self.payment_methods_text.config(state=tk.DISABLED)

    def handle_choice(self):
        try:
            choice = int(self.choice_entry.get())
            if 1 <= choice <= 6:
                if choice == 4 or choice == 5:
                    self.execute_transaction(choice)
                else:
                    self.display_output("Invalid choice for direct execution.\n", "red")
            else:
                self.display_output("Invalid choice. Please try again.\n", "red")
        except ValueError:
            self.display_output("Invalid input. Please enter a valid number.\n", "red")

    def execute_transaction(self, choice):
        if choice == 4:
            self.book_ticket()
        elif choice == 5:
            self.cancel_ticket()

    def book_ticket(self):
        class_name = self.show_entry_dialog("Enter class (Economy/Business/First Class): ")
        num_tickets = int(self.show_entry_dialog("Enter the number of tickets to book: "))
        destination = self.show_entry_dialog("Enter destination (NYC/LAX/ORD/MIA): ")
        payment_method = self.show_entry_dialog("Enter payment method (CC/DC/PP): ")

        if payment_method == "CC" or payment_method == "DC":
            self.show_card_details_window(class_name, num_tickets, destination)
        elif payment_method == "PP":
            self.show_paypal_details_window(class_name, num_tickets, destination)
        else:
            self.display_output("Invalid payment method. Please choose CC, DC, or PP.\n", "red")

    def cancel_ticket(self):
        class_name = self.show_entry_dialog("Enter class (Economy/Business/First Class): ")
        num_tickets = int(self.show_entry_dialog("Enter the number of tickets to cancel: "))
        destination = self.show_entry_dialog("Enter destination (NYC/LAX/ORD/MIA): ")
        payment_method = self.show_entry_dialog("Enter payment method for refund (CC/DC/PP): ")

        if payment_method == "CC" or payment_method == "DC":
            self.show_card_details_window(class_name, num_tickets, destination, refund=True)
        elif payment_method == "PP":
            self.show_paypal_details_window(class_name, num_tickets, destination, refund=True)
        else:
            self.display_output("Invalid payment method. Please choose CC, DC, or PP.\n", "red")

    def show_entry_dialog(self, prompt):
        return simpledialog.askstring("Input", prompt, parent=self.root)

    def show_card_details_window(self, class_name, num_tickets, destination, refund=False):
        card_window = tk.Toplevel(self.root)
        card_window.title("Card Details")
        card_window.geometry("300x200")

        card_label = tk.Label(card_window, text="Card Number:", font=("Helvetica", 12))
        card_label.pack()
        card_entry = tk.Entry(card_window, font=("Helvetica", 12), show="*")
        card_entry.pack()

        expiry_label = tk.Label(card_window, text="Expiry Date (MM/YY):", font=("Helvetica", 12))
        expiry_label.pack()
        expiry_entry = tk.Entry(card_window, font=("Helvetica", 12))
        expiry_entry.pack()

        cvv_label = tk.Label(card_window, text="CVV:", font=("Helvetica", 12))
        cvv_label.pack()
        cvv_entry = tk.Entry(card_window, font=("Helvetica", 12), show="*")
        cvv_entry.pack()

        confirm_button = tk.Button(card_window, text="Confirm Payment", command=lambda: self.confirm_card_payment(card_window, class_name, num_tickets, destination, card_entry, expiry_entry, cvv_entry, refund))
        confirm_button.pack()

    def show_paypal_details_window(self, class_name, num_tickets, destination, refund=False):
        paypal_window = tk.Toplevel(self.root)
        paypal_window.title("PayPal Details")
        paypal_window.geometry("300x200")

        paypal_label = tk.Label(paypal_window, text="PayPal Email:", font=("Helvetica", 12))
        paypal_label.pack()
        paypal_entry = tk.Entry(paypal_window, font=("Helvetica", 12))
        paypal_entry.pack()

        confirm_button = tk.Button(paypal_window, text="Confirm Payment", command=lambda: self.confirm_paypal_payment(paypal_window, class_name, num_tickets, destination, paypal_entry, refund))
        confirm_button.pack()

    def confirm_card_payment(self, card_window, class_name, num_tickets, destination, card_entry, expiry_entry, cvv_entry, refund):
        card_number = card_entry.get()
        expiry_date = expiry_entry.get()
        cvv = cvv_entry.get()

        if card_number and expiry_date and cvv:
            card_window.destroy()
            if refund:
                self.complete_refund(class_name, num_tickets, destination)
            else:
                self.complete_purchase(class_name, num_tickets, destination)
        else:
            messagebox.showerror("Error", "Incomplete card details. Please fill all fields.")

    def confirm_paypal_payment(self, paypal_window, class_name, num_tickets, destination, paypal_entry, refund):
        paypal_email = paypal_entry.get()

        if paypal_email:
            paypal_window.destroy()
            if refund:
                self.complete_refund(class_name, num_tickets, destination)
            else:
                self.complete_purchase(class_name, num_tickets, destination)
        else:
            messagebox.showerror("Error", "Incomplete PayPal details. Please fill the email field.")

    def complete_purchase(self, class_name, num_tickets, destination):
        total_price = prices[class_name] * num_tickets
        output = f"Booking successful! {num_tickets} {class_name} ticket(s) to {destination}. Total Price: ${total_price}\n"
        output += f"Payment successful.\n"
        self.display_output(output, "green")

        # Update available seats after booking
        available_seats[class_name] -= num_tickets
        booked_seats[class_name] += num_tickets
        self.update_available_seats()

    def complete_refund(self, class_name, num_tickets, destination):
        total_refund = prices[class_name] * num_tickets
        output = f"Cancellation successful! {num_tickets} {class_name} ticket(s) to {destination} cancelled. Total Refund: ${total_refund}\n"
        output += f"Refund processed.\n"
        self.display_output(output, "green")

        # Update available seats after cancellation
        available_seats[class_name] += num_tickets
        booked_seats[class_name] -= num_tickets
        self.update_available_seats()

    def display_output(self, output, color):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, output, color)
        self.output_text.config(state=tk.DISABLED)

# Sample data
available_seats = {'E': 50, 'B': 20, 'FC': 10}
prices = {'E': 300, 'B': 600, 'FC': 1000}
booked_seats = {'E': 0, 'B': 0, 'FC': 0}
destinations = {'New York': 'NYC', 'Los Angeles': 'LAX', 'Chicago': 'ORD', 'Miami': 'MIA'}
payment_methods = ['CC', 'DC', 'PP']

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingGUI(root)
    root.mainloop()
