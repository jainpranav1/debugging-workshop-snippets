import os


def create():
    # get data from user
    data = []
    name = input("What would you like to name this file?: ")
    data.append(name)
    print("Type 'done' to finish creating the list")
    bullet_point = input(" * ")
    while (bullet_point.strip() != "done"):
        data.append(bullet_point)
        bullet_point = input(" * ")

    # write content to file seperated by comma
    with open(f"lists/{name}.txt", "w") as f:
        # adding the brackets is just for asthetics :P
        f.write("[")
        for content in data[:-1]:
            f.write(content+",")
        f.write(data[-1]+"]\n")


def view():
    # check if file path exists
    name = input("What file would you like to view?: ")
    fileCheck1 = os.path.isfile(f"lists/{name}.txt")
    fileCheck2 = os.path.isfile(f"lists/{name}")
    if (not (fileCheck1 or fileCheck2)):
        print("File not found")
        return 0

    # get file and print it out
    with open(f"lists/{name}.txt", "r") as f:
        data = f.read()
        data = data.split(",")
    for content in data[1:-1]:
        print(" *", content)
    print(" *", data[-1][:-2])


def all():
    # gets list of all files in lists directory
    files = os.listdir("lists")

    # making output look prettier
    for file in files:
        print(" *", file)


def main():
    # list making/viewing mini app
    done = False
    while (not done):
        user_input = input(
            "What would you like to do? (type help for more info): ")
        if (user_input.strip() == "exit"):
            done = True
        elif (user_input.strip() == "help"):
            print("Options:")
            print("1. type exit to exit program")
            print("2. type create to create a list")
            print("3. type view to view a list")
            print("4. type all to see all stored lists")
        elif (user_input.strip() == "create"):
            create()
        elif (user_input.strip() == "view"):
            view()
        elif (user_input.strip() == "all"):
            all()
        else:
            print("Please enter a valid command (type help for more info):\n")


if __name__ == "__main__":
    main()
