from datetime import date
import os
from tabulate import tabulate
from inventory import *
from data_handler import *


def add_sales():
    df = read_file("data/items.csv")
    print("""\n\t\tAdd Sales:-""")

    file_exists = os.path.exists("data/sales.csv")

    if file_exists:
        old_sales = pd.read_csv("data/sales.csv")
        if not old_sales.empty:
            sale_id = old_sales["sale_id"].max() + 1
        else:
            sale_id = 1001
    else:
        sale_id = 1001

    try:
        item_id = int(input("Enter item id: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("\nInvalid Input...")
        exit()

    date_ = date.today()

    filtered = df.loc[df["item_id"] == item_id]

    if filtered.empty:
        print("Item not found")
        exit()

    product_name = filtered["product_name"].iloc[0]
    price = filtered["price"].iloc[0]
    stock = filtered["stock"].iloc[0]

    if quantity > stock:
        print("\nOut of stock...")
        exit()

    amount = quantity * price

    sales = {
        "sale_id": sale_id,
        "date": date_,
        "item_id": item_id,
        "product_name": product_name,
        "quantity": quantity,
        "price": price,
        "amount": amount,
    }

    sales_df = pd.DataFrame([sales])
    sales_df.to_csv("data/sales.csv", mode="a", header=not file_exists, index=False)

    df.loc[df["item_id"] == item_id, "stock"] -= quantity
    df.to_csv("data/items.csv", index=False)

    print("\nSale Added Successfully....")

    choice = input("Do you want a recipt?(y,n): ")

    if choice.strip() == "y":
        print("/n===========INVOICE===========")
        print(f"Sale ID        : {sale_id}")
        print(f"Date           : {date_}")
        print(f"Item ID        : {item_id}")
        print(f"Item Name      : {item_id}")
        print(f"Quantity       : {quantity}")
        print(f"Price          : {price}")
        print(f"-------------------------------")
        print(f"Total amount   : {amount}")
        print("===============================\n")
    else:
        print("\nGoodbye...")
        exit()


def show_sales():
    df = read_file("data/sales.csv")
    tab = tabulate(
        df, headers=list(df.columns), tablefmt="fancy_grid", showindex=False
    )    
    print(tab)