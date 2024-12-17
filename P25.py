from os import system
system("cls")
number1=int(input("youre fav number1 ?:"))
number2=int(input("youre fav number2 ?:"))
number3=input("Which mathematical operation (-,+,//,**) ?:")
result1=(number1)+(number2)
result2=(number1)-(number2)
result3=(number1)**(number2)
result4=(number1)%(number2)
if    number3 == ('+'):
    print("result1",result1)
elif  number3 == ('-'):
    print("result2",result2)
elif  number3 == ('*'):
    print("I won't do anything for you")
elif  number3 == ('/'):
    print("I won't do anything for you")
elif  number3 == ('**'):
    print("result3",result3)
elif  number3 == ('%'):
    print("result4",result4)