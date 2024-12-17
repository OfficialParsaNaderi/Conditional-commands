from os import system
system("cls")
name=input("first what your name ? :")
weather=int(input(" how's it weather conditions in number ?:"))
if weather<20:
    print("it's weather is cold")
elif 20<weather<30:
    print("it's weather is mild")
elif 30<weather<40:
    print("it's weather is hot")
elif weather>40:
    print("please don't come out")