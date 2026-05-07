#!/usr/bin/env python3
import sys               # Import the sys module to handle incoming arguments from command line 

def crack_cipher(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # English alphabet reference 
    # Special characters to remove from the obscured text 
    obscure_chars = "@#$%^&" # Defines the string of special characters 
    
    # Clean the input: remove obscure chars but DO NOT force uppercase yet 
    clean_text = "".join([c for c in ciphertext if c not in obscure_chars]) 

    print(f"Brute-forcing all 26 keys:\n")
    for key in range(26): # Loops through all 26 possible shift keys in the alphabet
        decrypted = "" # Initialize and empty string for current decryption attempt
        for char in clean_text: # Iterates through each character in cleaned text
            # Check if character is an uppercase letter
            if char.isupper():
                idx = alphabet.find(char)
                # Apply backward shift and keep uppercase
                decrypted += alphabet[(idx - key) % 26]
            # Check if character is a lowercase letter
            elif char.islower():
                # Find index using the uppercase version of the character
                idx = alphabet.find(char.upper()) # Finds the index upper level equivalent
                # Apply backward shift and convert result back to _lowercase
                decrypted += alphabet[(idx - key) % 26].lower()
            else:
                # Keep spaces, punctuation, and non-alphabetic chars as is 
                decrypted += char # Append the original character without modification
        print(f"Key {key:02}: {decrypted}") # Output key and result 

if __name__ == "__main__":
    # Default ciphertext 
    ciphertext = "Jycu yi jxu bed%wuij tyijqdsu rujmuud jm^e fbqsui" # Given ciphertext

    if len(sys.argv) > 1:
        crack_cipher(sys.argv[1]) # Handle command line input 
    else:
        crack_cipher(ciphertext)  # Use default text

# To run wner in sudo need to run in Powershell <wsl -d Ubuntu -u root>