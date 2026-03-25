import pandas as pd
from tabulate import tabulate
from inventory import *
from sales import *
from search import *
from analytics import *
from graphs import *


def analytics_menu():
    while True:
        print("\n" + "=" * 40)
        print("\t ANALYTICS MENU")
        print("=" * 40)

        print(" 1. Total Sales")
        print(" 2. Profit")
        print(" 3. Total Sales Entries")
        print(" 4. Total Item Entries")
        print(" 5. Stock Available")
        print(" 6. Low Stock Items")
        print(" 7. Top Selling Item")
        print(" 8. Revenue Per Item")
        print(" 9. Stock Available per brands")
        print("10. items Available per brands")
        print("11. Top Selling Brand")
        print("12. Brand Revenue")
        print("13. Category Stock")
        print("14. Category Items")
        print("15. Stock Per Category Per Brand ")
        print("16. Sales Per Category Per Brand ")
        print("17. Revenue Per Category Per Brand ")
        print("18. Search By Category")
        print("19. Search By Brand")
        print("20. Particular Search")
        print("21. Mega Search")
        print("22. Exit")

        try:
            choice = int(input("\nEnter your Choice: "))

        except ValueError:
            print("\nInvalid input...")
            continue

        if choice == 1:
            print("\nTotal Sales: ", total_sales())

        elif choice == 2:
            print("\nProfit: ", sales_profit())

        elif choice == 3:
            print("\nTotal Sales Entries: ", sales_entries())

        elif choice == 4:
            print("\nTotal Item Entries: ", items_entries())

        elif choice == 5:
            print("=" * 50)
            print("\t  STOCK AVAILABLE")
            print("=" * 50)

            print(get_stock())

        elif choice == 6:
            print("=" * 45)
            print("\t⚠️ LOW STOCK ITEMS")
            print("=" * 45)

            print(low_stock())

        elif choice == 7:
            print("=" * 50)
            print("\t  TOP SELLING ITEMS")
            print("=" * 50)

            print(top_selling_item())

        elif choice == 8:
            print("=" * 50)
            print("\t  REVENUE PER ITEM")
            print("=" * 50)

            print(revenue_per_item())

        elif choice == 9:
            print("=" * 30)
            print(" Stock Available per brands")
            print("=" * 30)

            print(brand_stock())

        elif choice == 10:
            print("=" * 30)
            print(" items Available per brands")
            print("=" * 30)

            print(brand_items())

        elif choice == 11:
            print("=" * 36)
            print("\t  TOP SELLING BRANDS")
            print("=" * 36)

            print(top_selling_brand())

        elif choice == 12:
            print("=" * 23)
            print("   BRANDS REVENUE")
            print("=" * 23)

            print(brand_revenue())

        elif choice == 13:
            print("=" * 23)
            print("   CATEGORY STOCK")
            print("=" * 23)
            print(category_stock())

        elif choice == 14:
            print("=" * 23)
            print("   CATEGORY STOCK")
            print("=" * 23)
            print(category_items())

        elif choice == 15:
            print("=" * 134)
            print("\t\t\t\t\tSTOCK PER CATEGORY PER BRAND")
            print("=" * 134)

            print(category_vs_brand_stock())

        elif choice == 16:
            print("=" * 134)
            print("\t\t\t\t\t\tSALES PER CATEGORY PER BRAND")
            print("=" * 134)

            print(category_vs_brand_sales())

        elif choice == 17:
            print("=" * 118)
            print("\t\t\t\t\t\tREVENUR PER CATEGORY PER BRAND")
            print("=" * 118)

            print(category_vs_brand_revenue())

        elif choice == 18:
            print(search_by_category())

        elif choice == 19:
            print(search_by_brand())

        elif choice ==20:
            print(particular_search())
        
        elif choice == 21:
            print(mega_search())

        elif choice == 22:
            print("\nExiting Analytics Menu...")
            break

        else:
            print("\nInvalid choice. Try again.")
            analytics_menu()


def graphs_menu():
    while True:
        print("\n" + "=" * 40)
        print("\t GRAPHS MENU")
        print("=" * 40)

        print(" 1. Brand v/s Items")
        print(" 2. Brand v/s Stock")
        print(" 3. Brand v/s Items Sold")
        print(" 4. Brand v/s Revenue")
        print(" 5. Items v/s Category")
        print(" 6. Stock v/s Category")
        print(" 7. Sales Per Month")
        print(" 8. Revenue Per Month")
        print(" 9. Mega Graph")
        print("10. Mega Graph Month Wise")
        print("11. Exit")

        try:
            choice = int(input("\nEnter your Choice: "))
        except ValueError:
            print("\nInvalid input...")
            continue

        if choice == 1:
            brand_vs_items()

        elif choice == 2:
            brand_vs_stock()

        elif choice == 3:
            brand_vs_items_sold()

        elif choice == 4:
            brand_vs_revenue()

        elif choice == 5:
            items_vs_category()

        elif choice == 6:
            stock_vs_category()

        elif choice == 7:
            sales_per_month()

        elif choice == 8:
            revenue_per_month()

        elif choice == 9:
            mega_graph()

        elif choice ==10:
            mega_month_graph()

        elif choice == 11:
            print("\nExiting graphs menu....")
            break

        else:
            print("\nInvalid Input... Try again...")
            graphs_menu()


def main():
    while True:
        print(
            """\n\tELECTRONICS STORE INVENTORY MANAGEMENT SYSTEM
                1. ADD ITEM
                2. SELL ITEM 
                3. SHOW INVENTORY
                4. SEARCH ITEM
                5. SHOW SOLD ITEMS
                6. SHOW ANALYTICS MENU
                7. SHOW GRAPHS MENU
                8. Exit"""
        )
        try:
            choice = int(input("\nEnter your Choice: "))
        except ValueError:
            print("\nInvalid input...")
            continue

        if choice == 1:
            additem()

        elif choice == 2:
            add_sales()

        elif choice == 3:
            df = pd.read_csv("data/items.csv")
            tab = tabulate(
                df, headers=list(df.columns), tablefmt="fancy_grid", showindex=False
            )
            print(tab)

        elif choice == 4:
            input_id = int(input("\nEnter item id: "))
            item = display_item(input_id)
            if item is None:
                print("\nItem does not exist...")
            else:
                print(item)

        elif choice == 5:
            show_sales()

        elif choice == 6:
            analytics_menu()

        elif choice == 7:
            graphs_menu()

        elif choice == 8:
            print("\n\tGOODBYE...")
            break

        else:
            print("\nInvalid Input...")
            break


if __name__ == "__main__":
    main()
