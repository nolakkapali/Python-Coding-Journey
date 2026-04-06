print("Disclaimer:////Choose C->F, Click C or\n Otherwise for F->C Choose F")
User = input("Option: ")
if (User == "C"):
    celsius = float(input("Enter Celsium Temparature: "))
    farenheit = celsius*5/9+32
    print(f"Temparature is {farenheit}F")
else:
    farenheit = float(input("Enter Farenheit Temparature: "))
    celsius = (farenheit-32)*9/5
    print(f"Temparature is {celsius}C")
