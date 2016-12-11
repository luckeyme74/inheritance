import Inheritance

def main():
    writing_desk = Inheritance.Desk("desk", "cherry", 36, 24, 48, 225, 4, "center", 1)
    print ("Item: " + writing_desk.get_category())
    print ("Material: " + writing_desk.get_material())
    print ("Price: $" + str(writing_desk.get_price()))
    print ("Size: " + str(writing_desk.get_length()) + (" in. x " + str(writing_desk.get_width()) + " in. x " + str(writing_desk.get_height()) + " in."))
    print ("Drawer Location: " + writing_desk.get_drawer_location())
    print ("Drawer Quantity: " + str(writing_desk.get_drawer_quantity()))
    print ("Quantity: " + str(writing_desk.get_quantity()))
    print ("Total Price: $" + str(writing_desk.get_total()))


main()
