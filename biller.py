import tkinter as tk

# Initialize the main data dictionary
data = {}

# Function to add a new person
def add_person():
    name = name_entry.get()
    if name:
        data[name] = {'items': []}
        update_display()
        name_entry.delete(0, tk.END)

# Function to add a new item for a person
def add_item(person, item_name, price, quantity):
    try:
        price = int(price)
        quantity = int(quantity)
        total = price * quantity
        data[person]['items'].append((item_name, price, quantity, total))
        update_display()
    except ValueError:
        # Handle invalid input
        pass

# Function to update the display
def update_display():
    for person_frame in main_frame.winfo_children():
        person_frame.destroy()

    for person, person_data in data.items():
        person_frame = tk.Frame(main_frame, bd=2, relief=tk.RAISED)
        person_frame.pack(pady=5, padx=10, fill=tk.BOTH)

        person_label = tk.Label(person_frame, text=person)
        person_label.pack(side=tk.LEFT, padx=10)

        total = sum(item[3] for item in person_data['items'])
        total_label = tk.Label(person_frame, text=f"Total: Rs-{total}")
        total_label.pack(side=tk.RIGHT, padx=10)

        item_frame = tk.Frame(person_frame)
        item_frame.pack()

        for i, (item_name, price, quantity, total) in enumerate(person_data['items']):
            tk.Label(item_frame, text=item_name).grid(row=i, column=0)
            tk.Label(item_frame, text=price).grid(row=i, column=1)
            tk.Label(item_frame, text=quantity).grid(row=i, column=2)
            tk.Label(item_frame, text=f"Total: Rs-{total}").grid(row=i, column=3)

        delete_person_button = tk.Button(person_frame, text="Delete Person", command=lambda p=person: delete_person(p))
        delete_person_button.pack(side=tk.BOTTOM, padx=10, pady=5)

# Function to delete a person and their data
def delete_person(person):
    del data[person]
    update_display()

# Main window
root = tk.Tk()
root.title("Expense Tracker")

# Main frame
main_frame = tk.Frame(root)
main_frame.pack()

# Heading
heading_label = tk.Label(main_frame, text="Expense Tracker", font=("Helvetica", 16))
heading_label.pack(pady=10)

# Frame for adding people
add_person_frame = tk.Frame(main_frame, bd=2, relief=tk.RAISED)
add_person_frame.pack(pady=10, padx=10)

name_label = tk.Label(add_person_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5)
name_entry = tk.Entry(add_person_frame)
name_entry.grid(row=0, column=1, padx=5)
add_button = tk.Button(add_person_frame, text="Add Person", command=add_person)
add_button.grid(row=0, column=2, padx=5)

# Input fields for adding items
item_name_entry = tk.Entry(add_person_frame)
price_entry = tk.Entry(add_person_frame)
quantity_entry = tk.Entry(add_person_frame)
add_item_button = tk.Button(add_person_frame, text="Add Item", command=lambda: add_item(name_entry.get(), item_name_entry.get(), price_entry.get(), quantity_entry.get()))
item_name_entry.grid(row=1, column=0, padx=5)
price_entry.grid(row=1, column=1, padx=5)
quantity_entry.grid(row=1, column=2, padx=5)
add_item_button.grid(row=1, column=3, padx=5)

# Start the main loop
root.mainloop()
