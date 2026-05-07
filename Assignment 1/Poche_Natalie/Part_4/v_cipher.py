#!/usr/bin/env python3
import sys
from itertools import product # Imports profuct to generate all possible key combinations

def decrypt_vigenere(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = [] # Initialize list to store resulting characters
    k_idx = 0 # Initialize pointer for the current position in the key
    
    # Ensure the key is treated as uppercase for consistent index finding
    key = key.upper() # Ensures key is uppercase for conistent index lookups
    
    for char in ciphertext: # Iterates through every character in ciphertext
        # Check if the character is an uppercase letter
        if char.isupper():
            shift = alphabet.find(key[k_idx % len(key)]) # Determines shift value based on current key character
            char_idx = alphabet.find(char) # Get the alphabetical index of the ciphertext character
            # Apply backward shift and keep as uppercase
            res.append(alphabet[(char_idx - shift) % 26]) # Applies the baackward shift and append the uppercase result to the list
            k_idx += 1 #Increaments the key index onlt when the alphabetic char is shifted
        # Check if the character is a lowercase letter
        elif char.islower():
            shift = alphabet.find(key[k_idx % len(key)])
            # Use uppercase version to find the index in our reference alphabet
            char_idx = alphabet.find(char.upper())
            # Apply shift and convert back to lowercase
            res.append(alphabet[(char_idx - shift) % 26].lower())
            k_idx += 1 # Increments key index when alphabetic char is shifted
        else:
            # If it is punctuation, a space, or a number, keep it exactly as is
            res.append(char) # Appends the char to the result list without modifications
            
    return "".join(res) # Joins the list of characters into a single string

def brute_force_vigenere(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Testing keys of length 1, 2, 3, and 4
    for length in range(1, 5):
        print(f"--- Testing keys of length {length} ---")
        for key_tuple in product(alphabet, repeat=length): # Generates every possible alphabetical combination for current key length being tested
            key = "".join(key_tuple) # Converts the generated key tuple into a string
            decoded = decrypt_vigenere(ciphertext, key) # Decrypts the ciphertext using the given key
            
            print(f"Key {key}: {decoded}")

            # Removed because it asks for  full output of every possible key combination
            # # Simple heuristic: only print if common English words are found
            # # Use .upper() for the check to ensure we catch "the", "THE", or "The"
            # if " THE " in decoded.upper() or " AND " in decoded.upper(): # Checks if common English word appears in decrypted text
            #     print(f"Key {key}: {decoded}") # Prints the successful key and the resulting plaintext

if __name__ == "__main__":
    # Assigned ciphertext from the assignment
    ciphertext = "THH YOROF BRHCKS HXERBQNE, DPD AIVERZCRD, VQME DTE SWTONJ CT TKG BRRMEN SNACHU"

    if len(sys.argv) > 1:
        # Allow passing a different ciphertext via command line
        brute_force_vigenere(sys.argv[1])
    else:
        # Run with the default ciphertext
        brute_force_vigenere(ciphertext)