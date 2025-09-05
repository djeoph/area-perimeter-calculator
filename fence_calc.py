
def num_check(question):
    error = "please enter a number that is over zero"

    while True:
        try:
            big = float(input(question))

            if big > 0:
                return big

            else:
                print(error)

        except ValueError:

            print(error)

#a dinner routine goes here

stew_makin = ""

#ask the user for the ingredients

while stew_makin =="":


    width = num_check("width: ")

    height = num_check("height: ")

    cost = num_check("cost per meter: ")

#make the stew

    broth = (width + height) * 2

    meat = cost * broth

#present the stew

    print(f"perimeter: {broth}")
    print(f"cost: ${meat:.2f}")

#continue?

    stew_makin = input("push enter to continue, or any key to quit ")
    print()

print("thank you for using the calculator")





