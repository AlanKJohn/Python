while True:
    first_unit=input("Hi, which unit would you like to convert choose either cm,in or ft.")
    if first_unit=="cm":
            print("Ok what is the second unit.")
            break
    elif first_unit=="in":
            print("Ok what is the second unit.")
            break
    elif first_unit=="ft":
            print("Ok what is your second unit.")
            break
    else:
            print("Invalid Input.")
            first_unit=0
while True:
    second_unit=input("Choose the next unit to convert the height which are cm,ft or in.")
    if second_unit=="cm":
            print("Ok we are working on it.")
            break
    elif second_unit=="in":
            print("Ok we are working on it.")
            break
    elif second_unit=="ft":
            print("Ok we are working on it.")
            break
    else:
            print("Invalid Input.")
            second_unit=0
while True:
    value=float(input("Enter the value for the first unit."))
    if first_unit=="cm" and second_unit=="in":
            print(value*0.393701)
            break
    elif first_unit=="in" and second_unit=="cm":
            print(value * 2.54)        
            break
    elif first_unit=="ft" and second_unit=="cm":
            print(value*30.48)
            break
    elif first_unit=="cm" and second_unit=="ft":
            print(value*0.0328084)
            break
    elif first_unit=="ft" and second_unit=="in":
            print(value*12)
            break
    elif first_unit=="in" and second_unit=="ft":
            print(value*0.0833333)
            break
    else:
            print("Invaild Input")
            value=0           
