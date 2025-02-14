import tkinter as tk
from tkinter import messagebox

class FlightBookingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Ticket Booking System")

        self.root.geometry("600x400")  # Set the initial size of the window

        self.style = tk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", background="#4caf50", foreground="white", font=("Arial", 12))
        self.style.configure("TText", background="#e0e0e0", font=("Arial", 12))

        self.frame = tk.Frame(root, style="TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.available_seats_label = tk.Label(self.frame, text="Available Seats:", style="TLabel")
        self.available_seats_label.pack()

        self.available_seats_text = tk.Text(self.frame, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED, style="TText")
        self.available_seats_text.pack()

        self.destinations_label = tk.Label(self.frame, text="Available Destinations:", style="TLabel")
        self.destinations_label.pack()

        self.destinations_text = tk.Text(self.frame, height=5, width=50, wrap=tk.WORD, state=tk.DISABLED, style="TText")
        self.destinations_text.pack()

        self.payment_methods_label = tk.Label(self.frame, text="Available Payment Methods:", style="TLabel")
        self.payment_methods_label.pack()

        self.payment_methods_text = tk.Text(self.frame, height=2, width=50, wrap=tk.WORD, state=tk.DISABLED, style="TText")
        self.payment_methods_text.pack()

        self.choice_label = tk.Label(self.frame, text="Enter your choice:", style="TLabel")
        self.choice_label.pack()

        self.choice_entry = tk.Entry(self.frame, style="TLabel")
        self.choice_entry.pack()

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.handle_choice, style="TButton")
        self.submit_button.pack()

        self.output_text = tk.Text(self.frame, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED, style="TText")
        self.output_text.pack()

        # Initialize the GUI with available information
        self.update_available_seats()
        self.update_destinations()
        self.update_payment_methods()

    def update_available_seats(self):
        seats_text = ""
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
        choice = self.choice_entry.get()

        if choice == '1':
            self.update_available_seats()
        elif choice == '2':
            self.update_destinations()
        elif choice == '3':
            self.update_payment_methods()
        elif choice == '4':
            self.book_ticket()
        elif choice == '5':
            self.cancel_ticket()
        elif choice == '6':
            self.root.destroy()
        else:
            messagebox.showinfo("Invalid Choice", "Please enter a valid choice.")

    def book_ticket(self):
        class_name = input("Enter class (Economy/Business/First Class): ")
        num_tickets = int(input("Enter the number of tickets to book: "))
        destination = input("Enter destination (NYC/LAX/ORD/MIA): ")
        payment_method = input("Enter payment method: ")

        if num_tickets <= available_seats[class_name]:
            available_seats[class_name] -= num_tickets
            booked_seats[class_name] += num_tickets
            total_price = prices[class_name] * num_tickets
            output = f"Booking successful! {num_tickets} {class_name} ticket(s) to {destination}. Total Price: ${total_price}\n"
            output += f"Payment successful using {payment_method}."
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)
            self.output_text.config(state=tk.DISABLED)
        else:
            output = f"Sorry, there are not enough available {class_name} seats."
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)
            self.output_text.config(state=tk.DISABLED)

    def cancel_ticket(self):
        class_name = input("Enter class (Economy/Business/First Class): ")
        num_tickets = int(input("Enter the number of tickets to cancel: "))
        destination = input("Enter destination (NYC/LAX/ORD/MIA): ")
        payment_method = input("Enter payment method for refund: ")

        if num_tickets <= booked_seats[class_name]:
            available_seats[class_name] += num_tickets
            booked_seats[class_name] -= num_tickets
            total_refund = prices[class_name] * num_tickets
            output = f"Cancellation successful! {num_tickets} {class_name} ticket(s) to {destination} cancelled. Total Refund: ${total_refund}\n"
            output += f"Refund processed to your {payment_method}."
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)
            self.output_text.config(state=tk.DISABLED)
        else:
            output = "Invalid number of tickets to cancel."
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)
            self.output_text.config(state=tk.DISABLED)

# Define the initial values for the FlightTicketBookingSystem
available_seats = {'E': 50, 'B': 20, 'FC': 10}
prices = {'E': 300, 'B': 600, 'FC': 1000}
booked_seats = {'E': 0, 'B': 0, 'FC': 0}
destinations = {'New York': 'NYC', 'Los Angeles': 'LAX', 'Chicago': 'ORD', 'Miami': 'MIA'}
payment_methods = ['CC', 'DC', 'PP']

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingGUI(root)
    root.mainloop()
