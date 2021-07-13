# PyCli
![last](https://img.shields.io/github/last-commit/n0vuh/pycli) ![release](https://img.shields.io/github/v/release/n0vuh/pycli) ![stars](https://img.shields.io/github/stars/n0vuh/pycli)\
A simple module to assist in creating lightweight, clean CLIs/TUIs that is built on-top of Colorama.

## Get Started
### Install required dependencies.
<p>PyCli is programmed to use Colorama for the coloring of text in the console. This means you need to have colorama installed.
Installing Colorama via pip:
`pip install colorama` or `python -m pip install colorama`

You're also going to need to add PyCli to your project directory or install it via pip.
<b>Note: PyCli is not on PyPi yet.</b>
</p>

### Initialize PyCli

```py
# windows
import os
from pycli.theme import cli
from colorama import Fore

os.system("cls")

theme = cli(Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTMAGENTA_EX)
```

### Print
```py
...
# print with default CMD tag
theme.print("Hello World!", True)

# print with set tag that's built-in
theme.print("Hello World!", True, theme.warn)

# print with custom tag
theme.print("Hello World!", True, "[custom tag] ")

# print without tag
theme.print("Hello World!", False)
```
![Imgur](https://i.imgur.com/VNT38Zn.png)

### Input
```py
...
# input expecting a integer
theme.input("prompt", int)

# input expecting a float
theme.input("prompt", float)

# input expecting a string
theme.input("prompt", string)
```
![Imgur](https://i.imgur.com/PoSSG3E.png)

### Misc
```py
...
# set console window
theme.set_window_title("title here, also supports special chars! }/^*#()")

# get console width
print(theme.get_console_width())

# clear console
theme.clear()

# bench
theme._bench()
```
![Imgur](https://i.imgur.com/JJSH31t.png)\
![Imgur](https://i.imgur.com/evDrBEY.png)\
![Imgur](https://i.imgur.com/Rbfe2K6.png)
