import datetime
import time
from colorama import Fore, Back, Style


def intro_to_program():
    #Chage font color,bg and add style stars
    print(Back.YELLOW + Fore.BLACK + "\n\n" + ("*" * 40) + "\nWelcome to the App DateTime Now!\n" + ("*" * 40) + "\n")
    print(Style.RESET_ALL)


def show_time_now(message_number):
    my_time = datetime.datetime.now().strftime("%H:%M:%S")
    if message_number % 2 == 0:
        print(Fore.LIGHTBLUE_EX + my_time + Fore.RESET)
    else:
        print(Fore.MAGENTA + my_time + Fore.RESET)


def show_refresh_time():
    while 1 == 1:
        show_time_now(0)
        time.sleep(1)
