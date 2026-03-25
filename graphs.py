import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from analytics import *
from inventory import *
from sales import *


# 1
def brand_vs_items():
    df_items = read_file("data/items.csv")

    filtered = df_items.groupby("brand")["stock"].count().reset_index()

    plt.figure(figsize=(8, 6))
    plt.bar(filtered["brand"], filtered["stock"])

    plt.title("Items for brand", fontsize=20)
    plt.xlabel("Brand", fontsize=15)
    plt.ylabel("Items", fontsize=15)

    plt.tight_layout()
    plt.savefig("graphs/graph1.png")
    plt.show()


# 2
def brand_vs_stock():
    df_items = read_file("data/items.csv")

    filtered = df_items.groupby("brand")["stock"].sum().reset_index()

    plt.figure(figsize=(8, 6))
    plt.bar(filtered["brand"], filtered["stock"])

    plt.title("Stock for brand", fontsize=20)
    plt.xlabel("Brand", fontsize=15)
    plt.ylabel("Items", fontsize=15)

    plt.tight_layout()
    plt.savefig("graphs/graph2.png")
    plt.show()


# 3
def brand_vs_items_sold():
    df_sales = read_file("data/sales.csv")
    df_items = read_file("data/items.csv")

    filtered = df_sales.groupby("item_id")["quantity"].sum().reset_index()

    merged = df_items.merge(filtered, on="item_id")
    merged = merged.sort_values(by="quantity", ascending=False)

    filtered_2 = (
        merged.groupby("brand")["quantity"]
        .sum()
        .reset_index()
        .sort_values(by="quantity", ascending=False)
    )

    plt.figure(figsize=(8, 6))
    plt.bar(filtered_2["brand"], filtered_2["quantity"])

    plt.title("Amount os sales", fontsize=20)
    plt.xlabel("Brand", fontsize=15)
    plt.ylabel("Items", fontsize=15)

    plt.tight_layout()
    plt.savefig("graphs/graph3.png")
    plt.show()


# 4
def brand_vs_revenue():
    df_sales = read_file("data/sales.csv")
    df_items = read_file("data/items.csv")

    filtered = df_sales.groupby("item_id")["amount"].sum().reset_index()

    merged = df_items.merge(filtered, on="item_id")
    merged = merged.sort_values(by="amount", ascending=False)

    filtered_2 = (
        merged.groupby("brand")["amount"]
        .sum()
        .reset_index()
        .sort_values(by="amount", ascending=False)
    )

    plt.figure(figsize=(8, 6))
    plt.bar(filtered_2["brand"], filtered_2["amount"])

    plt.title("Revenue made per brand", fontsize=20)
    plt.xlabel("Brand", fontsize=15)
    plt.ylabel("Revenue")

    plt.ticklabel_format(style="plain", axis="y")

    plt.tight_layout()
    plt.savefig("graphs/graph4.png")
    plt.show()


# 5
def items_vs_category():
    df_items = read_file("data/items.csv")

    filtered = df_items.groupby("category")["stock"].count().reset_index()

    plt.figure(figsize=(8, 6))
    plt.bar(filtered["category"], filtered["stock"])

    plt.title("Items in category", fontsize=20)
    plt.xlabel("Category", fontsize=15)
    plt.ylabel("Items", fontsize=15)

    plt.tight_layout()
    plt.savefig("graphs/graph5.png")
    plt.show()


# 6
def stock_vs_category():
    df_items = read_file("data/items.csv")

    filtered = df_items.groupby("category")["stock"].sum().reset_index()

    plt.figure(figsize=(8, 6))
    plt.bar(filtered["category"], filtered["stock"])

    plt.title("Stock in category", fontsize=20)
    plt.xlabel("Category", fontsize=15)
    plt.ylabel("Stock", fontsize=15)

    # plt.ticklabel_format(style='plain', axis='y')

    plt.tight_layout()
    plt.savefig("graphs/graph6.png")
    plt.show()


