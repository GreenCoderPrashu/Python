import math
def Math_Operations():
    print(" \n I'm here to help on Mathematical Operations \n _______________________________________________")
    while True:

        print("Which type of operation you want??? \n Choose one as follows \n 1) Logical Operations... \n 2) Trigonometric Operations... \n 3) Basic Arithmetic Operations... \n 4) Exit...")
        ch = int(input("\"Enter your choice\" :  "))
    
        def Logical_Operations():
            print("Basic Logical Operations \n _____________________________________")
            print("Choose Your Choice \n 1) \'OR\' Operations \n 2) \'AND\' Operations \n 3) \'NOT\' Operations \n 4) \'NOR\' Operations \n 5) \'NAND\' Operations")
            print(" 6) Exit From Basic Logical Operations")
            while True:
                ch = int(input("\"Enter your choice\" (To see choice list enter 0): "))
                if ch == 1:
                    print("You selected \"\'OR\' Operations\" \n --------------------------------------------")
                    x=(input("Enter Firest Value (\"True \\ False\") :")).lower() == 'true'
                    y=(input("Enter Second Value (\"True \\ False\") :")).lower() == 'true'
                    print(f"{x} OR {y} = {x or y}")
                elif ch == 2:
                    print("You selected \"\'AND\' Operations\" \n -------------------------------------------- ")
                    x=(input("Enter Firest Value (\"True \\ False\") :")).lower() == 'true'
                    y=(input("Enter Second Value (\"True \\ False\") :")).lower() == 'true'
                    print(f"{x} AND {y} = {x and y}")
                elif ch == 3:
                    print("You selected \"\'NOT\' Operations\" \n -------------------------------------------- ")
                    x=(input("Enter The Value (\"True \\ False\") :")).lower() == 'true'
                    print(f"NOT Of {x} = {not(x)}")
                elif ch == 4:
                    print("You selected \"\'NOR\' Operations\" \n -------------------------------------------- ")
                    x=(input("Enter Firest Value (\"True \\ False\") :")).lower() == 'true'
                    y=(input("Enter Second Value (\"True \\ False\") :")).lower() == 'true'
                    nor =x or y
                    print(f"{x} NOR {y} = {not(nor)}")
                elif ch == 5:
                    print("You selected \"\'NAND\' Operations\" \n -------------------------------------------- ")
                    x=(input("Enter Firest Value (\"True \\ False\") :")).lower() == 'true'
                    y=(input("Enter Second Value (\"True \\ False\") :")).lower() == 'true'
                    nand =x and y
                    print(f"{x} NAND {y} = {not(nand)}")
                elif ch == 6:
                    print("You selected \"Exit from the Basic Logical Operations\"")
                    print("\n \" Exited From Basic Logical Operations \"")
                    break
                elif ch == 0:
                    print("Choose Your Choice \n 1) \'OR\' Operations \n 2) \'AND\' Operations \n 3) \'NOT\' Operations \n 4) \'NOR\' Operations \n 5) \'NAND\' Operations")
                    print(" 6) Exit From Basic Logical Operations") 
                else:
                    print("Please enter the correct choice")

        def Trigonometric_Operations():
            print("Basic Trigonometric Operations \n _____________________________________")
            print("Choose Your Choice \n 1) Sine(sin) \n 2) Cosine(cos) \n 3) Tangent(tan) 4) Exit From Trigonometric Operations")
            while True:
                ch = int(input("\"Enter your choice\" (To see choice list enter 0): "))
                if ch == 0:
                    print("Choose Your Choice \n 1) Sine(sin) \n 2) Cosine(cos) \n 3) Tangent(tan) 4) Exit From Trigonometric Operations")
                elif ch == 1:
                    print("You selected \"\'Sine(sin)\' Operations\" \n --------------------------------------------")
                    r = float(input("Enter Angle in Radians :"))
                    sin = math.sin(r)
                    print(f"The value of sin is : {sin}")
                elif ch == 2:
                    print("You selected \"\'Cosine(cos)\' Operations\" \n --------------------------------------------")
                    r = float(input("Enter Angle in Radians :"))
                    cos = math.cos(r)
                    print(f"The value of cos is : {cos}")
                elif ch == 3:
                    print("You selected \"\'Tangent(tan)\' Operations\" \n --------------------------------------------")
                    r = float(input("Enter Angle in Radians :"))
                    tan = math.tan(r)
                    print(f"The value of tan is : {tan}")
                elif ch == 4:
                    print("You selected \"Exit from Trigonometric Operations\"")
                    print("\n \" Exited From Trigonometric Operations \"")
                    break
                else:
                    print("Please enter the correct choice")
            
            
        def Arithmetic_Operations():
            print("Basic Arithmetic Operations\n __________________________________")
            print("Your choices are:-\n1==> For \"Addition\"\n2==> For \"Substraction\"\n3==> For \"Multiplication\"\n4==> For \"Division\" ")
            print("5==> For \"Modulus\"\n6==> For \"See the history of your caluculations\"\n7==> For \"Exit from the Basic Arithmetic Operations\"")
            History = []
            while True:
                ch = int(input("\"Enter your choice\" (To see choice list enter 0): "))

                if ch == 1:
                    H = []
                    num = (input("Enter the Numbers separated by space :")).split()
                    num = [float(n) for n in num]
                    print("You selected \"Addition\"")
                    sum = 0 
                    for n in num:
                        sum += n
                        H.append(str(n)) 
                        exp = "+".join(H)
                    print(f"{exp} = {sum}")
                    history_entry = f"{exp} = {sum}"
                    History.append(history_entry) 
                elif ch == 2:
                    print("You selected \"Subtraction\"")
                    x = float(input("Enter the Firest number : "))
                    y = float(input("Enter the Second number : "))
                    print(f"The diffrence between{x} and {y} is : {x-y}")
                    history_entry = f"{x} - {y} = {x-y}"
                    History.append(history_entry) 
                elif ch == 3:
                    H = []
                    print("You selected \"Multiplication\"")
                    items = (input("Enter the Numbers separated by space :")).split()
                    items = [float(item) for item in items]
                    pro = 1 
                    for item in items:
                        pro = item * pro
                    
                        H.append(str(item)) 
                        exp = "*".join(H)
                    print(f"{exp} = {pro}")
                    history_entry = f"{exp} = {pro}"
                    History.append(history_entry) 
                elif ch == 4:
                    print("You selected \"Division\"")
                    x = float(input("Enter the Firest number : "))
                    y = float(input("Enter the Second number : "))
                    print(f"The Division of {x} and {y} is : {x/y}")
                    history_entry = f"{x} / {y} = {x/y}"
                    History.append(history_entry) 
                elif ch == 5:
                    print("You selected \"Modulus\"")
                    x = float(input("Enter the Firest number : "))
                    y = float(input("Enter the Second number : "))
                    print(f"The Modulus of {x} and {y} is : {x%y}")
                    history_entry = f"{x} % {y} = {x%y}"
                    History.append(history_entry) 
                elif ch == 6:
                    print("You selected \"History of the your caluculations\"")
                    for record in History:
                        print(record)
                    history_entry = f"You searched history"
                    History.append(history_entry) 
                elif ch == 7:
                    print("You selected \"Exit from the Basic Arithmetic Operations\"")
                    print("\n \" Exited From Basic Arithmetic Operations \"")
                    break
                elif ch == 0:
                    print("Basic Arithmetic Operations\n __________________________________")
                    print("Your choices are:-\n1==> For \"Addition\"\n2==> For \"Substraction\"\n3==> For \"Multiplication\"\n4==> For \"Division\" ")
                    print("5==> For \"Modulus\"\n6==> For \"See the history of your caluculations\"\n7==> For \"Exit from the Basic Arithmetic Operations\"")

                else:
                    print("Please enter the correct choice")
        if ch == 1:
            Logical_Operations()
        elif ch == 2:
            Trigonometric_Operations()
        elif ch == 3:
            Arithmetic_Operations()
        elif ch == 4:
            exit()
        else :
            print("Please enter the correct choice")                          
Math_Operations()
