
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


# main routine goes here

onion = ""

while onion == "":
    # ask for width and height
        width = num_check("width: ")
        height = num_check("height: ")


    # calculate the area and perimeter
        area = width * height
        perimeter = 2 * (area + width)

    # display output
        print()
        print(f"area: {area} square units")
        print(f"perimeter: {perimeter} units")

    # ask if the user wants to continue

        onion = input("push enter to continue, or any key to quit ")
        print()


print("Thank you for using the area / perimeter calculator.Please ignor the smell walst you're exiting")