# 7
def sales_per_month():

    df_sales = read_file("data/sales.csv")

    df_sales["date"] = pd.to_datetime(df_sales["date"])

    df_sales["month"] = df_sales["date"].dt.month_name()
    df_sales["monthNum"] = df_sales["date"].dt.month

    data = (
        df_sales.groupby(["monthNum", "month"])["quantity"]
        .sum()
        .reset_index()
        .sort_values("monthNum")
    )

    plt.figure(figsize=(8, 6))
    plt.grid(axis="both", linewidth=0.2, color="gray", linestyle="-")

    plt.plot(data["month"], data["quantity"], marker=".")

    plt.title("Sales per Month", fontsize=18)
    plt.xlabel("Month")
    plt.ylabel("Quantity Sold")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("graphs/graph7.png")
    plt.show()


# 8
def revenue_per_month():

    df_sales = read_file("data/sales.csv")

    df_sales["date"] = pd.to_datetime(df_sales["date"])

    df_sales["month"] = df_sales["date"].dt.month_name()
    df_sales["monthNum"] = df_sales["date"].dt.month

    data = (
        df_sales.groupby(["monthNum", "month"])["amount"]
        .sum()
        .reset_index()
        .sort_values("monthNum")
    )

    plt.figure(figsize=(8, 6))
    plt.grid(axis="both", linewidth=0.2, color="gray", linestyle="-")

    plt.plot(data["month"], data["amount"], marker=".")

    plt.title("Revenue per Month", fontsize=18)
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)
    plt.ticklabel_format(style="plain", axis="y")
    plt.tight_layout()

    plt.savefig("graphs/graph8.png")
    plt.show()


# 9
def mega_graph():
    df_items = read_file("data/items.csv")
    df_sales = read_file("data/sales.csv")

    filtered_1 = (
        df_sales.groupby("item_id")
        .agg({"quantity": "sum", "amount": "sum"})
        .reset_index()
    )

    merged = df_items.merge(filtered_1, on="item_id", how="left")
    merged = merged.fillna(0)
    merged.drop(columns=["product_name", "item_id"], inplace=True)

    filtered_0 = (
        df_sales.groupby("item_id")
        .agg({"quantity": "sum", "amount": "sum"})
        .reset_index()
    )

    merged = df_items.merge(filtered_0, on="item_id", how="left")
    merged = merged.fillna(0)
    merged.drop(columns=["product_name", "item_id"], inplace=True)
    merged["stock_value"] = merged["price"] * merged["stock"]

    all_categories = merged["category"].drop_duplicates()
    categories = all_categories.to_list()

    all_brands = merged["brand"].drop_duplicates()
    brands = all_brands.to_list()

    print(
        """Availabe Options: 
        1. Search By Brand
        2. Search By Category"""
    )

    opt_choice = int(input("Pick an Option: "))

    base = merged.copy()

    if opt_choice == 1:
        print("\nAVAILABLE BRANDS")
        for i, brand in enumerate(brands, start=1):
            print(f"{i}. {brand}")

        brand_input = int(input("Select a brand: "))
        if brand_input < 1 or brand_input > len(brands):
            print("Invalid choice")
            exit()
        brand_selected = brands[brand_input - 1]

        a = brand_selected

    elif opt_choice == 2:
        print("\nAVAILABLE CATEGORIES")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        category_input = int(input("Select a category: "))
        if category_input < 1 or category_input > len(brands):
            print("Invalid choice")
            exit()
        category_selected = categories[category_input - 1]
        a = category_selected

    if opt_choice == 1:
        base = base[base["brand"] == brand_selected]

    if opt_choice == 2:
        base = base[base["category"] == category_selected]

    print(
        """\nAVAILABLE ANALYTICS
    1. Stock
    2. Items
    3. Stock Amount
    4. Sales
    5. Revenue"""
    )

    choice = int(input("Pick an analytic: "))
    analyticals = {1: "stock", 2: "items", 3: "stock amount", 4: "sales", 5: "revenue"}
    picked = analyticals[choice]

    column_map = {
        1: ("stock", "sum"),
        2: ("stock", "count"),
        3: ("stock_value", "sum"),
        4: ("quantity", "sum"),
        5: ("amount", "sum"),
    }

    col, func = column_map[choice]

    if opt_choice == 1:
        if func == "sum":
            req = base.groupby("category")[col].sum().reset_index()

        else:
            req = base.groupby("category")[col].count().reset_index()

        req[col] = req[col].astype(int)
        req = req.sort_values(by=col, ascending=False)

    elif opt_choice == 2:
        if func == "sum":
            req = base.groupby("brand")[col].sum().reset_index()

        else:
            req = base.groupby("brand")[col].count().reset_index()

        req[col] = req[col].astype(int)
        req = req.sort_values(by=col, ascending=False)

    x = req.iloc[:, 0]
    y = req[col]

    plt.figure()
    plt.bar(x, y)

    plt.xlabel(req.columns[0].capitalize())
    plt.ylabel(picked.capitalize())
    plt.title(
        f"{picked.capitalize()} by {req.columns[0].capitalize()} for {a.capitalize()}"
    )

    plt.xticks(rotation=45)

    for i, v in enumerate(req[col]):
        plt.text(i, v, str(v), ha="center", va="bottom")

    plt.tight_layout()
    plt.show()


