    
def calculator():
    print("Taschenrechner")

    check = ["*","+","-","/"]

    number1 = float(input("number 1: "))
    operator = input("Operator: ")

    if operator not in check:
        print("Invalid operator!")
        return 

    number2 = float(input("number 2: "))

    try:
        if operator == "+":
            print(number1 + number2)

        elif operator =="-":
            print(number1 - number2)

        elif operator =="*":
            print(number1 * number2)

        elif operator =="/":
            print(number1 / number2)

    except:
        print("An error ecured, sorry try again by restarting your programm!")

while True:
    print("1. calculator")
    print("2. exit")

    action = input(">")

    if action == "1":
        calculator()

    elif action =="exit":
        break

    else:
        print("Error! Please just enter the number of the action you want!")
        