import secrets
import random 
import string

def gen_pw(amount, n, u, l, s, total_length=None):
    """
    Password generating function
    """

    passwords = []
    if total_length:
        for _ in range(amount):
            passwords.append("".join([secrets.choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(total_length)]))
    
    else:
        for _ in range(amount):
            password = []
            for _ in range(n):
                password.append(secrets.choice(string.digits))

            for _ in range(u):
                password.append(secrets.choice(string.ascii_uppercase))

            for _ in range(l):
                password.append(secrets.choice(string.ascii_lowercase))

            for _ in range(s):
                password.append(secrets.choice(string.punctuation))

            random.shuffle(password)
            passwords.append("".join(password))

    return passwords

def save_pw_file(file, passwords):
    """
    Output file saving function
    """

    with open(file, "w") as output:
        output.write("\n".join(passwords))
    
    # Encryption utils need to be added here for the output file
    return
