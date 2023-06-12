def celsius_to_fahrenheit(celsius):
    """converts temperature from celsius to fahrenheit"""
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """convert temperature from fahrenheit to celsius"""
    celsius=(fahrenheit-32)*5/9
    return celsius

while True:
        print("1.convert  celsius to fahrenheit")
        print("2.convert  fahrenheit to celsius")
        print("3.Quit")
        choice=input("Enter your choice(1-3):")
        if choice=="1":
            celsius=float(input("Enter temperature in celsius:"))
            fahrenheit=celsius_to_fahrenheit(celsius)
            print('%.2f'%fahrenheit)
        elif choice=="2":
            fahrenheit=float(input("Enter temperature in fahrenheit:"))
            celsius=fahrenheit_to_celsius(fahrenheit)
            print('%.2f'%celsius)
        elif choice=="3":
            print("Good Bye")
            break
        else:
            print("Invalid choice!please try again!!!.\n")