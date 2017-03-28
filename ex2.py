from math import pi
menu = int(input("assignment number? \n"))
while menu != 0:
    if menu == 1:
        name = input("type u name:\n")
        print("Your name is: " + name[::-1] + "\n")
    elif menu == 2:
        rad = float(input("Radius is? \n"))
        print("Circumference is: " + str(pi*2.0*rad))
    elif menu == 3:
        filename = input("Type the file name: \n")
        filename = filename.split('.')
        print("The file type is: "+str(filename[-1]))
    elif menu == 4:
        n = int(input("input n: \n"))
        print("outcome is {y}".format(y=n+n*n+n**3))
    elif menu == 5:
        my_list = []
        for a in range(11):
            my_list += [a]
        print(my_list[::2])
    elif menu == 6:
        my_list1 = list(map(int, input("enter your list:\n").split()))
        my_list2 = list(map(int, input("enter another list:\n").split()))
        for a in my_list1:
            for b in my_list2:
                if a == b:
                    print("Found match {}".format(a))
                    break
    else:
        print("invalid choice! try again\n")
    menu = int(input("assignment number? \n"))

