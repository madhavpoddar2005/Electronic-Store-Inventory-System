import pandas as pd
import os
from data_handler import *


def add_mobiles(item_id):
    ram = int(input("Enter ram (in GB): "))
    storage = int(input("Enter storage (in GB): "))
    camera_quality = int(input("Enter camera quality (in Mp): "))
    battery = int(input("Enter battery life (in MAH): "))
    mobiles = {
        "item_id": item_id,
        "ram": ram,
        "storage": storage,
        "camera_quality": camera_quality,
        "battery": battery,
    }
    return mobiles


def add_laptops(item_id):
    ram = int(input("Enter ram (in GB): "))
    storage = int(input("Enter storage (in GB): "))
    cpu = input("Enter CPU processor: ")
    gpu = input("Enter GPU: ")
    laptops = {
        "item_id": item_id,
        "ram": ram,
        "storage": storage,
        "cpu": cpu,
        "gpu": gpu,
    }
    return laptops


def add_tablets(item_id):
    ram = int(input("Enter ram (in GB): "))
    storage = int(input("Enter storage (in GB): "))
    screen_size = int(input("Enter screen size: "))
    battery = int(input("Enter battery life (in MAH): "))
    tablets = {
        "item_id": item_id,
        "ram": ram,
        "storage": storage,
        "screen_size": screen_size,
        "battery": battery,
    }
    return tablets


def add_headphones(item_id):
    wireless = input("Wireless?(yes/no): ")
    if wireless.strip().lower() == "yes":
        battery_hours = int(input("Enter battery life (in hrs): "))
    else:
        battery_hours = None
    noise_cancelling = input("Noise cancelling?(yes/no)")
    mics = int(input("Enter number of mics: "))
    headphones = {
        "item_id": item_id,
        "wireless": wireless,
        "battery_hours": battery_hours,
        "noise_cancelling": noise_cancelling,
        "mics": mics,
    }
    return headphones


def add_accessories(item_id):
    accessory_type = input("Enter type: ")
    compatibility = input("Enter compatibility: ")
    accessories = {
        "item_id": item_id,
        "accessory_type": accessory_type,
        "compatibility": compatibility,
    }
    return accessories


def add_smart_watches(item_id):
    display_size = int(input("Enter display size: "))
    battery_hours = int(input("Enter battery hours: "))
    gps = input("GPS?(yes/no): ")
    water_resistant = input("Water Resistant?(yes/no): ")
    smart_watches = {
        "item_id": item_id,
        "display_size": display_size,
        "battery_hours": battery_hours,
        "gps": gps,
        "water_resistant": water_resistant,
    }
    return smart_watches


def add_cameras(item_id):
    sensor = input("Enter sensor: ")
    resolution = input("Enter resolution: ")
    video = input("Enter video: ")
    weight = input("Enter weight: ")
    cameras = {
        "item_id": item_id,
        "sensor": sensor,
        "resolution": resolution,
        "video": video,
        "weight": weight,
    }
    return cameras


def additem():
    print("""\n\t\tADD AN ITEM""")
    print(
        """Categories
            1. Mobiles
            2. Tablets
            3. Laptops
            4. Accessories
            5. Headphones
            6. Smart Watches
            7. Cameras
            8. Exit
            """
    )

    item_id = int(input("Enter item id: "))

    df = read_file("data/items.csv")

    if item_id in df["item_id"].values:

        print("Item exist...\n")

        stock_up = int(input("Enter new stock: "))
        print("\nIncreasing existing stock...")
        df.loc[df["item_id"] == item_id, "stock"] += stock_up
        df.to_csv("data/items.csv", index=False)
        print(f"Stock updated for item id: {item_id}")

    else:
        product_name = input("Enter product name: ")
        brand = input("Enter brand: ")
        price = int(input("Enter price: "))
        stock = int(input("Enter stock size: "))
        category_choice = item_id // 100

        categories = {
            1: "Mobiles",
            2: "Tablets",
            3: "Laptops",
            4: "Accessories",
            5: "Headphones",
            6: "Smart Watches",
            7: "Cameras",
        }

        category = categories.get(category_choice)

        if category is None:
            print("Invalid category")
            return

        items = {
            "item_id": item_id,
            "product_name": product_name,
            "brand": brand,
            "category": category,
            "price": price,
            "stock": stock,
        }

        append_to_csv(
            "data/items.csv",
            list(items.values()),
            list(items.keys()),
        )

        if category_choice == 1:
            category_data = add_mobiles(item_id)
            append_to_csv(
                "data/mobiles.csv",
                list(category_data.values()),
                list(category_data.keys()),
            )

        elif category_choice == 2:
            category_data = add_tablets(item_id)
            append_to_csv(
                "data/tablets.csv",
                list(category_data.values()),
                list(category_data.keys()),
            )

        elif category_choice == 3:
            category_data = add_laptops(item_id)
            append_to_csv(
                "data/laptops.csv",
                list(category_data.values()),
                list(category_data.keys()),
            )

        elif category_choice == 4:
            category_data = add_accessories(item_id)
            append_to_csv(
                "data/accessories.csv",
                list(category_data.values()),
                list(category_data.keys()),
            )

        elif category_choice == 5:
            category_data = add_headphones(item_id)
            append_to_csv(
                "data/headphones.csv",
                list(category_data.values()),
                list(category_data.keys()),
            )

        elif category_choice == 6:
            category_data = add_smart_watches(item_id)
            append_to_csv(
                "data/smartwatches.csv",
                list(category_data.values()),
                list(category_data.keys()),
            )

        elif category_choice == 7:
            category_data = add_cameras(item_id)
            append_to_csv(
                "data/cameras.csv",
                list(category_data.values()),
                list(category_data.keys()),
            )

        elif category_choice == 8:
            print("\n\tGOODBYE...")
            return



