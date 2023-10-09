# Split Bill Application

This application helps to split bills between multiple people. It allows adding people and items under each person to calculate the total amount each person owes.

## Key Features

- Add multiple people who participated in the bill splitting
- Add items under each person with name, price and quantity 
- Calculate total price of items for each person
- Calculate overall total bill amount
- View amount each person needs to pay
- Update/edit existing people and item details
- Delete people and their items

## Getting Started

To use this application, follow the steps:

1. Clone the repository

```git clone https://github.com/Siddhu2502/cash-splitter```

2. Install dependencies

well there is none python ships with tkinter default !!


3. Start the development server

```python biller.py```
or 
```python3 biller.py```

# Run this application as a stand alone app
``` pip install pyinstaller ```

Run this command to create a single executable file it will be inside the dist folder
rest all folder is not that importatnt you can delete them if you want it will not affect the app

```pyinstaller --onefile biller.py ```

## Data Model

The key entities in this application are:

### Person

A person represents someone who is part of the bill split. Each person has the following properties:

- name (string) - Name of the person

### Item 

An item represents a product/service whose cost is being split. Each item is associated with a person and has:

- name (string) - Name of the item  
- price (number) - Price of the item
- quantity (number) - Quantity purchased of the item

### Total

The totals calculated are:

- Person total - Total price of all items associated with a person 
- Overall total - Sum of all item prices

## Usage

### Add Person

Users can add a new person by clicking the "Add Person" button. They need to enter the person's name.

### Add Item 

Under each person, users can add a new item by clicking "Add Item". They need to enter the item name, price and quantity.

### View Totals

The amounts owed by each person and overall total will automatically update as items are added or updated.

### Edit/Delete

Users can edit existing people and item details as needed. They also have an option to delete people along with their associated items.