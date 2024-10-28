while True:
    print("\n.1\tconvert celsius to fahrenheit")
    print("2.\tconvert fahrenheit to celsius")
    print("3.\t exit the programe")
    option = int(input("enter your option"))
    if option ==1:
        temp=int(input("enter temprature in celsius"))
        fahrenheit = (9/5*temp)+32
        print(fahrenheit)
    elif option ==2:
        temp=int(input("enter temprature in fahrenhite"))
        celsius = (5/9)*(temp-32)
        print(celsius)
    elif option == 3:
        break
