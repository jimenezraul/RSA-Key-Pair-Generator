import os
import subprocess

def generate_key_pair(private_key_name):
    # Generate private key
    subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-out", private_key_name])

    # Generate public key from private key
    subprocess.run(["openssl", "rsa", "-pubout", "-in", private_key_name, "-out", private_key_name.replace("private_key", "public_key")])

def process_pem_files():
    access_private_key = ""
    refresh_private_key = ""
    access_public_key = ""
    refresh_public_key = ""

    # get all files in the root directory
    files = os.listdir()

    # Create a list of all the .pem files
    pem_files = [f for f in files if f.endswith('.pem')]

    for pem_file in pem_files:
        with open(pem_file) as f:
            lines = f.readlines()
            lines = lines[1:-1]
            lines = [line.strip() for line in lines]

            # Join the lines together into one string
            key_content = ''.join(lines)

            if "access_private_key" in pem_file:
                access_private_key = key_content
            elif "refresh_private_key" in pem_file:
                refresh_private_key = key_content
            elif "access_public_key" in pem_file:
                access_public_key = key_content
            elif "refresh_public_key" in pem_file:
                refresh_public_key = key_content
            
        # remove the pem file
        os.remove(pem_file)

    with open("key_pairs.txt", "w") as output_file:
        output_file.write(f"ACCESS_PRIVATE_KEY={access_private_key}\n")
        output_file.write(f"ACCESS_PUBLIC_KEY={access_public_key}\n")
        output_file.write(f"REFRESH_PRIVATE_KEY={refresh_private_key}\n")
        output_file.write(f"REFRESH_PUBLIC_KEY={refresh_public_key}\n")

    print("Key pairs written to key_pairs.txt")

def main():
    generate_key_pair("access_private_key.pem")
    generate_key_pair("refresh_private_key.pem")
    process_pem_files()

if __name__ == "__main__":
    main()
