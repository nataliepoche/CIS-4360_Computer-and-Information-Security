import hashlib # Imports library used for secure hashing
import sys # Imports system-specific parameters and functions, used for terminal arguments
import os # Imports operating system interface (used to check og the wordlist file exists)

def generate_custom_hash(password: str) -> str:
    # The provided inputs should be UTF-8 encoded before being processed
    data = password.encode('utf-8')

    # MD5 100 times (feeding the output as a raw digest into the next)
    for i in range(100):
        data = hashlib.md5(data).digest()

    # SHA256 100 times (feeding the output as a raw digest into the next)
    for i in range(100):
        data = hashlib.sha256(data).digest()

    # SHA512 100 times (feeding the output as a raw digest into the next)
    for i in range(100):
        data = hashlib.sha512(data).digest()

    # The final output should be a hexadecimal string
    return data.hex()

def main():
    #Checks if the user provided a hash in the terminal commandline
    if len(sys.argv) != 2:
        # If no hash was provided, set a default target hash to look for
        target_hash = "e44afbf84f0b3af3a9621a9dfe468c9c98d6fd381a735e243126963557067bb7e9a035c8316b1af763692039cd43d483b58923ac82fc60d897c6d8befb6f48a3"
        print(f"Usage: ./crack_hashes <custom_hash>, using default hash = {target_hash}")
    else:
        # If a hash was provided as an argument, use it as the target
        target_hash = sys.argv[1].strip()
    
    # Define the path to the wordlist file
    wordlist_path = 'rockyou-20.txt'

    # Check if the wordlist file actually exists in the current folder
    if not os.path.exists(wordlist_path):
        print(f"Error {wordlist_path} not found in the current directory.")
        sys.exit(1) # Stops the script with an error code

    print(f"[*] Targeting Hash: {target_hash}")
    print("[*] Processing wordlist...")
    
    # Open the wordlost file for reading : 'ignore' ensures it doesn't crash on weird characters
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
        # Iterates through every single line (password) in the file
        for line in file:
            # Removes trailing newlines or spaces from the password
            password = line.strip()

            # Run the 300-round custom hashing function on the current word
            hashed_attempt = generate_custom_hash(password)

            # Compare the generated hash against the target hash
            if hashed_attempt == target_hash:
                # If they match, print th esuccess message and found password
                print(f"\n[+] SUCCESS! Password found: {password}")
                sys.exit(0) # Exit the script successfully

    # If the loop finishes without finding a match, notify the user
    print("\n[-] Password not found in the wordlist.")

# Wnsures the main() function only runs if the script is executed directly
if __name__ == "__main__":
    main()