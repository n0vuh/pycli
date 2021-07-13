from pycli import theme
from colorama import Fore, init
from os import system

system("cls")
init(convert=True)

theme = theme.cli(Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTMAGENTA_EX)

theme.print("Tagged print function with no set tag", True)

theme.input("prompt expecting a integer", int)
theme.input("prompt expecting a string", str)
theme.input("prompt expecting a float", float)

theme._bench()