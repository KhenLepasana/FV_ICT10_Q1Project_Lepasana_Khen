from pyscript import document

# Restaurant info
restaurant_name = "The FoodFather"  # string
owner_name = "Khen Lepasana"        # string
year_established = 2025             # integer
has_delivery = True                 # boolean
business_hours = "10:00 AM - 9:00 PM"  # string
tax_rate = 0.08                     # float

# Menu items and prices
product_names = ["Truffle Pasta", "Cheese Pizza", "Caesar Salad", "Iced Latte", "Fresh Lemonade"]  # list
menu_prices = {
    "Truffle Pasta": 320,
    "Cheese Pizza": 250,
    "Caesar Salad": 150,
    "Iced Latte": 80,
    "Fresh Lemonade": 60
}  # dictionary
common_allergens = ["Nuts", "Dairy", "Gluten"]  # list

def generate_order(e):
    # Get customer info
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    # Calculate total
    total = 0
    if document.getElementById("item1").checked:
        total += menu_prices["Truffle Pasta"]
    if document.getElementById("item2").checked:
        total += menu_prices["Cheese Pizza"]
    if document.getElementById("item3").checked:
        total += menu_prices["Caesar Salad"]
    if document.getElementById("item4").checked:
        total += menu_prices["Iced Latte"]
    if document.getElementById("item5").checked:
        total += menu_prices["Fresh Lemonade"]

    final_total = total + (total * tax_rate)

    message = f'''🍽️ Order
Customer Name : {name}
Address       : {address}
Contact       : {contact}

Total Amount  : ₱{final_total:.2f}

Thank you for ordering at {restaurant_name}!'''

    document.getElementById("output").innerText = message
