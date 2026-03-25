import pandas as pd
from tabulate import tabulate
from data_handler import read_file


def search_inventory(item_id):

    df_1 = read_file("data/items.csv")
    filtered = df_1.loc[df_1["item_id"] == item_id]

    if filtered.empty:
        return None

    return filtered.iloc[0]


def search_category_file(item_id):
    category_files = {
        1: "data/mobiles.csv",
        2: "data/tablets.csv",
        3: "data/laptops.csv",
        4: "data/accessories.csv",
        5: "data/headphones.csv",
        6: "data/smartwatches.csv",
        7: "data/cameras.csv",
    }

    category_code = int(str(item_id)[0])
    file_path = category_files.get(category_code)

    df_2 = pd.read_csv(file_path)

    filtered_2 = df_2.loc[df_2["item_id"] == item_id]

    if filtered_2.empty:
        return None

    return filtered_2.iloc[0].drop("item_id")


def display_item(item_id):
    item_main = search_inventory(item_id)
    item_extra = search_category_file(item_id)

    combined = {}

    if item_main is not None:
        combined.update(item_main.to_dict())

    if item_extra is not None:
        combined.update(item_extra.to_dict())

    tab = [[key.replace("_", " ").title(), value] for key, value in combined.items()]

    print("\n" + "=" * 30)
    print("         ITEM DETAILS")
    print("=" * 30)

    return tabulate(tab, headers=["Field", "Value"], tablefmt="fancy_grid")
