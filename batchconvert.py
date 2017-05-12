import sys

if len(sys.argv) == 1:
    print("Must add a .py file to convert to batch")
    sys.exit()
elif len(sys.argv) > 2:
    print("This script accepts one argument")
    sys.exit()
elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".py"):
        user_input = input("You are about to create a batch file from the specified file, do you wish to continue? y/n") == "Y":
