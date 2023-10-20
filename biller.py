import tkinter as tk
import json

# Function to calculate the total for an item
def calculate_item_total(price, quantity):
    return price * quantity
    
# Function to save the list of items
def save_data(data):
    """
    Save the expense data to a JSON file.

    Parameters:
    data (list): List of dictionaries containing the expense data.

    Returns:
    None
    """
    with open('expense_data.json', 'w') as f:
        json.dump(data, f)

# Function to load the save file
def load_data():
    """
    Load expense data from the JSON file.

    Returns:
    list: List of dictionaries containing the loaded expense data. If the file doesn't exist, returns an empty list.
    """
    try:
        with open('expense_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Function to add a new person
def add_person():
    name = name_entry.get()
    person_frame = tk.Frame(main_frame, bd=2, relief=tk.RAISED)
    person_frame.pack(pady=5, padx=10, fill=tk.BOTH)
    
    person_label = tk.Label(person_frame, text=name)
    person_label.pack(side=tk.LEFT, padx=10)
    
    total_label = tk.Label(person_frame, text="Total: 0/-")
    total_label.pack(side=tk.RIGHT, padx=10)
    
    name_entry.delete(0, tk.END)
    items = load_data()
    
    def add_item():
        item_name = item_entry.get()
        try:
           price = float(price_entry.get())
           quantity = float(quantity_entry.get())
        except:
           price = 0.0
           quantity = 0.0
        total = calculate_item_total(price, quantity)
        items.append((item_name, price, quantity, total))
        update_items()
        item_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
    
    def delete_person():
        person_frame.destroy()
    
    def delete_item(item_index):
        del items[item_index]
        update_items()
    
    def update_items():
        total = sum(item[3] for item in items)
        total_label.config(text=f"Total: {total}/-")
        
        for widget in item_frame.winfo_children():
            widget.grid_forget()
            
        tk.Label(item_frame, text="Item").grid(row=0, column=0)
        tk.Label(item_frame, text="Price").grid(row=0, column=1)
        tk.Label(item_frame, text="Quantity").grid(row=0, column=2)
        
        for i, (item_name, price, quantity, total) in enumerate(items):
            row_i = i + 1
            tk.Label(item_frame, text=item_name).grid(row=row_i, column=0)
            tk.Label(item_frame, text=price).grid(row=row_i, column=1)
            tk.Label(item_frame, text=quantity).grid(row=row_i, column=2)
            tk.Label(item_frame, text=f"Total: {total}").grid(row=row_i, column=3)
            tk.Button(item_frame, text="Delete", command=lambda i=i: delete_item(i)).grid(row=row_i, column=4)
        
        s_row = len(items) + 1
        item_entry.grid(row=s_row, column=0)
        price_entry.grid(row=s_row, column=1)
        quantity_entry.grid(row=s_row, column=2)
        add_item_button.grid(row=s_row + 1, columnspan=3)      
        save_data(items)
          
    
    item_frame = tk.Frame(person_frame)
    item_frame.pack()
    
    item_entry = tk.Entry(item_frame)
    price_entry = tk.Entry(item_frame)
    quantity_entry = tk.Entry(item_frame)
    add_item_button = tk.Button(item_frame, text="Add Item", command=add_item)
    update_items()
    
    delete_person_button = tk.Button(person_frame, text="Delete Person", command=delete_person)
    delete_person_button.pack(side=tk.BOTTOM, padx=10, pady=5)

# main window
root = tk.Tk()
root.title("Expense Tracker")

# main frame
main_frame = tk.Frame(root)
main_frame.pack()

# heading
heading_label = tk.Label(main_frame, text="Expense Tracker", font=("Helvetica", 16))
heading_label.pack(pady=10)

# frame for adding people
add_person_frame = tk.Frame(main_frame, bd=2, relief=tk.RAISED)
add_person_frame.pack(pady=10, padx=10)

name_label = tk.Label(add_person_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5)
name_entry = tk.Entry(add_person_frame)
name_entry.grid(row=0, column=1, padx=5)
add_button = tk.Button(add_person_frame, text="Add Person", command=add_person)
add_button.grid(row=0, column=2, padx=5)

# Start the main loop
root.mainloop()