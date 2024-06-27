import csv


cookies = []


def read_cookies_from_csv():
    global cookies
    with open('data/cookies.csv', mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cookie = {
                'id': int(row['id']),
                'title': row['title'],
                'description': row['description'],
                'price': float(row['price']),
                'sugar_free': row['sugar_free'].lower() == 'true',
                'gluten_free': row['gluten_free'].lower() == 'true',
                'contains_nuts': row['contains_nuts'].lower() == 'true'
            }
            cookies.append(cookie)


def welcome_and_get_preferences():
    print("Welcome to the Python Cookie Shop!")
    print("We feed each according to their need.")

    print("\nWe'd hate to trigger an allergic reaction in your body. So please answer the following questions:")
    allergic_to_nuts = input("Are you allergic to nuts? (yes/no): ").lower() in ['yes', 'y']
    allergic_to_gluten = input("Are you allergic to gluten? (yes/no): ").lower() in ['yes', 'y']
    diabetic = input("Do you suffer from diabetes? (yes/no): ").lower() in ['yes', 'y']
    
    return allergic_to_nuts, allergic_to_gluten, diabetic


def display_cookies(allergic_to_nuts, allergic_to_gluten, diabetic):
    print("\nHere are the cookies we have in the shop for you:\n")
    for cookie in cookies:
        if (not allergic_to_nuts or not cookie['contains_nuts']) and \
           (not allergic_to_gluten or not cookie['gluten_free']) and \
           (not diabetic or not cookie['sugar_free']):
            print(f"#{cookie['id']} - {cookie['title']}")
            print(cookie['description'])
            print(f"Price: ${cookie['price']:.2f}\n")


def process_orders():
    orders = {}
    while True:
        order_id = input("Please enter the number of any cookie you would like to purchase (type 'finished' to complete your order): ")
        if order_id.lower() in ['finished', 'done', 'quit', 'exit']:
            break
        try:
            order_id = int(order_id)
            if order_id < 1 or order_id > len(cookies):
                print("Invalid cookie ID. Please enter a valid ID.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid cookie ID.")
            continue
        
        quantity = input(f"How many {cookies[order_id - 1]['title']} would you like? ")
        try:
            quantity = int(quantity)
            if quantity < 1:
                print("Quantity should be greater than zero.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")
            continue
        
        if order_id in orders:
            orders[order_id] += quantity
        else:
            orders[order_id] = quantity
    
    print("\nThank you for your order. You have ordered:\n")
    total_price = 0
    for order_id, quantity in orders.items():
        cookie = cookies[order_id - 1]
        subtotal = cookie['price'] * quantity
        total_price += subtotal
        print(f"- {quantity} {cookie['title']}")
    
    print(f"\nYour total is ${total_price:.2f}.")
    print("Please pay with Bitcoin before picking up.\n")
    print("Thank you!")
    print("- The Python Cookie Shop Robot.")


def main():
    read_cookies_from_csv()
    allergic_to_nuts, allergic_to_gluten, diabetic = welcome_and_get_preferences()
    display_cookies(allergic_to_nuts, allergic_to_gluten, diabetic)
    process_orders()

if __name__ == "__main__":
    main()