def parsa():
    parsa=(input("<<"))
    poyan,math,naderi=parsa.split()
    if poyan == "hello":
        print(f"result: ${int(math)-int(naderi)}")
    elif poyan == "hi":
        print(f"result: ${int(math)-int(naderi)}")
    elif poyan == "parsa":
        print(f"result: ${int(math)-int(naderi)}")
    else :
        print("go out!")
parsa()