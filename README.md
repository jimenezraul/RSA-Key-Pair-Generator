# RSA Key Pair Generator

This Python script generates RSA key pairs and processes the generated PEM files to create a consolidated output file containing key pairs in a specific format.

## Features

- Generates RSA key pairs using OpenSSL commands.
- Processes generated PEM files to create key pairs in a consolidated output format.
- Outputs the key pairs to a single file with designated variable names.

## Prerequisites

- Python 3.x
- OpenSSL (for key generation)

## Usage

1. Clone this repository:

   ```sh
   git clone https://github.com/jimenezraul/RSA-Key-Pair-Generator.git
   ```

2. Go to the cloned repository:

   ```sh
   cd RSA-Key-Pair-Generator
   ```

3. Run the script:

   ```sh
   python main.py
   ```

## Output

The script will generate a file named `key_pairs.txt` in the same directory that will contain the key pairs in the following format:

```sh
ACCESS_PRIVATE_KEY=<Access Private Key Content>
ACCESS_PUBLIC_KEY=<Access Public Key Content>
REFRESH_PRIVATE_KEY=<Refresh Private Key Content>
REFRESH_PUBLIC_KEY=<Refresh Public Key Content>
```
