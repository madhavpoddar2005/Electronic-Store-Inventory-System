import pandas as pd
from tabulate import tabulate
from data_handler import *


# 1
def total_sales():
    df_sales = read_file("data/sales.csv")
    turn_over = df_sales["amount"].sum()
    return turn_over


# 2
def sales_profit():
    df_sales = read_file("data/sales.csv")
    filtered = df_sales["amount"].sum()
    profit = filtered * (15 / 100)
    return profit


# 3
def sales_entries():
    df_sales = read_file("data/sales.csv")
    count = df_sales["sale_id"].count()
    return count


# 4
def items_entries():
    df_items = read_file("data/items.csv")
    count = df_items["item_id"].count()
    return count


# 5
def get_stock():
    df_items = read_file("data/items.csv")

    tab = tabulate(
        df_items[["item_id", "product_name", "stock"]],
        headers="keys",
        tablefmt="grid",
        showindex=False,
    )
    return tab


# 6
def low_stock():
    df_items = read_file("data/items.csv")
    filtered = df_items.loc[df_items["stock"] < 5]

    tab = tabulate(
        filtered[["item_id", "product_name", "stock"]],
        headers="keys",
        tablefmt="grid",
        showindex=False,
    )
    return tab


# 7
def top_selling_item():
    df_sales = read_file("data/sales.csv")
    df_items = read_file("data/items.csv")

    filtered = df_sales.groupby("item_id")["quantity"].sum().reset_index()

    merged = df_items.merge(filtered, on="item_id")
    merged = merged.sort_values(by="quantity", ascending=False)

    tab = tabulate(
        merged[["item_id", "product_name", "quantity"]],
        headers="keys",
        tablefmt="grid",
        showindex=False,
    )

    return tab


# 8
def revenue_per_item():
    df_sales = read_file("data/sales.csv")
    df_items = read_file("data/items.csv")

    filtered = df_sales.groupby("item_id")["amount"].sum().reset_index()
    merged = df_items.merge(filtered, on="item_id")
    merged = merged.sort_values("amount", ascending=False)

    tab = tabulate(
        merged[["item_id", "product_name", "amount"]],
        headers="keys",
        tablefmt="grid",
        showindex=False,
    )

    return tab


# 9
def brand_stock():
    df_items = read_file("data/items.csv")
    filtered = df_items.groupby("brand")["stock"].sum().reset_index()

    tab = tabulate(
        filtered, headers=["Brand", "Available stock"], tablefmt="grid", showindex=False
    )
    return tab


# 10
def brand_items():
    df_items = read_file("data/items.csv")
    filtered = df_items.groupby("brand")["item_id"].count().reset_index()

    tab = tabulate(
        filtered, headers=["Brand", "Available items"], tablefmt="grid", showindex=False
    )
    return tab


# 11
def top_selling_brand():
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

    tab = tabulate(
        filtered_2[["brand", "quantity"]],
        headers="keys",
        tablefmt="grid",
        showindex=False,
    )
    return tab


# 12
def brand_revenue():
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

    tab = tabulate(
        filtered_2[["brand", "amount"]],
        headers="keys",
        tablefmt="grid",
        showindex=False,
    )
    return tab


# 13
def category_stock():
    df_items = read_file("data/items.csv")

    filtered = df_items.groupby("category")["stock"].sum().reset_index()

    tab = tabulate(
        filtered[["category", "stock"]],
        headers="keys",
        tablefmt="grid",
        showindex=False,
    )
    return tab


# 14
def category_items():
    df_items = read_file("data/items.csv")

    filtered = df_items.groupby("category")["stock"].count().reset_index()

    tab = tabulate(
        filtered[["category", "stock"]],
        headers=["category", "items"],
        tablefmt="grid",
        showindex=False,
    )
    return tab


# 15
def category_vs_brand_stock():
    df_items = read_file("data/items.csv")

    tab = df_items.pivot_table(
        index="category", columns="brand", values="stock", aggfunc="sum", fill_value=0
    )

    tab = tab.sort_values(by="category")
    tab["Total"] = tab.sum(axis=1)
    tab.loc["Total"] = tab.sum()

    table = tabulate(tab, headers="keys", tablefmt="psql")
    return table


