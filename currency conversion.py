def dollar_to_euro(dollar):
    """converts dollars to euros"""
    euro=0.93*dollar
    return euro
def dollar_to_rupee(dollar):
    """converts dollars to rupees"""
    rupee=82.67*dollar
    return rupee
def dollar_to_pound(dollar):
    """converts dollars to pound"""
    pound=0.81*dollar
    return pound
def pound_to_rupee(pound):
    """coverts pounds to rupees"""
    rupee=102.61*pound
    return rupee
def rupee_to_yen(rupee):
    """converts rupees to yen"""
    yen=1.68*rupee
    return yen
while True:
    print("1.Convert dollars to euros ")
    print("2.convert dollars to rupees")
    print("3.convert dollars to pounds")
    print("4.convert pound to rupees")
    print("5.convert rupee to yen")
    print("6.Quit")
    choice=input("Enter your choice(1-6):")
    if choice=='1':
        dollar=float(input("Enter the currency value in dollar:"))
        euro=dollar_to_euro(dollar)
        print("The value of ",'%.2f'%dollar,"dollar in euros is",'%.2f'%euro)
    elif choice=='2':
        dollar=float(input("Enter the currency value in dollar:"))
        rupee=dollar_to_rupee(dollar)
        print("The value of ",dollar,"'%.2f'%dollar in rupees is",'%.2f'%rupee)
    elif choice=='3':
        dollar=float(input("Enter the currency value in dollar:"))
        pound=dollar_to_pound(dollar)
        print("The value of ",'%.2f'%dollar,"dollar in pounds is",'%.2f'%pound)
    elif choice=='4':
        pound=float(input("Enter the currency value in pound:"))
        rupee=pound_to_rupee(pound)
        print("The value of ",'%.2f'%pound,"pounds in rupees is",'%.2f'%rupee)
    elif choice=='5':
        rupee=float(input("Enter the currency value in rupee:"))
        yen=rupee_to_yen(rupee)
        print("The value of ",'%.2f'%rupee,"rupees in yens is",'%.2f'%yen)
    elif choice=='6':
        print("bye")
        break
    else :
        print("Invalid choice!please try again!!!")