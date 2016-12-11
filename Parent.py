import Inheritance

def main():
    desk_chair = Inheritance.office_furniture("chair", "leather", 36, 36, 48, 75, 10)
    print ("Item: " + desk_chair.get_category())
    print ("Material: " + desk_chair.get_material())
    print ("Price: $" + str(desk_chair.get_price()))
    print ("Quantity: " + str(desk_chair.get_quantity()))
    print ("Size: " + str(desk_chair.get_length()) + (" in. x " + str(desk_chair.get_width()) + " in. x " + str(desk_chair.get_height()) + " in."))
    print ("Total Price: $" + str(desk_chair.get_total()))


main()