# 16
def category_vs_brand_sales():
    df_items = read_file("data/items.csv")
    df_sales = read_file("data/sales.csv")

    filtered = df_sales.groupby("item_id")["quantity"].sum().reset_index()

    merged = df_items.merge(filtered, on="item_id")

    tab = merged.pivot_table(
        index="category",
        columns="brand",
        values="quantity",
        aggfunc="sum",
        fill_value=0,
    )

    tab = tab.sort_values(by="category")
    tab["Total"] = tab.sum(axis=1)
    tab.loc["Total"] = tab.sum()

    table = tabulate(tab, headers="keys", tablefmt="psql")
    return table


# 17
def category_vs_brand_revenue():
    df_items = read_file("data/items.csv")
    df_sales = read_file("data/sales.csv")

    filtered = df_sales.groupby("item_id")["amount"].sum().reset_index()

    merged = df_items.merge(filtered, on="item_id")

    tab = merged.pivot_table(
        index="category",
        columns="brand",
        values="amount",
        aggfunc="sum",
        fill_value=0,
    )

    tab = tab.sort_values(by="category")
    tab = tab.T
    tab["Total"] = tab.sum(axis=1)
    tab.loc["Total"] = tab.sum()

    table = tabulate(tab, headers="keys", tablefmt="grid")
    return table


# 18
def search_by_category():
    df_items = read_file("data/items.csv")
    df_sales = read_file("data/sales.csv")

    filtered_0 = (
        df_sales.groupby("item_id")
        .agg({"quantity": "sum", "amount": "sum"})
        .reset_index()
    )

    merged = df_items.merge(filtered_0, on="item_id", how="left")
    merged = merged.fillna(0)
    merged.drop(columns=["product_name", "item_id"], inplace=True)

    filtered_2 = merged["category"].drop_duplicates()
    categories = filtered_2.to_list()

    print("\nAVAILABLE CATEGORIES")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    category_input = int(input("Select a category: "))
    category_selected = categories[category_input - 1]

    all_brands = merged["brand"].drop_duplicates()

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

    merged["stock_value"] = merged["price"] * merged["stock"]
    grouped = merged.groupby(["brand", "category"])

    if choice == 1:
        filtered_3 = grouped["stock"].sum().reset_index()
        req = filtered_3.loc[filtered_3["category"] == category_selected]
        req = req.set_index("brand").reindex(all_brands, fill_value=0).reset_index()
        req = req.sort_values(by="stock", ascending=False)
        total_value = req["stock"].sum()

        total_row = {"brand": "TOTAL", "stock": total_value}

        req = pd.concat([req, pd.DataFrame([total_row])], ignore_index=True)

        tab = tabulate(
            req[["brand", "stock"]], headers="keys", tablefmt="psql", showindex=False
        )

    elif choice == 2:
        filtered_3 = grouped["stock"].count().reset_index()
        req = filtered_3.loc[filtered_3["category"] == category_selected]
        req = req.set_index("brand").reindex(all_brands, fill_value=0).reset_index()
        req = req.sort_values(by="stock", ascending=False)
        total_value = req["stock"].sum()

        total_row = {"brand": "TOTAL", "stock": total_value}

        req = pd.concat([req, pd.DataFrame([total_row])], ignore_index=True)

        tab = tabulate(
            req[["brand", "stock"]],
            headers=["brand", "items"],
            tablefmt="psql",
            showindex=False,
        )

    elif choice == 3:
        filtered_3 = grouped["stock_value"].sum().reset_index()
        req = filtered_3.loc[filtered_3["category"] == category_selected]
        req = req.set_index("brand").reindex(all_brands, fill_value=0).reset_index()
        req = req.sort_values(by="stock_value", ascending=False)
        total_value = req["stock_value"].sum()

        total_row = {"brand": "TOTAL", "stock_value": total_value}

        req = pd.concat([req, pd.DataFrame([total_row])], ignore_index=True)

        tab = tabulate(
            req[["brand", "stock_value"]],
            headers="keys",
            tablefmt="psql",
            showindex=False,
        )

    elif choice == 4:
        filtered_3 = grouped["quantity"].sum().reset_index()
        req = filtered_3.loc[filtered_3["category"] == category_selected]
        req = req.set_index("brand").reindex(all_brands, fill_value=0).reset_index()
        req = req.sort_values(by="quantity", ascending=False)
        total_value = req["quantity"].sum()

        total_row = {"brand": "TOTAL", "quantity": total_value}

        req = pd.concat([req, pd.DataFrame([total_row])], ignore_index=True)

        tab = tabulate(
            req[["brand", "quantity"]], headers="keys", tablefmt="psql", showindex=False
        )

    elif choice == 5:
        filtered_3 = grouped["amount"].sum().reset_index()
        req = filtered_3.loc[filtered_3["category"] == category_selected]
        req = req.set_index("brand").reindex(all_brands, fill_value=0).reset_index()
        req = req.sort_values(by="amount", ascending=False)
        req["amount"] = req["amount"].astype(int)
        total_value = req["amount"].sum()

        total_row = {"brand": "TOTAL", "amount": total_value}

        req = pd.concat([req, pd.DataFrame([total_row])], ignore_index=True)

        tab = tabulate(
            req[["brand", "amount"]], headers="keys", tablefmt="psql", showindex=False
        )

    print(f"\nBrand wise {picked} for {category_selected}")
    return tab


