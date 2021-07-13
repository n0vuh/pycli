from typing import Any
from colorama import Fore, Style, Back
import os, ctypes
import pycli


class cli:
    def __init__(self, primary: Fore, secondary: Fore, highlight: Fore, text: Fore=Fore.WHITE):
        """
        
        pycli base class

        ---

        Parameters:
        ```
        primary : AnsiFore
            Primary color, used for title and basic tags.
        secondary : AnsiFore
            Secondary color, used wherever needed.
        highlight : AnsiFore
            Text highlight color.
        text : AnsiFore
            Text color, defaults to white.
        ```
        
        """
        self.primary = primary
        self.secondary = secondary
        self.highlight = highlight
        self.text_color = text

        self.cmd = Style.BRIGHT + f"{self.secondary}[{self.primary}CMD{self.secondary}]{self.text_color} "
        self.warn = Style.BRIGHT + f"{self.secondary}[{Fore.YELLOW}WARN{self.secondary}]{self.text_color} "
        self.error = Style.BRIGHT + f"{self.secondary}[{Fore.RED}ERROR{self.secondary}]{self.text_color} "
    
    def get_console_width(self) -> int:
        """Returns console width."""
        return os.get_terminal_size().columns
    
    def clear(self):
        """Clears console, only for windows."""
        os.system('cls')

    def set_window_title(self, title: str):
        """Sets the window title, only for windows."""
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    
    def _bench(self):
        """pycli benchmark, for presentation purposes."""
        print(f"""
        {Style.BRIGHT}PyCLI v{pycli.__version__}

        {self.cmd} command tag
        {self.warn} warn tag
        {self.error} error tag

        {Fore.WHITE}{self.primary}Primary Color
        {Fore.WHITE}{self.secondary}Secondary Color
        {Fore.WHITE}{self.highlight}Highlight Color
        {Fore.WHITE}{self.text_color}Text Color{Fore.WHITE}

        """)
        
    def print(self, object: Any, tagged: bool=True, tag: str=None) -> None:
        """
        
        Prints to console.

        Tags: (cli.cmd, cli.warn, cli.error)

        ---

        Parameters:
        ```
        object : Any
            The object to print to console.
        tagged : bool (optional)
            Whether or not to use a set tag prefix.
            Default : True
        tag : str (optional)
            The tag to use (cli.cmd, cli.warn, cli.error)
        ```
        
        """
        if tagged == True and tag == None:
            print(self.cmd + str(object))
        elif tagged == True and tag != None:
            print(tag + str(object))
        else:
            print(object)
    
    def input(self, prompt: str, required_type: Any=str):
        """
        
        Gets input from user.

        ---

        Parameters:
        ```
        prompt : str
            The prompt for the user.
        required_type : Any (optional)
            The expected input type.
            Default : str
        ```
        
        """
        while True:
            try:
                res = required_type(input(self.cmd + f"{self.text_color}{prompt}{self.primary} -> {self.highlight}"))
                break
            except ValueError:
                self.print(f"Please provide a(n) {required_type.__name__}", True, self.error)
        return res