import os
import subprocess

def generate_key_pair(private_key_name):
    # Generate private key
    subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-out", private_key_name])

    # Generate public key from private key
    subprocess.run(["openssl", "rsa", "-pubout", "-in", private_key_name, "-out", private_key_name.replace("private_key", "public_key")])

def process_pem_files():
    all_keys = {}

    # get all files in the root directory
    files = os.listdir()

    # Create a list of all the .pem files
    pem_files = [f for f in files if f.endswith('.pem')]

    for pem_file in pem_files:
        # Remove the .pem extension
        fileName = pem_file.split(".pem")[0]
        
        with open(pem_file) as f:
            lines = f.readlines()
            lines = lines[1:-1]
            lines = [line.strip() for line in lines]

            # Join the lines together into one string
            key_content = ''.join(lines)

            # Add the key to the dictionary
            all_keys[fileName] = key_content
            
        # remove the pem file
        os.remove(pem_file)

    with open("key_pairs.txt", "w") as output_file:
        for key, value in all_keys.items():
            output_file.write(f"{key.upper()}={value}\n")

    print("Key pairs written to key_pairs.txt")

def main():
    generate_key_pair("access_private_key.pem")
    generate_key_pair("refresh_private_key.pem")
    process_pem_files()

if __name__ == "__main__":
    main()
