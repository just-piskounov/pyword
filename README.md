# PyWord - Password Generator

**PyWord** is a command-line password generator tool written in Python. It allows you to generate secure passwords with customizable length and complexity. I will include output file encryption next.

## Features

- Generate secure passwords with customizable length.
- Specify the number of passwords to generate.
- Easy-to-use command-line interface (CLI).

## Installation

### Prerequisites

- Python 3.7 or higher.
- GPG (GNU Privacy Guard) installed on your system (optional, for encryption).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pyword.git
   cd pyword
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Allow the script to be executable (optional):
   ```bash
   chmod +x run.py
   ```

4. (Optional) Set up GPG for encryption:
   - Ensure GPG is installed on your system.
   - Generate a GPG key pair if you don't already have one:
     ```bash
     gpg --full-generate-key
     ```
   - Export your public key:
     ```bash
     gpg --export --armor your-email@example.com > public-key.pem
     ```

## Usage

### Generate Passwords

To generate passwords, run the following command:

```bash
  ./run.py --help
```

## Project Structure

```
pyword/
├── cli/
│   ├── ascii.txt          # ASCII art for the CLI
│   ├── cli.py             # CLI implementation
│   ├── __init__.py        # Package initialization
├── LICENSE                # License file
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── run.py                 # Main script
├── tests/                 # Unit tests
│   └── __init__.py
└── utils/                 # Utility functions
    ├── helpers.py
    └── __init__.py
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your fork.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Python community for awesome tools and libraries.
- Inspired by the need for secure and customizable password generation.
