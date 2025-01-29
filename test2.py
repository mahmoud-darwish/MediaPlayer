print(" do you fly?")
fly = input("yes or no ")
if fly == "yes": # he can fly
    print("are you wild")
    wild = input()
    if wild == "yes": # iam wild
        print("eagle")
    else:  # iam not wild
        print("parrot")

else:
    print("Do you live under the sea")
    undersea=input()
    if undersea == "yes": #live under the sea
        print("are you wild")
        wild = input()
        if wild == "yes":
            print("shark")
        else:
            print("dolphin")
    else: # do not live under sea
        print("are you wild")
        wild = input()
        if wild == "yes":
            print("lion")
        else:
            print("cat")
