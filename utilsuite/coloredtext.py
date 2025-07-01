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
        from . import colorPalette
        self.cp = colorPalette()
        init(autoreset=True)
        def get_rgb_color(color_str):
            color = self.cp.rgb(color_str)
            return f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
        self.color_dict = {
            'r': get_rgb_color('r'),
            'r2': Fore.RED,
            'g': get_rgb_color('g'),
            'g2': Fore.GREEN,
            'b': get_rgb_color('b'),
            'b2': Fore.BLUE,
            'pi': get_rgb_color('pi'),
            'br': get_rgb_color('br'),
            'm': Fore.MAGENTA,
            'c': Fore.CYAN,
            'w': Fore.WHITE,
            'y': Fore.LIGHTYELLOW_EX,
            'k': Fore.BLACK,
            'o': get_rgb_color('o'),
            'o2': "\033[38;2;255;165;0m",
            'default': Fore.RESET,
        }
        self.background_dict = {
            'default': Back.RESET,
            'r': Back.RED,
            'g': Back.GREEN,
            'b': Back.BLUE,
            'm': Back.MAGENTA,
            'c': Back.CYAN,
            'w': Back.WHITE,
            'y': Back.YELLOW,
            'k': Back.BLACK,
        }
        self.style_dict = {}
        self.style_dict['b'] = self.style_dict['bold'] = Style.BRIGHT
        self.reset = Style.RESET_ALL
        
    def print(self, text, color=None, background=None, style=None):
        color = self.color_dict.get(color, self.color_dict['default'])
        background = self.background_dict.get(background, self.background_dict['default'])
        style = self.style_dict.get(style, '')
        print(f"{color}{background}{style}{text}{self.reset}")