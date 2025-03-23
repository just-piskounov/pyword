#!/usr/bin/env python3
from cli import load_cli
from utils.helpers import gen_pw, save_pw_file

def main():
    
    # Loading the CLI
    parser = load_cli()

    # Displaying the interface

    # Loading the scripts arguments
    args = parser.parse_args()

    # Generating the passwords
    passwords = gen_pw(args.amount,
                       args.numbers,
                       args.lowercase,
                       args.uppercase,
                       args.special_chars,
                       args.total_length)
 

    save_pw_file("passwords.txt", passwords )    

    return 

if __name__ == "__main__":
    main()
