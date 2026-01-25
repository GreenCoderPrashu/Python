def Math_Operations():
    print(" \n I'm here to help on Mathematical Operations \n _______________________________________________")
    while True:

        print("Which type of operation you want??? \n Choose one as follows \n 1) Logical Operations... \n 2) Scientific Operations... \n 3) Basic Arithmetic Operations... \n 4) Exit...")
        ch = int(input("\"Enter your choice\" :  "))
    
        def Logical_Operations():
            print("Currently Working On it...")
            exit()

        def Scientific_Operations():
            print("Currently Working On it...")
            exit()
            
            
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
                    print("Plese enter the correct choice")
        if ch == 1:
            Logical_Operations()
        elif ch == 2:
            Scientific_Operations()
        elif ch == 3:
            Arithmetic_Operations()
        elif ch == 4:
            exit()
        else :
            print("Plese enter the correct choice")                          
Math_Operations()
