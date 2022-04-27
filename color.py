class Color:
    __version__ = "1.0.0"
    """
    Class for formatted print in a terminal
    """
    __styles = {
        "clr"       : '\033[0m', # clear formatting
        "clear"     : '\033[0m',

        "bold"      : '\033[1m', # bold
        "bld"       : '\033[1m', 

        "fdd"       : '\033[2m', # faded

        "italic"    : '\033[3m', # italic
        "itl"       : '\033[3m',

        "line"      : '\033[4m', # underscore
        "und"       : '\033[4m',

        "s_flash"   : '\033[5m', # slow flash
        "sfl"       : '\033[5m',

        "f_flash"   : '\033[6m', # fast flash
        "ffl"       : '\033[6m',

        "inversion" : '\033[7m', # invert text and background color
        "inv"       : '\033[7m',

        # Text color
        "blk"     : '\033[30m', # black
        "black"   : '\033[30m',
        "k"       : '\033[30m',

        "red"   : '\033[31m', # red
        "r"     : '\033[31m',

        "grn"   : '\033[32m', # green
        "green" : '\033[32m', 
        "g"     : '\033[32m',

        "yel"   : '\033[33m', # yellow
        "yellow": '\033[33m',
        "y"     : '\033[33m',

        "blue"  : '\033[34m', # blue
        "b"     : '\033[34m',

        "prp"    : '\033[35m', # magenta
        "purple" : '\033[35m',
        "magenta": '\033[35m',
        "mgt"    : '\033[35m',
        "m"      : '\033[35m',

        "trq"   : '\033[36m', # cyan
        "cyan"  : '\033[36m',
        "c"     : '\033[36m',

        "wht"   : '\033[37m', # white
        "white" : '\033[37m', 
        "w"     : '\033[37m',

        # Background styles
        "blk_f" : '\033[40m', # black
        "kf"    : '\033[40m',

        "red_f" : '\033[41m', # red
        "rf"    : '\033[41m',

        "grn_f" : '\033[42m', # green
        "gf"    : '\033[42m',

        "yel_f" : '\033[43m', # yellow
        "yf"    : '\033[43m',

        "blue_f": '\033[44m', # blue
        "bf"    : '\033[44m',

        "prp_f" : '\033[45m', # magenta
        "mgt_f" : '\033[45m', 
        "mf"    : '\033[45m',

        "trq_f" : '\033[46m', # cyan
        "cf"    : '\033[46m',

        "wht_f" : '\033[47m', # white
        "wf"    : '\033[47m',
    }

    @classmethod
    def decolor(cls, *text):
        """Removes color keys from text

        text: input args as in python print() function
        returns list of decolored strings
        """
        txt_clear = []
        for txt in text:
            txt = str(txt)
            for key, _ in cls.__styles.items():
                txt_key = f"<{key}>"
                txt = txt.replace(txt_key, "")
            txt_clear.append(txt)
        return txt_clear

    @classmethod
    def print(cls, *text, **kwargs):
        """Parses input text for color keys "<key>" and replaces them with
        special symbols

        text: list with input for python print() function
        kwargs: forwarded to python print() function
        """
        colored = []
        for txt in text:
            txt = str(txt)
            for key, mark in cls.__styles.items():
                txt_key = f"<{key}>"
                txt = txt.replace(txt_key, mark)
            txt = txt + cls.__styles["clr"]
            colored.append(txt)
        print(*colored, **kwargs) 

    @classmethod
    def print2(cls, *text, **kwargs):
        """Same as print but returns uncolored text
        """
        cls.print(*text, **kwargs)
        return cls.decolor(*text)