# 19
def search_by_brand():
    df_items = read_file("data/items.csv")
    df_sales = read_file("data/sales.csv")

    filtered_0 = (
        df_sales.groupby("item_id")
        .agg({"quantity": "sum", "amount": "sum"})
        .reset_index()
    )

    merged = df_items.merge(filtered_0, on="item_id", how="left")
    merged = merged.fillna(0)
    merged.drop(columns=["product_name", "item_id"], inplace=True)

    filtered_2 = merged["brand"].drop_duplicates()
    brands = filtered_2.to_list()

    print("\nAVAILABLE BRANDS")
    for i, brand in enumerate(brands, start=1):
        print(f"{i}. {brand}")

    brand_input = int(input("Select a brand: "))
    brand_selected = brands[brand_input - 1]

    all_categories = merged["category"].drop_duplicates()

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

    merged["stock_value"] = merged["price"] * merged["stock"]
    grouped = merged.groupby(["brand", "category"])

    if choice == 1:
        filtered_3 = grouped["stock"].sum().reset_index()
        req = filtered_3.loc[filtered_3["brand"] == brand_selected]
        req = (
            req.set_index("category")
            .reindex(all_categories, fill_value=0)
            .reset_index()
        )
        req = req.sort_values(by="stock", ascending=False)

        tab = tabulate(
            req[["category", "stock"]], headers="keys", tablefmt="psql", showindex=False
        )

    elif choice == 2:
        filtered_3 = grouped["stock"].count().reset_index()
        req = filtered_3.loc[filtered_3["brand"] == brand_selected]
        req = (
            req.set_index("category")
            .reindex(all_categories, fill_value=0)
            .reset_index()
        )
        req = req.sort_values(by="stock", ascending=False)

        tab = tabulate(
            req[["category", "stock"]],
            headers=["category", "items"],
            tablefmt="psql",
            showindex=False,
        )

    elif choice == 3:
        filtered_3 = grouped["stock_value"].sum().reset_index()
        req = filtered_3.loc[filtered_3["brand"] == brand_selected]
        req = (
            req.set_index("category")
            .reindex(all_categories, fill_value=0)
            .reset_index()
        )
        req = req.sort_values(by="stock_value", ascending=False)

        tab = tabulate(
            req[["category", "stock_value"]],
            headers="keys",
            tablefmt="psql",
            showindex=False,
        )

    elif choice == 4:
        filtered_3 = grouped["quantity"].sum().reset_index()
        req = filtered_3.loc[filtered_3["brand"] == brand_selected]
        req = (
            req.set_index("category")
            .reindex(all_categories, fill_value=0)
            .reset_index()
        )
        req = req.sort_values(by="quantity", ascending=False)

        tab = tabulate(
            req[["category", "quantity"]],
            headers="keys",
            tablefmt="psql",
            showindex=False,
        )

    elif choice == 5:
        filtered_3 = grouped["amount"].sum().reset_index()

        req = filtered_3.loc[filtered_3["brand"] == brand_selected]

        req = (
            req.set_index("category")
            .reindex(all_categories, fill_value=0)
            .reset_index()
        )
        req = req.sort_values(by="amount", ascending=False)

        req["amount"] = req["amount"].astype(int)

        tab = tabulate(
            req[["category", "amount"]],
            headers="keys",
            tablefmt="psql",
            showindex=False,
        )

    print(f"\tBrand wise {picked} for {brand_selected}")
    return tab


