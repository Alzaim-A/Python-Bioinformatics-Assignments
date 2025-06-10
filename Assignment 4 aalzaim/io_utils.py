"""io_utils.py: Utility"""

import os
import sys


def mkdir_from_infile(file: str) -> None:
    """
    void : mkdir_from_infile("/home/cleslin/test.txt")
    Takes : 1 argument, tries to create a directory from an infile string passed in
    @param file: The fh_in it will then try and make a directory from it's root
    @return: None
    """
    directory = os.path.dirname(file)
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except PermissionError as err:
        # raising like this allows the overall application to choose whether
        # to stop running gracefully or handle the exception.

        # Printing exceptions to sys.stderr is a good practice, especially in larger or more complex applications.
        # By default, uncaught exceptions are written to sys.stderr in Python, and explicitly doing so for caught
        # exceptions can help maintain consistency in how error messages are logged.
        print(f"{err}\nPermissionError: Could not mkdir {directory}", file=sys.stderr)
        raise
    except FileNotFoundError as err:
        # if the file is only a string with no /, you'll get : No such fh_in or directory: ''
        print(f"{err}\nFileNotFoundError: b/c file does not exist {directory}", file=sys.stderr)
        raise
    except OSError as err:
        print(f"{err}\nOSError: A more generic error at the OS level occurred {directory}", file=sys.stderr)
        raise
