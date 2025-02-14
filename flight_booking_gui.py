import tkinter as tk
from tkinter import messagebox

class FlightBookingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Ticket Booking System")

        self.available_seats_label = tk.Label(root, text="Available Seats:")
        self.available_seats_label.pack()

        self.available_seats_text = tk.Text(root, height=10, width=50)
        self.available_seats_text.pack()

        self.destinations_label = tk.Label(root, text="Available Destinations:")
        self.destinations_label.pack()

        self.destinations_text = tk.Text(root, height=5, width=50)
        self.destinations_text.pack()

        self.payment_methods_label = tk.Label(root, text="Available Payment Methods:")
        self.payment_methods_label.pack()

        self.payment_methods_text = tk.Text(root, height=2, width=50)
        self.payment_methods_text.pack()

        self.choice_label = tk.Label(root, text="Enter your choice:")
        self.choice_label.pack()

        self.choice_entry = tk.Entry(root)
        self.choice_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.handle_choice)
        self.submit_button.pack()

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack()

    def update_available_seats(self):
        seats_text = ""
        for class_name, seats in available_seats.items():
            seats_text += f"{class_name}: {seats} seats\n"
        self.available_seats_text.delete(1.0, tk.END)
        self.available_seats_text.insert(tk.END, seats_text)

    def update_destinations(self):
        destinations_text = ""
        for city, code in destinations.items():
            destinations_text += f"{city} ({code})\n"
        self.destinations_text.delete(1.0, tk.END)
        self.destinations_text.insert(tk.END, destinations_text)

    def update_payment_methods(self):
        methods_text = "\n".join(payment_methods)
        self.payment_methods_text.delete(1.0, tk.END)
        self.payment_methods_text.insert(tk.END, methods_text)

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
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)
        else:
            output = f"Sorry, there are not enough available {class_name} seats."
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)

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
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)
        else:
            output = "Invalid number of tickets to cancel."
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output)

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
