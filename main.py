
from my_functions import intro_to_program, show_refresh_time
from file_functions import file_program


print("Choose your program you want to use: \n"
      "[1] Refreshing datetime\n"
      "[2] File Program")

user_choice = int(input("Enter your choice: "))

if user_choice == 1:
    intro_to_program()
    show_refresh_time()
else:
    file_program()