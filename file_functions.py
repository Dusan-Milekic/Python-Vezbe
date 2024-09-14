from colorama import Fore, Back


def intro_program_file():
    print(Back.BLACK + Fore.BLUE + "\n" + ("*" * 40) + "\n" + "FILE PROGRAM\n" + ("*" * 40) + "\n")


def ffile_read():
    print(Fore.YELLOW)  # Place color Yellow to Text
    file = open("text_file.txt")  # Open file with read / default
    print(file.read())  # print read file
    file.close()


def ffile_append():
    file = open("text_file.txt", "a")
    file.write("\nPC - Added new Text")
    file.close()


def ffile_rewrite():
    file = open("text_file.txt", "w")
    file.write("\nFile was rewrote by PC")


def file_program():
    intro_program_file()

    # Get User input
    user_input = int(input("Enter what you want: \n"
                           "\n[1] Read file"
                           "\n[2] Append file"
                           "\n[3] ReWrite file\n"))

    if user_input == 1:
        ffile_read()
    elif user_input == 2:
        ffile_append()
        ffile_read()
    elif user_input == 3:
        ffile_rewrite()
        ffile_read()
