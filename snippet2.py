def strToInt(num1, num2):
    # sees if num1 and num2 can be casted as floats
    if (not num1.replace(".", "").isnumeric() or not num2.replace(".", "").isnumeric()):
        return False
    return (float(num1), float(num2))


def main():

    # get user input and validate
    user_input = input("Enter 2 numbers and arithmetic sign: ")

    # split user input and validate
    content = user_input.split(' ')
    if (not (len(content) == 3)):
        print("Needs to be three arguments, did you put a space between each argument?")
        return 0

    # turn string into int and validate
    numbers = strToInt(content[0], content[2])
    if (not numbers):
        print("Invalid numbers, please try again")
        return 0

    # python 3.10 match & case
    match content[1]:
        case "+":
            print(user_input, f"= {numbers[0] + numbers[1]}")
        case "-":
            print(user_input, f"= {numbers[0] - numbers[1]}")
        case "*":
            print(user_input, f"= {numbers[0] * numbers[1]}")
        case "/":
            if (numbers[1] == 0):
                print("Cant divide by 0 ;-;")
                return 0
            print(user_input, f"= {numbers[0] / numbers[1]}")
        case _:
            print("Not a valid arithmetic sign")
            return 0


if __name__ == "__main__":
    main()