# 10
def mega_month_graph():
    df_items = read_file("data/items.csv")
    df_sales = read_file("data/sales.csv")

    merged = df_sales.merge(df_items, on="item_id", how="left")
    merged = merged.drop(
        columns=[
            "sale_id",
            "product_name_x",
            "product_name_y",
            "item_id",
            "price_y",
            "stock",
            "price_x",
        ]
    )

    # print(merged.to_string())

    new_df = merged
    new_df["date"] = pd.to_datetime(new_df["date"])

    new_df["month"] = new_df["date"].dt.month_name()
    new_df["monthnum"] = new_df["date"].dt.month

    # print(new_df.to_string())
    merged = (
        new_df.groupby(["brand", "category", "month", "monthnum"])
        .agg({"quantity": "sum", "amount": "sum"})
        .reset_index()
    )

    merged = merged.sort_values(by="monthnum").reset_index(drop=True)
    # print(merged.to_string())

    all_categories = merged["category"].drop_duplicates()
    categories = all_categories.to_list()

    all_brands = merged["brand"].drop_duplicates()
    brands = all_brands.to_list()

    print(
        """Availabe Options: 
        1. Search By Brand
        2. Search By Category"""
    )

    opt_choice = int(input("Pick an Option: "))

    base = merged.copy()

    if opt_choice == 1:
        print("\nAVAILABLE BRANDS")
        for i, brand in enumerate(brands, start=1):
            print(f"{i}. {brand}")

        brand_input = int(input("Select a brand: "))
        if brand_input < 1 or brand_input > len(brands):
            print("Invalid choice")
            exit()
        brand_selected = brands[brand_input - 1]

        a = brand_selected

    elif opt_choice == 2:
        print("\nAVAILABLE CATEGORIES")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        category_input = int(input("Select a category: "))
        if category_input < 1 or category_input > len(categories):
            print("Invalid choice")
            exit()
        category_selected = categories[category_input - 1]
        a = category_selected

    if opt_choice == 1:
        base = base[base["brand"] == brand_selected]

    if opt_choice == 2:
        base = base[base["category"] == category_selected]

    print(
        """\nAVAILABLE ANALYTICS
    1. Sales
    2. Revenue"""
    )

    choice = int(input("Pick an analytic: "))
    analyticals = {1: "sales", 2: "revenue"}
    picked = analyticals[choice]

    column_map = {1: ("quantity"), 2: ("amount")}

    col = column_map[choice]

    req = base.groupby(["month", "monthnum"])[col].sum().reset_index()
    req = req.sort_values(by="monthnum")

    plt.plot(req["month"], req[col])
    plt.title(f"Month wise {picked} for {a}")
    plt.xlabel("Month")
    plt.ylabel(f"{col.capitalize()}")

    for i, v in enumerate(req[col]):
        plt.text(i, v, str(v), ha="center", va="bottom")

    plt.tight_layout()
    plt.show()
