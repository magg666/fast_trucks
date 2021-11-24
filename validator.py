# Global variable for validation - shortcut for country has three letters. I pulled it out here, because it is easy
# to find and can be used in other functions if the application is expanded
SHORTCUT_LENGTH = 3


def is_shortcut_valid(shortcut):
    """
    Validate input
    :param shortcut:str
    :return: bool
    """
    str_shortcut = str(shortcut)
    return str_shortcut.upper() and str_shortcut.isalpha() and len(str_shortcut) == SHORTCUT_LENGTH



