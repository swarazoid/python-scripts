print("Welcome human!")
s = "y"
while(s == "y"):
    try:
        num = int(input("Enter a number : "))
        if(num % 2 == 0):
            print("{} is an even number".format(num))
        else:
            print("{} is an odd number".format(num))
    except ValueError:
        print("That's not an integer")
    s = input("Do you want another? (y/n) : ")
print("Good Bye!")
