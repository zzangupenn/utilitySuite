class coloredText:
    """
    Utility class for printing colored and styled text to the terminal.

    Uses the `colorama` library for cross-platform color support and ANSI escape codes
    for true-color orange. Supports foreground colors, background colors, and styles.

    Attributes:
    -----------
    color_dict : dict
        Maps color names and single-letter shortcuts to ANSI color codes for text.
    background_dict : dict
        Maps color names and shortcuts to ANSI background color codes.
    style_dict : dict
        Maps style names (e.g., 'bold') and shortcuts to ANSI style codes.
        
    Methods:
    --------
    print(text, color=None, background=None, style=None):
        Prints the given text with optional foreground color, background color, and style.
        Parameters accept keys or single-letter shortcuts as defined in the dictionaries.

    Example:
    --------
    ct = coloredText()
    ct.print("Hello World", color='r', background='w', style='b')
    """
    def __init__(self) -> None:
        from colorama import Fore, Back, Style, init
        init(autoreset=True)
        self.color_dict = {}
        self.color_dict['o'] = self.color_dict['orange'] = "\033[38;2;255;165;0m"
        self.color_dict['m'] = self.color_dict['magenta'] = Fore.MAGENTA
        self.color_dict['g'] = self.color_dict['green'] = Fore.GREEN
        self.color_dict['b'] = self.color_dict['blue'] = Fore.BLUE
        self.color_dict['r'] = self.color_dict['red'] = Fore.RED
        self.color_dict['c'] = self.color_dict['cyan'] = Fore.CYAN
        self.color_dict['w'] = self.color_dict['white'] = Fore.WHITE
        self.color_dict['y'] = self.color_dict['yellow'] = Fore.LIGHTYELLOW_EX
        self.color_dict['k'] = self.color_dict['black'] = Fore.BLACK
        self.color_dict['default'] = Fore.RESET
        self.background_dict = {}
        self.background_dict['default'] = Back.RESET
        self.background_dict['r'] = self.background_dict['red'] = Back.RED
        self.background_dict['g'] = self.background_dict['green'] = Back.GREEN
        self.background_dict['b'] = self.background_dict['blue'] = Back.BLUE
        self.background_dict['m'] = self.background_dict['magenta'] = Back.MAGENTA
        self.background_dict['c'] = self.background_dict['cyan'] = Back.CYAN
        self.background_dict['w'] = self.background_dict['white'] = Back.WHITE
        self.background_dict['y'] = self.background_dict['yellow'] = Back.YELLOW
        self.background_dict['k'] = self.background_dict['black'] = Back.BLACK
        self.style_dict = {}
        self.style_dict['b'] = self.style_dict['bold'] = Style.BRIGHT
        self.reset = Style.RESET_ALL
        
    def print(self, text, color=None, background=None, style=None):
        color = self.color_dict.get(color, self.color_dict['default'])
        background = self.background_dict.get(background, self.background_dict['default'])
        style = self.style_dict.get(style, '')
        print(f"{color}{background}{style}{text}{self.reset}")