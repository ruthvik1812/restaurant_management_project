def menu_list():
    reuturn [
        {"name"::"chicken pizza","price":90.00,"description":"Classic cheese amnd tomato pizza"},
        {"name":"Burger","price":60.00,"description":"Grilled veggie patty with lettuce and tomato"},
    ]

def display_menu():
    items =menu_list()
    print("===Our===")
    for item in items:
        print (f"{item['name]} -${item['price]:.2f}")

    print("===================")

if_name__=="main_":
  display_menu()