# 20
def particular_search():
    df_items = read_file("data/items.csv")
    df_sales = read_file("data/sales.csv")

    filtered_0 = (
        df_sales.groupby("item_id")
        .agg({"quantity": "sum", "amount": "sum"})
        .reset_index()
    )

    merged = df_items.merge(filtered_0, on="item_id", how="left")
    merged = merged.fillna(0)
    merged.drop(columns=["product_name", "item_id"], inplace=True)

    all_brands = merged["brand"].drop_duplicates()
    brands = all_brands.to_list()
    print("\nAVAILABLE BRANDS")
    for i, brand in enumerate(brands, start=1):
        print(f"{i}. {brand}")
    brand_input = int(input("Select a brand: "))

    all_categories = merged["category"].drop_duplicates()
    categories = all_categories.to_list()
    print("\nAVAILABLE CATEGORIES")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    category_input = int(input("Select a Category: "))

    print(
        """\nAVAILABLE ANALYTICS
        1. Stock
        2. Items
        3. Stock Amount
        4. Sales
        5. Revenue"""
    )
    analyticals = {1: "stock", 2: "items", 3: "stock amount", 4: "sales", 5: "revenue"}

    choice = int(input("Pick an analytic: "))

    picked = analyticals[choice]
    brand_selected = brands[brand_input - 1]
    category_selected = categories[category_input - 1]

    exists = df_items[
        (df_items["brand"] == brand_selected)
        & (df_items["category"] == category_selected)
    ]
    if exists.empty:
        print("\n❌ This brand does not have items in this category")
        exit()

    merged["stock_value"] = merged["price"] * merged["stock"]
    base = merged[
        (merged["brand"] == brand_selected) & (merged["category"] == category_selected)
    ]

    column_map = {
        1: ("stock", "sum"),
        2: ("stock", "count"),
        3: ("stock_value", "sum"),
        4: ("quantity", "sum"),
        5: ("amount", "sum"),
    }

    col, func = column_map[choice]

    if func == "sum":
        value = base[col].sum()
    else:
        value = base[col].count()

    req = pd.DataFrame(
        {"brand": [brand_selected], "category": [category_selected], picked: [value]}
    )
    req[picked] = req[picked].astype(int)

    tab = tabulate(req, headers="keys", tablefmt="grid", showindex=False)

    print("=" * 46)
    print(tab)
    print("=" * 46)


# 21
def mega_search():
    df_sales = read_file("data/sales.csv")
    df_items = read_file("data/items.csv")


    filtered_0 = (
        df_sales.groupby("item_id").agg({"quantity": "sum", "amount": "sum"}).reset_index()
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
        """
        Availabe Options: 
        1. Search By Brand
        2. Search By Category 
        3. Specefic Search"""
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


    elif opt_choice == 2:
        print("\nAVAILABLE CATEGORIES")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        category_input = int(input("Select a category: "))
        if category_input < 1 or category_input > len(brands):
            print("Invalid choice")
            exit()
        category_selected = categories[category_input - 1]


    elif opt_choice == 3:
        print("\nAVAILABLE CATEGORIES")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        category_input = int(input("Select a category: "))
        if category_input < 1 or category_input > len(brands):
            print("Invalid choice")
            exit()
        category_selected = categories[category_input - 1]

        print("\nAVAILABLE BRANDS")
        for i, brand in enumerate(brands, start=1):
            print(f"{i}. {brand}")

        brand_input = int(input("Select a brand: "))
        if brand_input < 1 or brand_input > len(brands):
            print("Invalid choice")
            exit()
        brand_selected = brands[brand_input - 1]


    if opt_choice in [1, 3]:
        base = base[base["brand"] == brand_selected]

    if opt_choice in [2, 3]:
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
        if func == 'sum':
            req = base.groupby("category")[col].sum().reset_index()

        else:
            req = base.groupby("category")[col].count().reset_index()

        req[col] = req[col].astype(int)
        req = req.sort_values(by=col,ascending=False)


    elif opt_choice == 2:
        if func =='sum':
            req = base.groupby("brand")[col].sum().reset_index()

        else:
            req = base.groupby("brand")[col].count().reset_index()

        req[col] = req[col].astype(int)
        req = req.sort_values(by=col,ascending=False)



    elif opt_choice == 3:
        if func == "sum":
            value = base[col].sum()

        else:
            value = base[col].count()

        req = pd.DataFrame(
            {"brand": [brand_selected], "category": [category_selected], picked: [value]}
        )
        req[picked] = req[picked].astype(int)
    else:
        print("\nINVALID INPUT...")


    tab = tabulate(req, headers="keys", tablefmt="fancy_grid", showindex=False)
    return tab