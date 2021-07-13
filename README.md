## PyCli
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

```
# windows
import os
from pycli.theme import cli
from colorama import Fore

os.system("cls")

theme = cli(Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.LIGHTMAGENTA_EX)
```

### Print
```
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

### Input
<p>PyCli allows you to have an "expected" output, i.e int or float.</p>
```
...
# input expecting a integer
theme.input("prompt", int)

# input expecting a float
theme.input("prompt", float)

# input expecting a string
theme.input("prompt", string)
```

### Misc
```
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