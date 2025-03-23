from argparse import RawDescriptionHelpFormatter
from argparse import ArgumentParser
import os

# To load ASCII art
def load_ascii():
    """
    Load ascii art from the .txt file
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ascii_path = os.path.join(script_dir, "ascii.txt")
    with open(ascii_path, "r") as ascii:
        ascii_art = ascii.read()
        return ascii_art

def load_cli():
    
    # Loading the ASCII
    ascii_art = load_ascii()

    # The argument Parser Object
    parser = ArgumentParser(
        prog = "pyword",
        description = f"{ascii_art} \n Python Password Generation Tool",
        formatter_class=RawDescriptionHelpFormatter
    )

    # Program arguments
    # PW arguments
    parser.add_argument("-n",
                        "--numbers",
                        default=0,
                        help="Number of digits in the PW",
                        type=int)

    parser.add_argument("-l",
                        "--lowercase",
                        default=0,
                        help="Number of lowercase chars in the PW",
                        type=int)

    parser.add_argument("-u",
                        "--uppercase",
                        default=0,
                        help="Number of uppercase chars in the PW",
                        type=int)

    parser.add_argument("-s",
                        "--special-chars",
                        default=0,
                        help="Number of special chars in the PW",
                        type=int)

    parser.add_argument("-t",
                        "--total-length",
                        help="The total password length. If passed, it will ignore the -n, -l, -u and -s",
                        type=int)

    # Output arguments
    parser.add_argument("-a",
                        "--amount",
                        default=1,
                        help="Number of passwords to output",
                        type=int)
    parser.add_argument("-o",
                        "--output-file",
                        help="Output file")

    return parser
